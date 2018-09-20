# https://leetcode.com/problems/two-sum/description/
# Example from site:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


class Solution:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def twoSum(self):
        dictionary = {}
        for i in range(len(self.nums)):
            dictionary[self.nums[i]] = self.nums.index(self.nums[i])
            if (self.target - self.nums[i]) in dictionary:
                return [dictionary[self.target - self.nums[i]], i]
                break
        else:
            return 'Target not found'


nums = [2, 7, 11, 15]
target = 9
print(Solution(nums, target).twoSum())

'''
class Solution:
    def twoSum(self, nums, target):
        dictionary = {}
        for i in range(len(nums)):
            dictionary[nums[i]] = nums.index(nums[i])
            if (target - nums[i]) in dictionary and dictionary[target - nums[i]] != i:
                return [dictionary[target - nums[i]], i]
                break
        else:
            return 'Target not found'
            
# accepted answer on the website
# you do not need to do __init__ 
'''
