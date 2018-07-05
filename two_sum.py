'''
https://leetcode.com/problems/two-sum/description/

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

def two_sum(list, target):
    for x in range(len(list)):
        for y in range(x + 1, len(list)):
            if  list[x] + list[y] == target:
                return[list.index(list[x]), list.index(list[y])]
            else:
                continue

nums = [2, 7, 11, 15]
target = 9

print(two_sum(nums, target))

