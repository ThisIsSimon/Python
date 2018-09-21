# https://leetcode.com/problems/reverse-integer/description/
# Given a 32-bit signed integer, reverse digits of an integer.
# -123 is -321
# 120 is 21

# first draft - while it accomplishes the goal, it needs a lot of simplification

x = -123


class Solution:
    def reverse(x):
        dictionary = {str(abs(x)) : ''}
        x_str = str(abs(x))

        for i in range(len(x_str) -1, -1, -1):
            dictionary[x_str] += x_str[i]

        pos_neg = 0 if x == 0 else int((x/(abs(x))))
        if abs(int(dictionary[x_str])) >= ((2**31) - 1):
            return 0
        else:
            return int(dictionary[x_str]) * pos_neg

print(Solution.reverse(x))
