'''
Reference:
https://yeqiuquan.blogspot.tw/2017/03/lintcode-459-closest-number-in-sorted.html

Description:
Given a target number and an integer array A sorted in ascending order, 
find the index i in A such that A[i] is closest to the given target.

Return -1 if there is no element in the array.

Notice:
There can be duplicate elements in the array, 
and we can return any of the indices with same value.

Example:
Given [1, 2, 3] and target = 2, return 1.
Given [1, 4, 6] and target = 3, return 1.
Given [1, 4, 6] and target = 5, return 1 or 2.
Given [1, 3, 3, 4] and target = 2, return 0 or 1 or 2.
'''

def find_closet_num(A, target):
	if A is None or len(A) == 0:
		return -1

	start = 0
	end = len(A) - 1
	if target <= A[start]:
		return start
	if target >= A[end]:
		return end

	# == Recursive ==
	# def helper(nums, start, end, target):
	# 	if start + 1 < end:
	# 		mid = start + (end - start) / 2
	# 		if target == nums[mid]:
	# 			return mid
	# 		elif target < nums[mid]:
	# 			return helper(nums, start, mid, target)
	# 		elif target > nums[mid]:
	# 			return helper(nums, mid, end, target)

	# 	if target - nums[start] < nums[end] - target:
	# 		return start
	# 	else:
	# 		return end

	# return helper(A, start, end, target)

	# == For Loop ==
	while start + 1 < end:
		mid = start + (end - start) / 2
		if target == A[mid]:
			return mid
		elif target < A[mid]:
			end = mid
		else:
			start = mid

	if target - A[start] < A[end] - target:
		return start
	else:
		return end


def testing(nums, target, ans):
	sol = find_closet_num(nums, target)
	print sol, sol in ans

testing([1, 2, 3], 2, [1])
testing([1, 4, 6], 3, [1])
testing([1, 4, 6], 5, [1, 2])
testing([1, 3, 3, 4], 2, [0, 1, 2])
testing([1, 4, 4, 6], 0, [0])
testing([1, 4, 4, 6], 7, [3])

