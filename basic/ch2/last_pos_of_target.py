def binarySearch(nums, target):
    # write your code here
    if nums is None or len(nums) == 0:
        return -1
    
    # == Recursive ==
    # def helper(nums, start, end, target):
                
    #     if start + 1 < end:
    #         mid = start + (end - start) / 2
    #         if nums[mid] == target:
    #             return helper(nums, mid, end, target)
    #         elif nums[mid] > target:
    #             return helper(nums, start, mid-1, target)
    #         elif nums[mid] < target:
    #             return helper(nums, mid+1, end, target)
        
    #     if nums[end] == target:
    #         return end
    #     elif nums[start] == target:
    #         return start
    #     else:
    #         return -1
    
    # return helper(nums, 0, len(nums)-1, target)

    # == For Loop ==
    start = 0
    end = len(nums) - 1
    while start + 1 < end:
        mid = start + (end - start) / 2
        if nums[mid] == target:
            start = mid
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid -1

    if nums[end] == target:
        return end

    if nums[start] == target:
        return start

    return -1


ans = binarySearch([1, 2, 3, 8, 8, 8, 8, 9], 1)
print ans, ans==0

ans = binarySearch([1, 2, 3, 8, 8, 8, 8, 9], 9)
print ans, ans==7

ans = binarySearch([1, 2, 3, 3, 8, 8, 8, 9, 10], 3)
print ans, ans==3

ans = binarySearch([1, 2, 3, 8, 8, 8, 8, 9], 8)
print ans, ans==6



