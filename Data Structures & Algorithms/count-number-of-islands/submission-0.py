class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r, c):
            q = deque()
            q.append((r,c))
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    r2, c2 = r + dr, c + dc
                    if (0 <= r2 < rows and
                    0 <= c2 < cols and 
                    (r2,c2) not in visit and
                    (r2,c2) not in q and
                    grid[r2][c2] == "1"):
                        visit.add((r2,c2))
                        q.append((r2,c2))
            return
                



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands +=1
        return islands