import select
import socket
import sys
import signal
import argparse

SERVER_HOST = "localhost"  # 127.0.0.1
CHAT_SERVER_NAME = "server"
RCV_SIZE = 1024


def send(channel, *args):
    # Send message to socket
    buffer = "".join(args)
    channel.sendall(buffer.encode())


def receive(channel):
    # Return message received from socket
    return channel.recv(RCV_SIZE).decode()


class Chat_Server:
    """This class for server part of chat"""

    def __init__(self, port, backlog=5):
        self.clients = 0
        self.client_map = {}
        self.outputs = []   # list output sockets
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Enable re-using socket address
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((SERVER_HOST, port))
        print("Server listening to port: {}".format(port))
        self.server.listen(backlog)     # Catch keyboard interrupts
        signal.signal(signal.SIGINT, self.sighandler)

    def sighandler(self, signum, frame):
        """ Clean up client outputs"""
        # Close the server
        print("Shutting down server")

        # Close existing client sockets
        for output in self.outputs:
            output.close()
        self.server.close()

    def get_client_name(self, client):
        """ Return the name of the client """
        info = self.client_map[client]
        host, name = info[0][0], info[1]
        return "@".join((name, host))


    def run(self):
        inputs = [self.server, sys.stdin]
        self.outputs = []
        running = True
        while running:
            # Wait for message from client or keyboard input
            try:
                readable, writeable, exceptional = select.select(inputs, self.outputs, [])
            except (select.error, ValueError):
                break

            for sock in readable:
                # Accept new clients
                if sock == self.server:     # handle the server socket
                    client, address = self.server.accept()
                    print("Chat server: got connection from {}".format(address))

                    # Read the login name
                    client_name = receive(client).split("NAME: ")[1]
                    # Compute client name and send back
                    self.clients += 1
                    send(client, "CLIENT: " + str(address[0]))
                    inputs.append(client)
                    self.client_map[client] = (address, client_name)   # Send joining information to other clients
                    message = "\n(Connected: New client {} from {})".format(self.clients, self.get_client_name(client))

                    for output in self.outputs:
                        send(output, message)
                    self.outputs.append(client)
                # Exit program if press Enter
                elif sock == sys.stdin:
                    # handle standard input
                    junk = sys.stdin.readline()
                    running = False
                    print("You can not writing into server console")
                # Read message from client
                else:
                    try:
                        data = receive(sock)
                        # Send message to all clients
                        if data:
                            # Send as new client's message
                            message = "\n#[" + self.get_client_name(sock) + "]>>" + data

                            # Send data to all except ourself
                            for output in self.outputs:
                                if output != sock:
                                    send(output, message)
                        # Close socket of disconnected client and notify other clients
                        else:
                            print("Client {} was disconnected".format(self.get_client_name(sock)))
                            self.clients -= 1
                            sock.close()
                            inputs.remove(sock)
                            self.outputs.remove(sock)
                            # Sending client leaving info to others
                            message = "\nClient {} was disconnected".format(self.get_client_name(sock))

                            for output in self.outputs:
                                send(output, message)
                    except socket.error:
                        inputs.remove(sock)
                        self.outputs.remove(sock)
        self.server.close()


class Chat_Client:
    """ This class for client part of chat"""

    def __init__(self, name, port, host=SERVER_HOST):
        self.name = name
        self.connected = False
        self.host = host
        self.port = port
        # Initial prompt
        self.prompt = "[" + "@".join((name, socket.gethostname().split('.')[0])) + "]> "
        # Connect to server at port
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((host, self.port))
            print("Now connected to chat server@ port {}".format(self.port))
            self.connected = True
            send(self.sock, "NAME: " + self.name)
            data = receive(self.sock)
            # Contains client address, set it
            address = data.split("CLIENT: ")[1]
            self.prompt = "[" + "@".join((self.name, address)) + "]> "
        except socket.error:
            print("Failed to connect to chat server @ port {}".format(self.port))
            sys.exit(1)

    def run(self):
        """ Chat client main loop """
        while self.connected:
            try:
                # Print prompt
                sys.stdout.write(self.prompt)
                sys.stdout.flush()
                # Wait for input from keyboard or socket
                readable, writeable, exceptional = select.select([0, self.sock], [], [])

                for sock in readable:
                    # Read from keyboard and send to server
                    if sock == 0:
                        data = sys.stdin.readline().strip()
                        if data: send(self.sock, data)
                    # Read message from server
                    elif sock == self.sock:
                        data = receive(self.sock)
                        # Server closed
                        if not data:
                            print("Client shutting down because server dropped connection.")
                            self.connected = False
                            break
                        # Print message from server
                        else:
                            sys.stdout.write(data + "\n")
                            sys.stdout.flush()
            except KeyboardInterrupt:
                print("Client interrupted.")
                self.sock.close()
                break

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Socket ServerExample with Select")
    parser.add_argument("--name", action="store", dest="name", required=True)
    parser.add_argument("--port", action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    name = given_args.name
    if name == CHAT_SERVER_NAME:
        server = Chat_Server(port)
        server.run()
    else:
        client = Chat_Client(name=name, port=port)
        client.run()
