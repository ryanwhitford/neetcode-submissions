class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        if not word:
            return True

        m, n = len(board), len(board[0])

        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        def dfs(i,j,idx):
            if idx == len(word):
                return True
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[idx] or (i,j) in seen:
                return False
            seen.add((i,j))
            res = False
            for di, dj in directions:
                res = res or dfs(i+di, j+dj, idx+1)
            seen.remove((i,j))
            return res

        for i in range(m):
            for j in range(n):
                seen = set()
                if dfs(i, j, 0): return True
        
        return False
