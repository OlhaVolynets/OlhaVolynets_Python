# -------------------------1----------------------
# def arithmetic_mean(first, *args):
#     """This function calculates the arithmetic mean"""
#     for arith in args:
#         return first + sum(args) / (1 + len(args))
#
# print(arithmetic_mean(4, 40, 12, 25))
# print(arithmetic_mean.__doc__)

# -------------------------2----------------------
# def absolute_value(num):
#     if num > 0:
#         return num
#     else:
#         return abs(num)
#
# print(absolute_value(-10))

# -------------------------3-----------------------
# def maximum_number(num1, num2):
#     """This function determines maxim of two number"""
#     if num1 > num2:
#         print("The number {} is maximum, the number {} is minimum".format(num1, num2))
#     else:
#         print("The number {} is maximum, the number {} is minimum".format(num2, num1))
#
# print(maximum_number(59, 16))

# -------------------------4-----------------------
# def s_circle():
#     p = 3.14
#     radius = int(input("Enter radius of the circle: "))
#     S = p * radius ** 2
#     print("S of circle =", S)
#
# def s_triangle():
#     a = int(input("Enter side of the triangle: "))
#     h = int(input("Enter height of the triangle: "))
#     S = 0.5 * a * h
#     print("S of the circle =", S)
#
# def s_rectangle():
#     a = int(input("Enter first side of the rectangle: "))
#     b = int(input("Enter second side of the rectangle: "))
#     S = a * b
#     print("S of the rectangle =", S)
#
# print("1 = S circle\n"
#       "2 = S triangle\n"
#       "3 = S rectangle")
# user = int(input("Choice figure:"))
# if user == 1:
#     print(s_circle())
# elif user == 2:
#     print(s_triangle())
# elif user == 3:
#     print(s_rectangle())
# else:
#     print("Input Eror")

# -------------------------------5----------------------------
# def sum_of_number(number):
#     """This function counts sum of digits of the entered number"""
#     x = 0
#     for i in range(number + 1):
#         x += i
#     return x
#
# print(sum_of_number(5))
# print(sum_of_number.__doc__)

# -----------------------------6-------------------------------
"""This is a program with simple calculator """

print("The number 0 closes the program")

while True:
    x = float(input("Enter the first number, x=  "))
    symbl = input("Enter one of symbols (+, -, *, /): ")
    y = float(input("Enter the second number, y=  "))

    if symbl == "0":
        print("Thank you for choosing our product")
        break
    if symbl == "+":
        print("x + y =", x + y)
    elif symbl == "-":
        print("x - y =", x - y)
    elif symbl == "*":
        print("x * y =", x * y)
    elif symbl == "/":
        if x == 0 or y == 0:
            print("Division by zero!")
        else:
            print("x / y =", x / y)
    else:
        print("Input Error")
