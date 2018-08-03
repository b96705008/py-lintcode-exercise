"""
Description
Given an array of integers, 
find two numbers that their difference equals to a target value.
where index1 must be less than index2. 
Please note that your returned answers (both index1 and index2) are NOT zero-based.


Notice
It's guaranteed there is only one available solution


Example
Given nums = [2, 7, 15, 24], target = 5
return [1, 2] (7 - 2 = 5)
"""

class Solution:
    """
     * @param nums an array of Integer
     * @param target an integer
     * @return [index1 + 1, index2 + 1] (index1 < index2)
    """
    # method 1 (HashMap): time O(n), space O(n)
    def run_method1(self, nums, target):
        hash_map = {}
        for i, n in enumerate(nums):
            smaller_cand = n - target
            if smaller_cand in hash_map:
                print smaller_cand, n, 'in',
                return [hash_map[smaller_cand]+1, i+1]

            bigger_cand = n + target
            if bigger_cand in hash_map:
                print bigger_cand, n, 'in',
                return [hash_map[bigger_cand]+1, i+1]

            hash_map[n] = i

        return None

    # method 2 (Two Pointers): time O(nlogn), space O(n)
    def run_method2(self, nums, target):
        sorted_ns = sorted([(n, i) for i, n in enumerate(nums)], \
                            key=lambda t: t[0])

        size = len(sorted_ns)
        i1 = 0
        i2 = 1
        while i1 < size and i2 < size and i1 < i2:
            cur_diff = sorted_ns[i2][0] - sorted_ns[i1][0]
            if cur_diff == target:
                print sorted_ns[i2][0], sorted_ns[i1][0], 'in',
                return sorted([sorted_ns[i1][1]+1, sorted_ns[i2][1]+1])
            elif cur_diff < target:
                i2 = i2 + 1
            else:
                i1 = i1 + 1
                if i2 == i1:
                    i2 = i2 + 1

        return None

    def two_sum(self, nums, target):
        if nums is None or len(nums) < 2:
            return None

        return self.run_method1(nums, target)
        #return self.run_method2(nums, target)


if __name__ == '__main__':
    sol = Solution()

    print sol.two_sum([2, 7, 15, 24], 5)
    print sol.two_sum([7, 15, 2, 24], 5)
    print sol.two_sum([2, 7, 15, 24], 17)
    print sol.two_sum([2, 5, 7, 12], 2)

