class Solution:
    def simplifyPath(self, path: str) -> str:
        p_l = path.split('/')
        s = ''
        for p in p_l:
            print(s)
            if p != '':
                if p == '..':
                    if len(s) > 0:
                        pre_s = ''
                        for t_s in s.split('/')[:-1]:
                            if t_s != '':
                                pre_s += '/'
                                pre_s += t_s
                        s = pre_s
                    else:
                        s = '/'
                elif p == '.':
                    pass
                elif p == '/':
                    pass
                else:
                    if s == '/':
                        pass
                    else:
                        s += '/'
                    s += p
        if len(s) > 0:
            return s
        else:
            return '/'