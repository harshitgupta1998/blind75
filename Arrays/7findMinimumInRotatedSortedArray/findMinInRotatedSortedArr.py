# leetcode 153
# unique elements  return min and return solve it in O(log n)
# can able to use sliding window to search pair of decaresing value where it decreases we can find the minimum value
class Solution:
    def findMin(self, nums: list[int]) -> int:
        pre = 1
        post = 1
        r = len(nums) - 1
        l = 0
        res = nums[0]
        while r > -1 and l < len(nums):
            if pre == 0:
                pre = 1
            if post == 0:
                post = 1
            pre *= nums[l]
            l += 1
            post *= nums[r]
            r -= 1
            res = max(pre, post, res)
        return res
