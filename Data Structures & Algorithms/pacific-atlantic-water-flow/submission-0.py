class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacific = [[False for _ in range(n)] for _ in range (m)]
        atlantic = [[False for _ in range(n)] for _ in range (m)]
        p, a = [], []
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    pacific[i][j] = True
                    p.append([i,j])
                if i == m-1 or j == n-1:
                    atlantic[i][j] = True
                    a.append([i,j])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        def bfs(source, ocean):
            q = deque(source)
            while q:
                i, j = q.popleft()
                for di, dj in directions:
                    i2, j2 = i + di, j + dj
                    if (0 <= i2 < m and 0 <= j2 < n and
                    heights[i2][j2] >= heights[i][j] and
                    not ocean[i2][j2]):
                        ocean[i2][j2] = True
                        q.append([i2,j2])
            return
        bfs(p, pacific)
        bfs(a, atlantic)
        res = []
        for i in range(m):
            for j in range(n):
                if atlantic[i][j] and pacific[i][j]:
                    res.append([i,j])
        return res

        