m_l = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            r_list = board[i][:]
            c_list = []
            for c in board:
                c_list.append(c[i])
            r_visited = [False for _ in range(9)]
            c_visited = [False for _ in range(9)]
            for j in range(9):
                if (i in [1, 4, 7]) and (j in [1, 4, 7]):
                    s_visited = [False for _ in range(9)]
                    if '.' != board[i][j]:
                        s_n = int(board[i][j])
                        s_visited[s_n-1] = True
                    for k in range(1, 9):
                        m = m_l[k-1]
                        s_n = board[i+m[0]][j+m[1]]
                        if '.' != s_n:
                            s_n = int(s_n)
                            if s_visited[s_n-1] == False:
                                s_visited[s_n-1] = True
                            else:
                                return False
                if '.' != r_list[j]:
                    r_n = int(r_list[j])
                    if r_visited[r_n-1] == False:
                        r_visited[r_n-1] = True
                    else:
                        print(r_n)
                        return False
                if '.' != c_list[j]:
                    c_n = int(c_list[j])
                    if c_visited[c_n-1] == False:
                        c_visited[c_n-1] = True
                    else:
                        print(i, c_n)
                        return False
        return True