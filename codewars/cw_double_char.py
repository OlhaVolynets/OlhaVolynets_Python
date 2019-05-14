# Given a string, you have to return a string
# in which each character (case-sensitive) is repeated once.

def double_char(s):
    double_s = ""
    for i in s:
        double_s += i * 2
    return double_s