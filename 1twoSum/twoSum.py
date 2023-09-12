# Two Sum Leetcode 1 (Hashmap): Facebook interview question
# return indices of the 2 numbers such that they add up to a specific target
# each input would have exactly one solution and you may not use the same element twice
# ex: 2, 1, 5, 3 target = 4, 1+3 = 4
# 2, 7, 11, 9 target = 9 2+7 = 9
# use hashmap - 4-2=2 2 is not in val of hashmap(append2), 4-1=3 is not in val of hashmap(append1), 4-5=-1 is not in val of hashmap(append5), 4-3=1 is in hashmap so it would choose the value to add to get the target value
# usually can solve it in some other way like using two loop would go to O(n^2)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevMap = {} # index
        # nums.rfind(3)
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[n] = i
        return []

print(Solution().twoSum([2, 1, 5, 3], 4))
print(Solution().twoSum([2, 7, 11, 9], 9))
print(Solution().twoSum([3, 5, -4, 8, 11, 1, -1, 6], 10))
print(Solution().twoSum([15], 15))

# super solution