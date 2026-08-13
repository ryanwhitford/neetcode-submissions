class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        maxArea = 0

        def bfs(r, c):
            q = deque()
            visit.add((r,c))
            q.append((r,c))
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            A = 1
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    r2, c2 = r + dr, c + dc
                    if (0 <= r2 < rows and
                    0 <= c2 < cols and 
                    (r2,c2) not in visit and
                    grid[r2][c2] == 1):
                        A += 1
                        visit.add((r2,c2))
                        q.append((r2,c2))
            return A
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    A = bfs(r, c)
                    maxArea = max(A, maxArea)
        return maxArea