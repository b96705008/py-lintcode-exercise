"""
Given a target number and an integer array sorted in ascending order. 
Find the total number of occurrences of target in the array.

Example 
Given [1, 3, 3, 4, 5] and target = 3, return 2.

Given [2, 2, 3, 4, 6] and target = 4, return 1.

Given [1, 2, 3, 4, 5] and target = 6, return 0.
"""

def count_target(nums, target):
	cnt = 0
	if nums is None or len(nums) == 0:
		return cnt

	# == Recursive ==
	# def helper(nums, start, end, target, cnt):
	# 	if start + 1 < end:
	# 		mid = start + (end - start) / 2
	# 		if nums[mid] == target:
	# 			new_cnt = cnt + 1 + \
	# 				helper(nums, start, mid-1, target, 0) + \
	# 				helper(nums, mid+1, end, target, 0)
	# 			return new_cnt
	# 		elif nums[mid] > target:
	# 			return helper(nums, start, mid-1, target, cnt)
	# 		elif nums[mid] < target:
	# 			return helper(nums, mid+1, end, target, cnt)

	# 	if nums[start] == target:
	# 		cnt = cnt + 1

	# 	if start != end and nums[end] == target:
	# 		cnt = cnt + 1

	# 	return cnt

	# return helper(nums, 0, len(nums)-1, target, 0)

	# == Loop ==
	first_pos = -1
	last_pos = -1

	# 1. find first position
	start = 0
	end = len(nums) - 1
	while start + 1 < end:
		mid = start + (end - start) / 2
		if nums[mid] < target:
			start = mid
		else:
			end = mid

	if nums[start] == target:
		first_pos = start
	elif nums[end] == target:
		first_pos = end

	if first_pos == -1:
		return 0

	# 2. find last position:
	start = 0
	end = len(nums) - 1
	while start + 1 < end:
		mid = start + (end - start) / 2
		if nums[mid] > target:
			end = mid
		else:
			start = mid

	if nums[end] == target:
		last_pos = end
	elif nums[start] == target:
		last_pos = start

	return last_pos - first_pos + 1


def testing(nums, target, ans):
	sol = count_target(nums, target)
	print sol, sol==ans


testing([1, 3, 3, 4, 5], 3, 2)
testing([2, 2, 3, 4, 6], 4, 1)
testing([1, 2, 3, 4, 5], 6, 0)
testing([2, 2, 2], 2, 3)
testing([1], 1, 1)
testing([1, 2, 3, 4, 4, 4], 4, 3)


