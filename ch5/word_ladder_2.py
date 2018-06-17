"""
Given two words (start and end), and a dictionary, 
find all shortest transformation sequence(s) from start to end, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary

Example
Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]

Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
"""

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dic):
        # write your code here
        seqs = []
        if start is None or end is None:
            return seqs

        complete_dic = dic
        if complete_dic is None:
            complete_dic = set([end])
        else:
            complete_dic.add(end)

        distances = self.bfs_compute_dist(start, end, complete_dic)

        cur_seq = [start]
        visited = set([start])
        self.dfs_find_shortest_seqs(end, complete_dic, distances,
                                    visited, cur_seq, seqs)
        return seqs


    def bfs_compute_dist(self, start, end, dic):
        # find back
        complete_dic = dic.copy()
        complete_dic.add(start)
        queue = [end]
        visited = set([end])
        distances = {end: 0}

        while len(queue) > 0:
            word = queue.pop(0)
            if word == start:
                break
            neighbors = self.expand_neighbors(word, complete_dic)
            for neighbor in neighbors:
                if neighbor in visited:
                    continue
                distances[neighbor] = distances[word] + 1
                queue.append(neighbor)
                visited.add(neighbor)

        return distances


    def expand_neighbors(self, word, dic):
        neighbors = []

        for i, c in enumerate(word):
            for new_c_index in xrange(26):
                new_c = chr(ord('a')+new_c_index)
                # skip same word
                if new_c == c:
                    continue

                new_word = word[:i] + new_c + word[i+1:]
                if new_word in dic:
                    neighbors.append(new_word)

        return neighbors


    def dfs_find_shortest_seqs(self, end, dic, distances, visited, cur_seq, seqs):
        last_word = cur_seq[-1]
        if last_word == end:
            seqs.append(cur_seq[:])
            return

        neighbors = self.expand_neighbors(last_word, dic)
        for neighbor in neighbors:
            if neighbor in visited:
                continue
            if neighbor not in distances:
                continue
            if distances[last_word] <= distances[neighbor]:
                continue

            cur_seq.append(neighbor)
            visited.add(neighbor)
            self.dfs_find_shortest_seqs(end, dic, distances, visited, 
                                        cur_seq, seqs)
            cur_seq.pop()
            visited.remove(neighbor)


sol = Solution()
print sol.findLadders('hit', 'cog', set(["hot","dot","dog","lot","log"]))
