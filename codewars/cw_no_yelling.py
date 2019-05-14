# Write a function taking in a string
# like WOW this is REALLY amazing and
# returning Wow this is really amazing.
# String should be capitalized and properly spaced.
# Using re and string is not allowed.

def filter_words(st):
    change_st = ""
    for i in st:
        change_st += i.lower()
        change_st = change_st[0].upper() + change_st[1:]
    change_st = ' '.join(change_st.split())
    return change_st
