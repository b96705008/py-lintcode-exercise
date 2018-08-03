class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, dic):
        # write your code here
        if s is None or dic is None:
            return False
        
        if len(s) == 0:
            return True
        
        max_len = self.get_max_len(dic)
        
        return self.dfs_find(max_len, s, 0, dic)
    
    def get_max_len(self, dic):
        max_len = float('-inf')
        for w in dic:
            if len(w) > max_len:
                max_len = len(w)
        return max_len
    
    def dfs_find(self, max_len, s, start_index, dic):
        if start_index >= len(s):
            return True
        
        i = start_index
        while i < len(s):
            word = s[start_index:i+1]
            if len(word) > max_len:
                break
            print word
            if word in dic:
                print word
                is_found = self.dfs_find(max_len, s, i+1, dic)
                if is_found:
                    return is_found
            i = i + 1
            
        return False


sol = Solution()

s = 'lintcodefhaskjhfkjahfkjhfjkhkjwqhfqkhkjhfkjwhhhhhhhejkqww'
dic = ['lint', 'code']
print sol.wordBreak(s, dic)