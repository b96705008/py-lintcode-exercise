def sort_integers(nums):
	quick_sort(nums, 0, len(nums)-1)


def quick_sort(nums, start, end):
	if start >= end:
		return

	mid = (start + end) / 2
	pivot = nums[mid]
	left = start
	right = end

	while left <= right:
		while left <= right and nums[left] < pivot:
			left = left + 1

		while left <= right and nums[right] > pivot:
			right = right - 1

		if left <= right:
			nums[left], nums[right] = nums[right], nums[left]
			left = left + 1
			right = right - 1

	quick_sort(nums, start, right)
	quick_sort(nums, left, end)

nums = [5,1,3,7,2,4,8,6]
sort_integers(nums)
print nums


nums = [4,4,6,2,1,3,3]
sort_integers(nums)
print nums

