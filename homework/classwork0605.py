###################################1############################################
# num_list = int(input("Enter len list: "))
# numbers = [int(input("Enter int {}: ".format(i + 1))) for i in range(num_list)]
# print("Max number is: {}, min number is: {}".format(max(numbers), min(numbers)))


###################################2############################################
# for i in range (1, 11):
#     if i % 2 == 0:
#         print("The number {} is divided on 2".format(i))
#     elif i % 3 == 0:
#         print("The number {} is divided on 3".format(i))
#     else:
#         print("The number {} is not divided on 2 and 3".format(i))


##################################3##########################################
# number_factorial = int(input("Enter a number: "))
# factorial = 1
# if number_factorial < 0:
#     print("Error. This number does not factorial")
# elif number_factorial == 0:
#        print("Factorial of number 0 is 1")
# else:
#     for i in range(1, number_factorial + 1):
#         factorial *= i
#         print("Factorial of number {1} is {0}". format(factorial, i))

###################################4#####################################
# login = "First"
# user_login = input("Enter your login: ")
# while user_login != login:
#     user_login = input("Enter correct login again: ")
# else:
#     print("Hello,", user_login)

##################################5#######################################
# input_number = 1
# while input_number > 0:
#     input_number = int(input("Enter number: "))

#################################6#######################################
# num_list = int(input("Enter len list: "))
# for i in range(num_list):
#     number = int(input("Enter int: "))
#     if number <= 0:
#         print("This program is ended. Entered number is {}".format(number))
#         break
# else:
#     print("All numbers are positive")

##################################7##########################################
# for i in range(10, 31):
#     if i % 2 == 0:
#         n = i // 2
#         print(" {} equals is 2 * {}".format(i, n))
#     elif i % 3 == 0:
#         n = i // 3
#         print(" {} equals is 3 * {}".format(i, n))
#     else:
#         print("The number {} is prime".format(i))

##################################8##########################################
my_text = "There is a most beautiful city in our country"
# sorted_text = my_text.split()
# sorted_text.sort(key=len)
# print(" ".join(sorted_text))
print(" ".join(sorted(my_text.split(), key = len)))

