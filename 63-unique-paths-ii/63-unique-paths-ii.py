class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        result = [[0 for _ in range(n)] for _ in range(m)]
        if obstacleGrid[0][0] != 1:
            result[0][0] = 1
            
        for x in range(m):
            for y in range(n):
                if (((x - 1) < 0) and ((y - 1) < 0)) or obstacleGrid[x][y] == 1:
                    continue
                else:
                    if (y - 1) < 0:
                        result[x][y] = result[x-1][0]
                    elif (x - 1) < 0:
                        print(x, y)
                        result[x][y] = result[0][y-1]
                    else:
                        result[x][y] = result[x][y-1] + result[x-1][y]
                
        return result[-1][-1]