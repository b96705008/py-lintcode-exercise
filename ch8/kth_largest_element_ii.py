"""
Description
Find K-th largest element in an array. 
and N is much larger than k.


Notice
You can swap elements in the array

Example
In array [9,3,2,4,8], the 3rd largest element is 4.

In array [1,2,3,4,5], the 1st largest element is 5, 
2nd largest element is 4, 3rd largest element is 3 and etc.

Reference
https://www.jianshu.com/p/885318cf9b25
"""
from Queue import PriorityQueue
import numpy as np

class Solution:
    """
     * @param nums an integer unsorted array
     * @param k an integer from 1 to n
     * @return the kth largest element
    """
    def kthLargestElement2(self, nums, k):
        if nums is None or len(nums) < k:
            return None

        min_heap = PriorityQueue(maxsize=k)

        for i, n in enumerate(nums):
            if i < k:
                min_heap.put(n)
            elif n > min_heap.queue[0]:
                min_heap.get()
                min_heap.put(n)

        return min_heap.get()


if __name__ == '__main__':
    sol = Solution()

    nums = [9,3,2,4,8]
    print sol.kthLargestElement2(nums, 3), 4
    print sol.kthLargestElement2(nums, 2), 8
    print sol.kthLargestElement2(nums, 1), 9

    nums = [1,2,3,4,5]
    print sol.kthLargestElement2(nums, 1), 5


