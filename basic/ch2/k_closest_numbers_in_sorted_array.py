"""
Given a sorted array, two integers k and x, 
find the k closest elements to x in the array. 
The result should also be sorted in ascending order. 
If there is a tie, the smaller elements are always preferred.

ex1:
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]

ex2:
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]

Note:
The value k is positive and will always be smaller than the length of the sorted array.
Length of the given array is positive and will not exceed 104
Absolute value of elements in the array and x will not exceed 104
"""

# O(log(n)+k)
def find_k_nums(nums, k, x):
	result = []

	# 0. base check
	if nums is None or len(nums) == 0:
		return result

	if x <= nums[0]:
		return nums[:k]

	if x >= nums[len(nums)-1]:
		return nums[-k:]

	# 1. narrow the scope
	start = 0
	end = len(nums) - 1
	while start + 1 < end:
		mid = start + (end - start) / 2
		if nums[mid] < x:
			start = mid
		else:
			end = mid

	# 2. find real scope
	pivot = -1
	if nums[start] == x:
		pivot = start
	else:
		pivot = end

	first = max(0, pivot-(k-1))
	last = min(len(nums)-1, pivot+(k+1))
	while last - first + 1 > k:
		if nums[last] - x >= x - nums[first]:
			last = last - 1
		else:
			first = first + 1

	return nums[first:last+1]


def testing(nums, k, x):
	sol = find_k_nums(nums, k, x)
	print sol


testing([1,2,3,4,5], 4, 3)
testing([1,2,3,4,5], 4, -1)
testing([1,2,3,4,5], 3, 6)
testing([1,2,2,2,4,5], 3, 2)
testing([1,2,2,2,4,5], 2, 3)






