'''
https://monkeysayhi.github.io/2017/08/04/%E3%80%90%E5%88%B7%E9%A2%98%E3%80%91Search-in-a-Big-Sorted-Array/

Given a big sorted array with positive integers sorted by ascending order. 
The array is so big so that you can not get the length of the whole array directly, 
and you can only access the kth number by ArrayReader.get(k) 
(or ArrayReader->get(k) for C++). 
Find the first index of a target number. 
Your algorithm should be in O(log k), 
where k is the first index of the target number.
'''

import numpy

def search_big_array(nums, target):
    # write your code
    EOF = 2147483647

    if nums is None:
        return -1

    def query(nums, index):
        try:
            return nums[index]
        except:
            return EOF

    def get_range(nums, target):
        end = 1
        while query(nums, end) < target:
            end = end << 1

        start = end >> 1
        while end > start and query(nums, end) == EOF:
            end = end - 1

        if query(nums, end) == EOF or end < start:
            return None, None

        return start, end

    start, end = get_range(nums, target)
    if start is None or end is None:
        return -1

    def helper(nums, start, end, target):
        if start + 1 < end:
            mid = start + (end - start) / 2
            if query(nums, mid) == target:
                return helper(nums, start, mid, target)
            if query(nums, mid) < target:
                return helper(nums, mid+1, end, target)
            if query(nums, mid) > target:
                return helper(nums, start, mid-1, target)

        if query(nums, start) == target:
            return start
        elif query(nums, end) == target:
            return end
        
        return -1

    return helper(nums, start, end, target)

big_arr = [1, 2, 3, 4, 6, 7] + ([10] * 100)
ans = search_big_array(big_arr, 6)
print ans, ans==4

big_arr = [1, 2, 3, 4] + [7]*100 + [10]*100
ans = search_big_array(big_arr, 7)
print ans, ans==4

big_arr = ([2]*1000) + ([10]*100) + ([20]*400)
ans = search_big_array(big_arr, 20)
print ans, ans==1100

