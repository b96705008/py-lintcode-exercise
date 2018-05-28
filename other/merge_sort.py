

def sort_integers(nums):
    tmp = [None] * len(nums)
    merge_sort(nums, 0, len(nums)-1, tmp)


def merge(nums, start, end, tmp):
    left = start
    left_end = (start + end) / 2
    right = left_end + 1
    right_end = end
    index = start

    while left <= left_end and right <= right_end:
        if nums[left] < nums[right]:
            tmp[index] = nums[left]
            left = left + 1
        else:
            tmp[index] = nums[right]
            right = right + 1
        index = index + 1

    while left <= left_end:
        tmp[index] = nums[left]
        left = left + 1
        index = index + 1

    while right <= right_end:
        tmp[index] = nums[right]
        right = right + 1
        index = index + 1

    i = start
    while i <= end:
        nums[i] = tmp[i]
        i = i + 1


def merge_sort(nums, start, end, tmp):
    if start >= end:
        return

    print start, end

    mid = (start + end) / 2
    merge_sort(nums, start, mid, tmp)
    merge_sort(nums, mid+1, end, tmp)
    merge(nums, start, end, tmp)

nums = [5,1,3,7,2,4,8,6]
sort_integers(nums)
print nums

