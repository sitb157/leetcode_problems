def stringToInt(_input):
    _result = 0
    _input_s = _input.split()
    print(_input_s)
    l_i = len(_input_s)
    for idx, i_s in enumerate(_input_s):
        _result += int(i_s) * 10**(l_i-(idx+1))
    return _result

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(stringToInt(num1)*stringToInt(num2))
        