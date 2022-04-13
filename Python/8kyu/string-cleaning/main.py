# https://www.codewars.com/kata/57e1e61ba396b3727c000251

# Solution
def string_clean(s):
    for number in range(10):
        s = s.replace(str(number), '')
    return s