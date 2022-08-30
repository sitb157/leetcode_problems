from collections import deque
class Solution: 
    def numDecodings(self, s: str) -> int:
        s_l = list(s)
        n_l = len(s_l)
        d_l = [0 for _ in range(n_l)]
        if s_l[0] == '0' or n_l == 0:
            return 0
        if n_l == 1:
            return 1
        d_l[0] = 1
        if s_l[1] == '0':
            if s_l[0] == '1' or s_l[0] == '2':
                d_l[1] = d_l[0]
        else: 
            if s_l[0] == '1':
                d_l[1] = d_l[0] + 1
            else:
                if s_l[0] == '2':
                    if int(s_l[1]) <= 6:
                        d_l[1] = d_l[0] + 1
                    else:
                        d_l[1] = d_l[0]
                else:
                    d_l[1] = d_l[0]
                
        for i in range(2,n_l):
            if s_l[i] == '0':
                if s_l[i-1] == '1' or s_l[i-1] == '2':
                    d_l[i] = d_l[i-2]
                else:
                    return 0
            else:
                if s_l[i-1] == '1':
                    d_l[i] = d_l[i-1] + d_l[i-2]
                else:
                    if s_l[i-1] == '2':
                        if int(s_l[i]) <= 6:
                            d_l[i] = d_l[i-1] + d_l[i-2]
                        else:
                            d_l[i] = d_l[i-1]
                    else:
                        d_l[i] = d_l[i-1]
        print(d_l)
        return d_l[-1]