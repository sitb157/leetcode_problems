class Solution:
    def reverse(self, x: int) -> int:
        x_str = str(x)
        n_c = False
        if x_str[0] == '-':
            r_x = list(x_str[1:])
            n_c = True
        else:
            r_x = list(x_str[:])
        r_x.reverse()
        r_x_int = int(''.join(r_x))
        if n_c:
            r_x_int = -1 * r_x_int
            
        if r_x_int < -2**31:
            return 0
        elif r_x_int > (2**31-1):
            return 0
        else:
            return r_x_int
