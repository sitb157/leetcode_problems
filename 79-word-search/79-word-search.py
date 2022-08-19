from collections import deque
class Solution:
    def rP(self, pose, v_l, m, n, w_l, w_i, board):
        x = pose[0]
        y = pose[1]
        if w_i == len(w_l):
            return True
        for n_i in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            n_x = x + n_i[0]
            n_y = y + n_i[1]
            if (n_x >= 0) and (n_x < m) and (n_y >= 0) and (n_y < n):
                if v_l[n_x][n_y] == False:
                    if w_l[w_i] == board[n_x][n_y]:
                        v_l[n_x][n_y] = True
                        result = self.rP([n_x, n_y], v_l, m, n, w_l, w_i+1, board)
                        if result:
                            return True
                        v_l[n_x][n_y] = False
        return False
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        w_l = list(word)
        for x in range(m):
            for y in range(n):
                w_i = 0
                if w_l[w_i] == board[x][y]:
                    v_l = [[False for _ in range(n)] for _ in range(m)]
                    v_l[x][y] = True
                    result = self.rP([x, y], v_l, m, n, w_l, 1, board)
                    v_l[x][y] = False
                    if result:
                        return True                    
        return False
                
                
        