class Solution:
    """
    @param s: A string
    @return: An integer
    """
    min_cuts = float('inf')

    def get_palindrome(self, s):
        # init palindrome
        p_mtx = []
        n = len(s)
        for i in range(n):
            p_mtx.append([None for j in range(n)])
        
        # single char
        for i in range(n):
            p_mtx[i][i] = True
        
        # adjacent chars
        for i in range(n-1):
            p_mtx[i][i+1] = s[i] == s[i+1]
        
        # other chars
        for i in xrange(n-3, -1, -1):
            for j in xrange(i+2, n):
                p_mtx[i][j] = p_mtx[i+1][j-1] and s[i]==s[j]
        
        return p_mtx
    
    def minCut(self, s):
        # write your code here
        if s is None or len(s) == 0:
            return 0
        
        p_mtx = self.get_palindrome(s)
        self.dfs_cut(p_mtx, s, 0, -1)

        return self.min_cuts
        
    def dfs_cut(self, p_mtx, s, start_index, cut_num):
        if start_index == len(s):
            if cut_num < self.min_cuts:
                self.min_cuts = cut_num
            return
        
        i = start_index
        while i < len(s):
            if p_mtx[start_index][i]:
                self.dfs_cut(p_mtx, s, i+1, cut_num+1)
            i = i + 1
                        
sol = Solution()

s = 'ababababababababababababcbabababababababababababa'
print sol.minCut(s)

# mc = sol.minCut('ababababababababababababcbabababababababababababa')
# #mc = sol.minCut('ababcbaba')
# print mc