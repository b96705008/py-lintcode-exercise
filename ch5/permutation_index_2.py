class Solution:
    """
    @param A: An array of integers
    @return: A long integer
    """
    def permutationIndexII(self, A):
        # write your code here
        if A is None or len(A) == 0:
            return 1
        
        nums = sorted(A)
        num_dict = self.get_num_dict(A)
        visited = [False for i in nums]
        status = {
            'found': False,
            'index': 0
        }
        self.dfs_find(A, nums, status, True, [], visited, num_dict)
        return status['index']
    
    
    def dfs_find(self, A, nums, status, is_nums, perm, visited, num_dict):
        if len(perm) == len(A):
            status['index'] = status['index'] + 1
            if is_nums:
                status['found'] = True
                print 'FOUND:', status['index']
            return
        
        for i, num in enumerate(nums):
            if visited[i]:
                continue

            if i > 0 and num == nums[i-1] and not visited[i-1]:
                continue
            
            # next step
            perm.append(num)
            visited[i] = True
            num_dict[num] = num_dict[num] - 1
            
            # check if should dfs
            next_is_nums = is_nums and num == A[len(perm)-1]
            print next_is_nums, is_nums, num, A[len(perm)-1]
            if next_is_nums:
                self.dfs_find(A, nums, status, next_is_nums, perm, visited, num_dict)
            else:
                status['index'] = status['index'] + self.get_perm_count(num_dict)
                
            # backtrack
            perm.pop()
            visited[i] = False
            num_dict[num] = num_dict[num] + 1
            
            # check if found
            if status['found']:
                break
    
    
    def get_num_dict(self, nums):
        num_dict = {}
        for n in nums:
            num_dict[n] = num_dict.get(n, 0) + 1
        return num_dict
    
    
    def get_perm_count(self, num_dict):
        perm_cnt = 0
        all_count = 0
        div_values = []
        
        for count in num_dict.values():
            all_count = all_count + count 
            if count <= 1:
                continue
            div_values.append(reduce(lambda x, y: x*y, range(1, count+1)))
        
        perm_cnt = reduce(lambda x, y: x*y, range(1, all_count+1))
        for d_v in div_values:
            perm_cnt = perm_cnt / d_v
        
        return perm_cnt
            
if __name__ == '__main__':
    sol = Solution()
    sol.permutationIndexII([1,1,2,2,3])





