# https://leetcode.com/problems/reverse-integer/description/
# Given a 32-bit signed integer, reverse digits of an integer.

# (2 ** 31) - 1 # Max 32 bit integer

# [key : value]
# [input_num: reversed_num
# Will need to improve later to:
# 1. not convert to string
# 2. limit integer to 32 bit and return 0 if value exceeds range


x = str(x)
dictionary = {x: ''}


class Solution:
    def is_palindrome(x):
        for i in range(len(x) - 1, -1, -1):
            dictionary[x] += x[i]

        if dictionary[x] in dictionary and:
            return True
        else:
            return False


print(Solution.is_palindrome(x))
