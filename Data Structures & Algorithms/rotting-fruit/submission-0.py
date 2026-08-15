class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh = 0
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append([i,j])
                if grid[i][j] == 1:
                    fresh +=1
        
        time = 0
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        while q and fresh:
            length = len(q)
            for _ in range(length):
                i, j = q.popleft()
                for di, dj in directions:
                    i2, j2 = i + di, j + dj
                    if (
                        0 <= i2 < m and
                        0 <= j2 < n and
                        grid[i2][j2] == 1
                    ):
                        grid[i2][j2] = 2
                        q.append([i2,j2])
                        fresh -=1
            time +=1
        
        return time if fresh == 0 else -1