'''
Reference:
http://blog.leanote.com/post/westcode/c0469ec79225

Given a mountain sequence of n integers which increase firstly and then decrease, 
find the mountain top.

Example: 
Given nums = [1, 2, 4, 8, 6, 3] return 8 
Given nums = [10, 9, 8, 7], return 10
'''

def find_max_in_mountain(nums):
	if nums is None or len(nums) == 0:
		return None

	# == Recursive ==
	def helper(nums, start, end):
		if start + 1 < end:
			mid = start + (end - start) / 2
			if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
				# peak
				return nums[mid]
			elif nums[mid-1] > nums[mid+1]:
				# decreasing
				return helper(nums, start, mid-1)
			elif nums[mid-1] < nums[mid+1]:
				# increasing
				return helper(nums, mid+1, end)
			elif nums[mid-1] == nums[mid+1]:
				return max(helper(nums, start, mid-1),
						   helper(nums, mid+1, end))

		return max(nums[start], nums[end])

	return helper(nums, 0, len(nums)-1)


def testing(nums, ans):
	sol = find_max_in_mountain(nums)
	print sol, sol==ans

testing([1, 2, 4, 8, 6, 3], 8)
testing([10, 9, 8, 7], 10)
testing([1, 2, 4], 4)
testing([1], 1)
testing([], None)