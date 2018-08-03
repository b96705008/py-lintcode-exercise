class Solution:
    """
    @param stones: a list of stones' positions in sorted ascending order
    @return: true if the frog is able to cross the river or false
    """
    def canCross(self, stones):
        # write your code here
        if stones is None or len(stones) == 0:
            return False

        if len(stones) == 1:
            return True

        hash_map = {unit: i for i, unit in enumerate(stones)}

        #return self.jump_DFS(stones, hash_map, 0, 1)
        return self.jump_DP(stones, hash_map)


    def jump_DFS(self, stones, hash_map, index, jump):
        # jump
        next_unit = stones[index] + jump
        if next_unit not in hash_map:
            return False

        if next_unit == stones[-1]:
            return True

        next_index = hash_map[next_unit]
        for i in xrange(-1, 2):
            next_jump = jump + i
            if next_jump == 0:
                continue

            can = self.jump_DFS(stones, hash_map, next_index, next_jump)
            if can:
                return True

        return False

    def jump_DP(self, stones, hash_map):
        f = [{1:1}]

        for i in xrange(1, len(stones)-1):
            curr_unit = stones[i]
            curr_map = {}

            for jump_map in f:
                if curr_unit not in jump_map:
                    continue

                jump = jump_map[curr_unit]
                for i in xrange(-1, 2):
                    next_jump = jump + i
                    if next_jump == 0:
                        continue

                    next_unit = curr_unit + next_jump
                    if next_unit not in hash_map:
                        continue

                    if next_unit == stones[-1]:
                        return True

                    curr_map[next_unit] = next_jump

            f.append(curr_map)

        return False


if __name__ == '__main__':
    sol = Solution()

    stones = [0,1,3,5,6,8,12,17]
    print sol.canCross(stones)

    stones = [0,1,2,3,4,8,9,11]
    print sol.canCross(stones)
