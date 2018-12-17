# https://leetcode.com/problems/implement-strstr/

haystack = "aaaaa"
needle = "bba"


class Solution:
    def strStr(haystack, needle):

        if len(needle) == 0:
            return 0

        string = ""
        for char in range(len(haystack)):
            string += haystack[char]
            if needle in string:
                return char - (len(needle) - 1)
        else:
            return -1


print(Solution.strStr(haystack, needle))
