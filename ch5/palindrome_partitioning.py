class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """
    def partition(self, s):
        # write your code here
        partitions = []
        if s is None or len(s) == 0:
            return partitions
        
        p_matrix = self.get_palindrome_matrix(s)
        self.dfs_find(p_matrix, s, 0, [], partitions)
        return partitions
    
    def dfs_find(self, p_matrix, s, start_index, partition, partitions):
        if start_index == len(s):
            partitions.append(partition[:])
            return
    
        i = start_index
        while i < len(s):
            part = s[start_index:i+1]
            #if self.is_palindrome(part):
            if p_matrix[start_index][i]: 
                partition.append(part)
                self.dfs_find(p_matrix, s, i+1, partition , partitions)
                partition.pop()
            i = i + 1

    def is_palindrome(self, s):
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i = i + 1
            j = j - 1
        
        return True

    def get_palindrome_matrix(self, s):
        # init matrix
        n = len(s)
        p_mtx = []
        for i in range(n):
            p_mtx.append([None for j in range(n)])

        # same chars
        for i in range(n):
            p_mtx[i][i] = True

        # adjacent chars
        for i in range(n-1):
            p_mtx[i][i+1] = s[i] == s[i+1]

        # other chars
        i = n-3
        while i >= 0:
            j = i + 2
            while j < n:
                p_mtx[i][j] = p_mtx[i+1][j-1] and s[i]==s[j]
                j = j + 1
            i = i - 1

        return p_mtx
        
sol = Solution()
p = sol.partition('aab')
print p