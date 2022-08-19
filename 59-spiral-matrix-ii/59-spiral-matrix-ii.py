from collections import deque
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        m = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        v_l = [[False for _ in range(n)] for _ in range(n)]
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        c = 0
        v = deque()
        s_i = 0
        s_j = 0
        v_l[s_i][s_j] = True
        v.append([s_i, s_j])
        o_t = False
        r = 0
        while v:
            t = v.popleft()
            r += 1
            matrix[t[0]][t[1]] = r
            v_l[t[0]][t[1]] = True
            n_i = t[0] + m[c%4][0]
            n_j = t[1] + m[c%4][1]
            o_t = False
            if (n_i < 0) or (n <= n_i) or (n_j < 0) or (n <= n_j):
                c += 1
                o_t = True
            else:
                if v_l[n_i][n_j]:
                    c += 1
                    o_t = True
                else:
                    v.append([n_i, n_j])
            if o_t:
                n_i = t[0] + m[c%4][0]
                n_j = t[1] + m[c%4][1]
                if (n_i < 0) or (n <= n_i) or (n_j < 0) or (n <= n_j):
                    pass
                else:
                    if v_l[n_i][n_j]:
                        pass
                    else:
                        v.append([n_i, n_j])
            
        return matrix
            