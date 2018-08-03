"""
Description
Find the kth smallest numbers in an unsorted integer array.


Example
Given [3, 4, 1, 2, 5], k = 3, 
the 3rd smallest numbers are [1, 2, 3].


Challenge 
An O(nlogn) algorithm is acceptable, 
if you can do it in O(n), that would be great.
"""

class Solution:
    """
     * @param k an integer
     * @param nums an integer array
     * @return kth smallest element
    """
    def kthSmallest(self, k, nums):
        if nums is None or len(nums) < k:
            return -1

        return self.quick_select(nums, 0, len(nums)-1, k)

    def quick_select(self, nums, start, end, k):
        if start == end:
            return nums[start]

        i = start
        j = end
        mid = (start + end) / 2
        pivot = nums[mid]
        while i <= j:
            while i <= j and nums[i] < pivot:
                i = i + 1

            while i <= j and nums[j] > pivot:
                j = j - 1

            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i = i + 1
                j = j - 1

        if k - 1 <= j:
            return self.quick_select(nums, start, j, k)
        elif k - 1 >= i:
            return self.quick_select(nums, i, end, k)

        # if start + k - 1 <= j:
        #     return self.quick_select(nums, start, j, k)
        # elif start + k - 1 >= i:
        #     return self.quick_select(nums, i, end, k-(i-start))

        return nums[j+1]


if __name__ == '__main__':
    sol = Solution()

    print sol.kthSmallest(3, [3,4,1,2,5])
    print sol.kthSmallest(1, [3,4,1,2,5])
    print sol.kthSmallest(1, [9,3,2,4,8])
    print sol.kthSmallest(5, [9,3,2,4,8])
    