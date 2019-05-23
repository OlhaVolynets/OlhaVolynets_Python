# -------------1------------------------------------------------
# Напишіть програму, яка пропонує користувачу ввести ціле число
# і визначає чи це число парне чи непарне, чи введені дані коректні.


# try:
#     enter = int(input("Enter integer number: "))
#     if enter <= 0:
#         raise ValueError("This is not positive number")
#     if enter % 2 == 0:
#         print("This number is paired number")
#     else:
#         print("This number is not paired number")
#
# except ValueError:
#     print("This number is not corect")
# else:
#     print("No exception")

# ----------2-----------------------------------------------------------
# Напишіть програму, яка пропонує користувачу ввести свій вік, після чого виводить повідомлення про те чи вік є парним чи непарним числом.
# Необхідно передбачити можливість введення від’ємного числа, в цьому випадку згенерувати власну виняткову ситуацію.
# Головний код має викликати функцію, яка обробляє введену інформацію.

# age = input("Enter your age: ")
# while type(age) != int:
#     try:
#         age = int(age)
#         if age <= 0:
#             raise ValueError("Your age can not be negative")
#     except ValueError:
#         print("\nYou entered incorrect number")
#         age = input("Enter number:\n ")
#
# if age % 2 == 0:
#     print("The number {} is even".format(age))
# else:
#     print("The number is odd".format(age))

# ---------------------3-----------------------------------------------
# Напишіть програму для обчислення частки двох чисел, які вводяться користувачем послідовно через кому,
# передбачити випадок ділення на нуль,
# випадки синтаксичних помилок та випадки інших виняткових ситуацій. Використати блоки else та finaly.

# try:
#     entered = input("Enter two numbers separated by comma: ").replace(",", "")
#     num_1 = int(entered[0])
#     num_2 = int(entered[1])
#     fraction_of_division = num_1 / num_2
# except ZeroDivisionError:
#     print("Division to zero")
# except ValueError:
#     print("You are writing with a mistake")
# else:
#     print("Fraction of division is {}".format(fraction_of_division))
# finally:
#     print("Executing finally clause")


# -------------------4----------------------------------------------------------------
# Написати  програму, яка аналізує введене число та в залежності від числа видає день тижня, який відповідає цьому числу
# (1 це Понеділок, 2 це Вівторок і т.д.) .
# Врахувати випадки введення чисел від 8 і більше, а також випадки введення не числових даних.

# class DaysError(Exception):
#     def __init__(self, data):
#         self.data = data
#     def __str__(self):
#         return repr(self.data)
#
# number_of_day = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
#
# while True:
#     try:
#         entered = int(input("Enter one number from 1 to 7:\n "))
#         if entered <= 0 or entered >= 8:
#             raise DaysError("Please, enter a integer number 1-7:\n")
#         else:
#             print(number_of_day.get(entered))
#     except DaysError as d:
#         print("Incorrect entered.", d.data)
#     else:
#         break
