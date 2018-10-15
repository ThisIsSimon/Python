# https://leetcode.com/problems/remove-element/description/


# Original solution I can up with

class Solution:
    def removeElement(nums, val):
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                del nums[i]
        return len(nums)


# A "pythonic" solution


class Solution:
    def removeElement(nums, val):
        while True:
            if val in nums:
                nums.remove(val)
            else:
                return (len(nums))


nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
print(Solution.removeElement(nums, val))
