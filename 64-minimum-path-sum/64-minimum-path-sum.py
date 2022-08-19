class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        result = [[0 for _ in range(n)] for _ in range(m)]
        result[0][0] = grid[0][0]
        for i in range(1, m):
            result[i][0] = result[i-1][0] + grid[i][0]
        for i in range(1, n):
            result[0][i] = result[0][i-1] + grid[0][i]
        for x in range(1, m):
            for y in range(1, n):
                result[x][y] = min((result[x-1][y]+grid[x][y]), (result[x][y-1]+grid[x][y]))
        return result[-1][-1]
                