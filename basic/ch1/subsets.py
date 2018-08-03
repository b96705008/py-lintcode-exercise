
def subsets(nums):
    result_sets = []

    if nums is None:
        return result_sets
    
    nums = sorted(nums)

    def find_subsets(root, nums, results):
        # add root set
        results.append(root[:])

        # Deep Traverse 
        for i, n in enumerate(nums):
            # prevent duplicate traverse
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # recursive to next level
            find_subsets(
                root + [n], 
                nums[i+1:], 
                results)

    find_subsets([], nums, result_sets)

    return result_sets

def show_subsets(nums):
    print 'nums:', nums
    results = subsets(nums)
    for r in results:
        print r

show_subsets([])
show_subsets([1, 2, 3])
show_subsets([4, 1, 2])
show_subsets([1, 2, 2])
show_subsets([1, 1])

# def try(nums):
#     print nums, ":"
#     results = subsets([nums])
#     for r in results:
#         print r

# try([1,2,3])
    