# print("==================1a====================")
# number = 0
# while number < 100:
#     print(number, end=" ")
#     number += 2

# print("==================1b====================")
# for i in range(0, 100, 2) :
#     print(i, end=" ")

# print("==================2====================")
# number = 1
# while number < 100:
#     print(number, end=" ")
#     number += 2

# print("====================2b======================")
# for i in range(1, 100, 2):
#     if i % 2 == 0:
#         continue
#     print(i, end=" ")
#
# print("====================3=====================")
# contain_odd = False
# for i in range(0, 100):
#     if not i % 2 == 0:
#         contain_odd = True
#         break
# if contain_odd:
#     print("There is odd numbers in the list")
# else:
#     print("There is even numbers in the list")

# print("=====================4=====================")
# numbers_int = [10, 32, 13, 40]
# numbers_float = []
# for i in numbers_int:
#     numbers_float.append(float(i))
# print(numbers_float)

# print("=======================5=====================")
# number_fibonachi = int(input("Enter your number: "))
# a = 0
# b = 1
# while b <= number_fibonachi:
#     b = a + b
#     a, b = b, a
#     print(b)

# print("=========================6======================")
# my_string = ("child", "young", "old")
# for i in my_string:
#     print(i)

print("=========================7======================")
my_string = ("child", "young", "old")
s = str(input("Enter special symbol: "))
for i in my_string:
    print(i, end="%s " % s)

