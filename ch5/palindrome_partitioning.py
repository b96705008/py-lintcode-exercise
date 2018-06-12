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
        
        self.dfs_find(s, 0, [], partitions)
        return partitions
    
    def dfs_find(self, s, start_index, partition, partitions):
        if start_index == len(s):
            partitions.append(partition[:])
            return
    
        i = start_index
        while i < len(s):
            part = s[start_index:i+1]
            if self.is_palindrome(part):
                partition.append(part)
                self.dfs_find(s, i+1, partition , partitions)
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
        
sol = Solution()
p = sol.partition('aab')
print p