print("======================a============================")
user = str(input("Enter your four-digit number: "))
count = 1
for i in user:
    count *= int(i)
print(count)

print("=========================b==========================")
number_reverse = " ".join(user[::-1])
print(number_reverse)

print("==========================c==========================")
number_sort = sorted(user)
print(number_sort)