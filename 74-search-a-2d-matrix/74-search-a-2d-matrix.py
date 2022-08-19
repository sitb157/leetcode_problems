class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        for y in range(m):
            min_n = matrix[y][0]
            max_n = matrix[y][-1]
            if min_n == target:
                return True
            if max_n == target:
                return True
            if (min_n < target) and (max_n > target):
                l = len(matrix[y])
                s = 0
                x = int((l-s)/2)     
                while abs(l - s) > 1:
                    n = matrix[y][x]
                    if n == target:
                        return True
                    if n > target:
                        l = x
                        s = s
                        x = int((l-s)/2)
                    else:
                        l = l
                        s = x
                        x = int((l-s)/2) + x   
                        
                return False
        return False
                        