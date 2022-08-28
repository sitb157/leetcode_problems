import copy
class Solution:
    def rS(self, s_i, c_n, m_n, c_s, s_l, nums):
        if c_n == m_n:
            c_s.sort()
            c_s_l = self.lS(c_s)
            s_l.append(c_s_l)
            return s_l
        for idx in range(s_i, len(nums)):
            temp = copy.deepcopy(c_s)
            temp.append(nums[idx])
            s_l = self.rS(idx+1, c_n+1, m_n, temp, s_l, nums)
        return s_l
    
    def lS(self, input_):
        output_ = ''
        if len(input_) == 0:
            return output_
        for i in input_:
            output_  += '/' + str(i)
        return output_
            
    def sL(self, input_):
        output_ = []
        for i in input_.split('/'):
            if not i == '':
                output_.append(int(i))
        return output_
    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n_l = len(nums)
        s_l = []
        for i in range(len(nums)+1):
            s_l = self.rS(0, 0, i, [], s_l, nums)
        results = []
        s_l = list(set(s_l))
        for s_ in s_l:
            results.append(self.sL(s_))
        return results