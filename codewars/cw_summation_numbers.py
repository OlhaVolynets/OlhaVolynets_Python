# Write a program that finds the summation
# of every number from 1 to num.
# The number will always be a positive integer greater than 0.

def summation(num):
    numbers = []
    for i in range(1, num + 1):
        numbers.append(i)
    return sum(numbers)
