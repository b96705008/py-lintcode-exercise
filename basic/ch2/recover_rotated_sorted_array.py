class Solution:
    """
    @param nums: An integer array
    @return: nothing
    """
    def swipe(self, nums, start, end):
        first = start
        last = end
        while first < last:
            nums[first], nums[last] = nums[last], nums[first]
            first = first + 1
            last = last - 1

        print(start, end, nums)

    def recoverRotatedSortedArray(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return []
        elif len(nums) == 1:
            return nums

        i = 0
        while i + 1 < len(nums):
            if nums[i] > nums[i+1]:
                break
            i += 1

        self.swipe(nums, 0, i)
        self.swipe(nums, i+1, len(nums)-1)
        self.swipe(nums, 0, len(nums)-1)


sol = Solution()

nums = [4, 5, 1, 2, 3]
sol.recoverRotatedSortedArray(nums)
print nums