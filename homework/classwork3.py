user = float(input("Enter your number: "))
result = 1
x = 1

while x <= user:
    result *= x
    x += 1
print("Factorial number's {} is {}".format(user, result))