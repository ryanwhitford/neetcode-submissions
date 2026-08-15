class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        
        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append([i,j])
        
        while q:
            i, j = q.popleft()
            for di, dj in directions:
                i2, j2 = i + di, j + dj
                if (
                    0 <= i2 < m and
                    0 <= j2 < n and
                    grid[i2][j2] == 2147483647
                ):
                    grid[i2][j2] = 1 + grid[i][j]
                    q.append([i2,j2])

        return