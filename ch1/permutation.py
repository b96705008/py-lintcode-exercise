
def permutation(nums):
    results = []

    if nums is None:
        return results

    sorted_nums = sorted(nums)

    def helper(root_set, nums, result_sets):
        if len(nums) == 0:
            result_sets.append(root_set[:])
    
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue

            helper(
                root_set + [n],
                nums[:i] + nums[i+1:],
                result_sets)

    helper([], sorted_nums, results)
    return results

print permutation([1, 2, 2])
print permutation([1, 1, 1])
print permutation([1, 2, 3])
print permutation([3, 3, 0, 3])