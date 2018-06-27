class Solution:
    """
    @param: nums: an array with positive and negative numbers
    @param: k: an integer
    @return: the maximum average
    """
    def maxAverage(self, nums, k):
        # write your code here
        max_num = float('-inf')
        min_num = float('inf')
        for n in nums:
            max_num = max(max_num, n)
            min_num = min(min_num, n)

        while max_num - min_num >= 1e-6:
            mid = float(max_num + min_num) / 2.

            if self.is_larger(nums, mid, k):
                min_num = mid
            else:
                max_num = mid

        return min_num

    def is_larger(self, nums, mid, k):
        sums = [0]
        min_pre = 0

        for i in range(1, len(nums)+1):
            cur_sum = sums[i-1] + nums[i-1] - mid
            sums.append(cur_sum)
            if i >= k:
                if cur_sum - min_pre >= 0:
                    return True
                min_pre = min(min_pre, sums[i-k+1])
            
        return False
        

if __name__ == '__main__':
    sol = Solution()

    nums = [1, 12, -5, -6, 50, 3]
    k = 3
    print sol.maxAverage(nums, k)
