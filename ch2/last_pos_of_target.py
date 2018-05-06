class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def binarySearch(self, nums, target):
        # write your code here
        if nums is None or len(nums) == 0:
            return -1
        
        def helper(nums, start, end, target):
                    
            if start + 1 < end:
                mid = start + (end - start) / 2
                if nums[mid] == target:
                    return helper(nums, mid, end, target)
                elif nums[mid] > target:
                    return helper(nums, start, mid-1, target)
                elif nums[mid] < target:
                    return helper(nums, mid+1, end, target)
            
            if nums[end] == target:
                return end
            elif nums[start] == target:
                return start
            else:
                return -1
        
        return helper(nums, 0, len(nums)-1, target)

sol = Solution()

ans = sol.binarySearch([1, 2, 3, 8, 8, 8, 8, 9], 1)
print ans, ans==0

ans = sol.binarySearch([1, 2, 3, 8, 8, 8, 8, 9], 9)
print ans, ans==7

ans = sol.binarySearch([1, 2, 3, 3, 8, 8, 8, 9, 10], 3)
print ans, ans==3

ans = sol.binarySearch([1, 2, 3, 8, 8, 8, 8, 9], 8)
print ans, ans==6



