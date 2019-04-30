print("Operations:")
print("1 = num1 + num2")
print("2 = num1 - num2")
print("3 = num1 * num2")
print("4 = num1 / num2")
num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
operation = int(input("Enter your operation:"))

if operation == 1:
    print(num1 + num2)
elif operation == 2:
    print(num1 - num2)
elif operation == 3:
    print(num1 * num2)
elif operation == 4:
    print(num1 / num2)