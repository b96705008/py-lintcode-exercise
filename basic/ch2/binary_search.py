class Solution:
    """
    @param: nums: An integer array sorted in ascending order
    @param: target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):
        # write your code here
        if nums is None or len(nums) == 0:
            return -1
        
        def helper(nums, start, end, target):
            if start + 1 < end:
                mid = start + (end - start) / 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    return helper(nums, mid+1, end, target)
                elif nums[mid] > target:
                    return helper(nums, start, mid-1, target)
                    
            if nums[start] == target:
                return start
            elif nums[end] == target:
                return end
            else:
                return -1
        
        return helper(nums, 0, len(nums)-1, target)