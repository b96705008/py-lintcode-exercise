"""
Description
Given an array of integers, 
find how many unique pairs in the array such that their sum is equal to a specific target number. 
Please return the number of pairs.

Example
Given nums = [1,1,2,45,46,46], target = 47
return 2

1 + 46 = 47
2 + 45 = 47
"""

class Solution:
    """
    * @param nums an array of integer
    * @param target an integer
    * @return an integer
    """
    def two_sum_unique_pairs(self, nums, target):
        unique_pairs = 0
        if nums is None or len(nums) == 0:
            return unique_pairs

        nums.sort()
        index1 = 0
        index2 = len(nums)-1
        while index1 < index2:
            cur_sum = nums[index1] + nums[index2]
            if cur_sum == target:
                print nums[index1], nums[index2]
                unique_pairs = unique_pairs + 1
                index1 = index1 + 1
                index2 = index2 - 1

                # Skip same pairs
                while index1 < index2 and nums[index1] == nums[index1-1]:
                    index1 = index1 + 1

                while index1 < index2 and nums[index2] == nums[index2+1]:
                    index2 = index2 - 1

            elif cur_sum < target:
                index1 = index1 + 1
            else:
                index2 = index2 - 1

        return unique_pairs


if __name__ == '__main__':
    sol = Solution()

    print 'target: 47'
    print sol.two_sum_unique_pairs([1,1,2,45,46,46], 47)

    print 'target: 12'
    print sol.two_sum_unique_pairs([2,3,3,5,7,9,9,10], 12)

    print 'target: 2'
    print sol.two_sum_unique_pairs([1,1,1,1,1], 2)

    print 'target: 4'
    print sol.two_sum_unique_pairs([1,2,2,3], 4)

    print 'target: 4'
    print sol.two_sum_unique_pairs([3,2,1,2], 4)
                


