class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat = []
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m*n-1
        while l<=r:
            k = (l + r) // 2
            i = k // n
            j = k % n
            if matrix[i][j] < target:
                l=k+1
            elif matrix[i][j] > target:
                r=k-1
            else:
                return True
        return False
