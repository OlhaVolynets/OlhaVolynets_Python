# Given an array of integers.
# Return an array, where
# the first element is the count of positives numbers and
# the second element is sum of negative numbers.
# If the input array is empty or null, return an empty array

def count_positives_sum_negatives(arr):
    count_positives = len([i for i in arr if i > 0])
    sum_negatives = sum([i for i in arr if i < 0])
    if not arr:
        return []
    return [count_positives, sum_negatives]

# def count_positives_sum_negatives(arr):
#     count_positives = 0
#     sum_negatives = 0
#     for i in arr:
#         if i > 0:
#             count_positives += 1
#         elif i < 0:
#             sum_negatives += i
#         else:
#             return []
#     return [count_positives, sum_negatives]