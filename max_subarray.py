# https://leetcode.com/problems/maximum-subarray/
# https://en.wikipedia.org/wiki/Maximum_subarray_problem


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


current_max_so_far = current_max = nums[0]

for i in nums[1:]:
    current_max = max(i, current_max + i)
    current_max_so_far = max(current_max_so_far, current_max)

print(current_max_so_far)
