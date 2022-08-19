class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        z_l = []
        for x in range(m):
            for y in range(n):
                if matrix[x][y] == 0:
                    z_l.append([x, y])    
                
        print(z_l)
        for z in z_l:
            t_x = z[0]
            t_y = z[1]
            while(t_x > 0):
                t_x -= 1
                matrix[t_x][z[1]] = 0
            t_x = z[0]
            while(t_x < (m-1)):
                t_x += 1
                matrix[t_x][z[1]] = 0
            while(t_y > 0):
                t_y -= 1
                matrix[z[0]][t_y] = 0
            t_y = z[1]
            while(t_y < (n-1)):
                t_y += 1
                matrix[z[0]][t_y] = 0
                