# https://leetcode.com/problems/valid-parentheses/description/

# NOTES
# I think there are two possible scenarios that determine if they're enclosed properly
# The provided true examples are:

# Input: "()"
# Output: true

# Input: "()[]{}"
# Output: true

# Input: "{[]}"
# Output: true

# Which means they're either enclosed by being next to each other
# i.e:
# i, i + 1
# (, )
# [, ]
# OR
# If I split them in half, the other must reflect the other half properly
# i.e:
# ([])
# I take ([
# and if the other side is ]) then it is valid


class Solution:
    def isvalid(s):
        # tests if i + 1 is the closing bracket of i
        dictionary = {'(': ')', '[': ']', '{': '}'}
        for i in range(0, len(s), 2):
            if s[i + 1] != dictionary[s[i]]:
                return False
                break
        else:
            return True

        # split the string in half, and see if the last half of the string is equal to the dictionary's
        # output using the first half of the string
        j = 0
        dictionary = {'(': ')', '[': ']', '{': '}'}
        for i in range(len(s) - 1, int(len(s) / 2) - 1, -1):
            if dictionary[s[j]] != s[i]:
                return False
                break
            j += 1
        else:
            return True



string = '()[]{}'
string1 = '{[()]}'

print(Solution.isvalid(string))
