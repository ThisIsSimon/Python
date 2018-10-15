# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
# NOTES
# list.remove removes first matching value
# list.del removes item at a specific index
# restrictions are "in-place" algorithm, I must edit the existing array
# and cannot use extra memory


class Solution:
    def removeDuplicates(nums):
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] == nums[i - 1]:
                del nums[i]
        return len(nums)


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

print(Solution.removeDuplicates(nums))

# Performance is not very good, as I have to check every single value
# Need to re-evaluate
