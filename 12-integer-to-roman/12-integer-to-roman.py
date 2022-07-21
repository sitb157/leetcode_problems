d_i_r = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
d_i_r_s = {4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'}


def iRS(i_n, result):
    if i_n == 0:
        return '', True
    if i_n in d_i_r:
        result += d_i_r[i_n]
    elif i_n in d_i_r_s:
        return d_i_r_s[i_n], False
    else:
        if i_n <= 9000 and i_n > 900:
            result += d_i_r[1000]
            result, _ = iRS(i_n - 1000, result)
        elif i_n <= 900 and i_n > 90:
            result += d_i_r[100]
            result, _ = iRS(i_n - 100, result)
        elif i_n <= 90 and i_n > 9:
            result += d_i_r[10]
            result, _ = iRS(i_n - 10, result)
        else:
            result += d_i_r[1]
            result, _ = iRS(i_n - 1, result)
    return result, True
class Solution:
    def intToRoman(self, num: int) -> str:
        l_n = reversed(list(str(num)))
        roman = ''
        for i, l in enumerate(l_n):
            s_l, n_p = iRS(int(l)*10**i, '')
            if not n_p:
                s_l = reversed(list(s_l))
                s_l = ''.join(s_l)
            roman += s_l
        return ''.join(reversed(list(roman))) 