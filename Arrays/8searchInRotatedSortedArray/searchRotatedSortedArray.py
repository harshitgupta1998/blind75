class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            
            # Case 1: find target
            if nums[mid] == target:
                return mid
            
            # Case 2: subarray on mid's left is sorted
            elif nums[mid] >= nums[left]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
                    
            # Case 3: subarray on mid's right is sorted.
            else:
                if target <= nums[right] and target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
        

print(Solution().search([4,5,6,7,0,1,2], 0))
print(Solution().search([4,5,6,7,0,1,2], 3))
print(Solution().search([4,5,6,7,0,1,2], 5))
print(Solution().search([4,5,6,7,0,1,2], 4))
print(Solution().search([2], 3))

# solved but need to optimize
"""
l = 0
r = len(nums) - 1
while l <= r:
    mid = (l+r) // 2
    if nums[mid] == target:
        return mid
    # left sorted portion
    if nums[mid] >= nums[l]:
        if target > nums[mid] or target < nums[l]:
            l = mid + 1
    
        else:
            r = mid - 1
            
    else:
        if target < nums[mid] or target > nums[r]:
            r = mid - 1
        else:
            l = mid + 1
"""
def mini(nums):
    l = 0
    r = len(nums) - 1
    # mid = (l + r) // 2
    minimum = nums[0]
    while l <= r:
        mid = (l+r) // 2
        if nums[mid] < minimum:
            minimum = nums[mid]
        # if nums[mid] == target:
        #     return mid
        # # left sorted portion
        if nums[mid] > nums[l]:
            # if minimum < nums[mid] or minimum < nums[l]:
            if nums[l] < minimum:
                minimum = nums[l]
            l = mid + 1
            
        
            # else:
                # r = mid - 1
                
        else:
            # if minimum < nums[mid] or minimum < nums[r]:
            if nums[r] < minimum:
                minimum = nums[r]
            r = mid - 1
            
            # else:
            #     l = mid + 1
                
    return minimum
                
                
print(mini([11,13,15,17]))
print(mini([4,5,6,7,0,1,2]))
print(mini([3,4,5,1,2]))
print(mini([2,1]))
print(mini([2,3,4,5,1]))