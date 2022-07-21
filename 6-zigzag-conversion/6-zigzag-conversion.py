class Solution:
    def convert(self, s: str, numRows: int) -> str:
        print_list = [['' for _ in range(len(s))] for _ in range(numRows)]
        if numRows < 2:
            return s
        
        i = 0
        j = 0
        k = 0
        r_mode = False
        while (i < len(s)):
            if r_mode:
                print_list[j][k] = s[i]
                j -= 1
                k += 1
                if j < 0:
                    r_mode = False
                    j = 1
                    k -= 1
            else:
                print_list[j][k] = s[i]
                j += 1
                if j == numRows:
                    r_mode = True
                    j = numRows - 2
                    k += 1
            i += 1
        result = ''
        for p_l in print_list:
            result += ''.join(p_l)
        return result