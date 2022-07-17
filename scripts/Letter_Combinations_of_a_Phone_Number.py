from itertools import product
LETTERS = {'2':['a', 'b', 'c'], '3':['d','e','f'], '4':['g','h', 'i'], '5':['j', 'k', 'l'], '6':['m', 'n', 'o'], '7':['p', 'q', 'r', 's'], '8':['t', 'u', 'v'], '9':['w', 'x', 'y', 'z']}
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []
        digits_list = list(digits)
        letter_list = [LETTERS[d] for d in digits_list]
        pd = list(product(*letter_list))
        result = ["".join(p_) for p_ in pd]
        return result    
