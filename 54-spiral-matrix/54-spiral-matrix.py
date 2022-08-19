from collections import deque
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        r_l = len(matrix)
        c_l = len(matrix[0])
        v_l = [[False for _ in range(c_l)] for _ in range(r_l)]
        c = 0
        v = deque()
        s_i = 0
        s_j = 0
        v_l[s_i][s_j] = True
        v.append([s_i, s_j])
        result = []
        o_t = False
        while v:
            t = v.popleft()
            result.append(matrix[t[0]][t[1]])
            v_l[t[0]][t[1]] = True
            n_i = t[0] + m[c%4][0]
            n_j = t[1] + m[c%4][1]
            o_t = False
            if (n_i < 0) or (r_l <= n_i) or (n_j < 0) or (c_l <= n_j):
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
                if (n_i < 0) or (r_l <= n_i) or (n_j < 0) or (c_l <= n_j):
                    pass
                else:
                    if v_l[n_i][n_j]:
                        pass
                    else:
                        v.append([n_i, n_j])
            
        return result
            
            
        