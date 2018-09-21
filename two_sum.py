# https://leetcode.com/problems/reverse-integer/description/

# [key : value]
# [input_num: reversed_num
# Will need to improve later to:
# 1. not convert to string


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
