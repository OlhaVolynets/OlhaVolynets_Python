# ============================================1
# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))

# if a > b:
    # print("biggest number is {}".format(a))
# else:
    # print("biggest number is {}".format(b))

# =============================================2

# num = float(input("Enter number: "))

# if (num % 2) == 0:
    # print("Number {} is even number".format(num))
# else:
    # print("Number {} is odd number".format(num))

# ==============================================3

user = float(input("Enter your number: "))
result = 1
x = 1

while x <= user:
    result *= x
    x += 1
print("Factorial number's {} is {}".format(user, result))

