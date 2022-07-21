class Solution:
    def myAtoi(self, s: str) -> int:
        n_q = "0123456789. "
        n_p_q = "-+"
        comma = '.'
        f_c = False
        n_in = False
        i = 0
        result = []
        b_c = False
        while i < len(s):
            if (s[i] in n_q) or (s[i] in n_p_q):
                if b_c:
                    break
                if len(result) >= 1:
                    if len(result) == 1 and s[i] in n_p_q:
                        return 0
                    elif s[i] in n_p_q:
                        break
                        
                if s[i] == comma:
                    f_c = True
                n_in = True
                if (s[i] == ' '):
                    if len(result) >= 1:
                        b_c = True
                else:
                    result.append(s[i])
            else:
                break
            i += 1
            
        if len(result) == 0:
            return 0
        
        if len(result) == 1:
            if result[0] in n_p_q:
                return 0
                  
        n_p = False
        if result[0] == '-':
            n_p = True
            result = result[1:]
        
        try:
            result = int(''.join(result))
        except:
            result = float(''.join(result))
        result = int(result)

        if n_p:
            result = -1 * result
        result = min(result, 2**31-1)
        result = max(result, -2**31)
        return result