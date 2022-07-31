def cSay(_input):
    diff = False
    pre_num = 0
    split_l = []
    for idx, _i in enumerate(_input):
        if pre_num != _i:
            if diff:
                split_l.append(_input[s_idx:idx])
            else:
                diff = True
            s_idx = idx
            pre_num = _i
    if diff:
        split_l.append(_input[s_idx:len(_input)])
    _result = ""
    for _s in split_l:
        n = _s[0]
        _result += "%d"%len(_s)
        _result += n
    print(_result)
    return _result
def rSay(_input, _n, n):
    print(_n, n, _input)
    if _n > n:
        return _input
    return rSay(cSay(_input), _n+1, n)
class Solution:
    def countAndSay(self, n: int) -> str:
        return rSay("1", 1+1, n)