"""
Description
Implement next permutation, which rearranges numbers 
into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, 
it must rearrange it as the lowest possible order 
(ie, sorted in ascending order).

Example
Here are some examples. Inputs are in the left-hand column 
and its corresponding outputs are in the right-hand column.

1,2,3 -> 1,3,2

3,2,1 -> 1,2,3

1,1,5 -> 1,5,1

Challenge
The replacement must be in-place, do not allocate extra memory.
"""

class Solution:
    """
    @param nums: An array of integers
    @return: nothing
    """
    def nextPermutation(self, nums):
        # write your code here
        if nums is None:
            return None

        found = {
            'nums': False,
            'next': False
        }
        seq = sorted(nums)

        self.dfs_replace(nums, seq, 0, found, True)

        if not found['next']:
            nums.sort()

    def dfs_replace(self, nums, seq, start_index, found, is_nums):
        num_len = len(nums)

        if start_index == num_len:
            if not found['nums'] and is_nums:
                found['nums'] = True
            elif found['nums'] and not found['next']:
                found['next'] = True
            return
        
        for i in range(start_index, num_len):
            if i > start_index and seq[i] == seq[i-1]:
                continue

            # next step
            self.replace_in_place(seq, start_index, i)
            if self.should_repeat(found):
                self.replace_in_place(nums, start_index, i)

            # dfs find
            if not found['nums']:
                next_is_nums = is_nums and seq[start_index] == nums[start_index]
                if next_is_nums:
                    self.dfs_replace(nums, seq, start_index+1, found, next_is_nums)
            elif not found['next']:
                self.dfs_replace(nums, seq, start_index+1, found, False)

            # backtrack
            self.replace_in_place(seq, i, start_index)
            if self.should_repeat(found):
                self.replace_in_place(nums, i, start_index)

            if found['next']:
                break

    def replace_in_place(self, n, i, j):
        if i != j:
            n.insert(i, n.pop(j))

    def should_repeat(self, found):
        return found['nums'] and not found['next']


def Testing(nums):
    origin = [n for n in nums]
    sol = Solution()
    sol.nextPermutation(nums)
    print origin, '->', nums

if __name__ == '__main__':
    Testing([1])
    Testing([1,2,3])
    Testing([3,2, 1])
    Testing([1,1,5])
    Testing([1,3,2])
    Testing([5,4,7,5,3,2])






