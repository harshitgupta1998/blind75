# leetcode 153 find minimum in rotated sorted array facebook medium
# unique elements  return min and return solve it in O(log n)
# can able to use sliding window to search pair of decaresing value where it decreases we can find the minimum value
class Solution:
    def findMin(self, nums: list[int]) -> int:
        res = nums[0]
        
        l, r = 0, len(nums) - 1
        
        while l <= r:
            if nums[l] < nums[r]:
                res = min(nums[l], res)
            mid = (l + r) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        
        return res