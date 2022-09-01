class Solution:
    def sI(self, input_):
        output_ = 0
        i_l = len(input_)
        for idx, key_ in enumerate(input_):
            output_ +=  10**((i_l-1)-idx)*int(key_)
        return output_
    
    def vC(self, input_):
        if len(input_) != 1:
            if input_[0] == '0':
                return None
        if len(input_) <= 2:
            return self.sI(input_)
        if len(input_) == 3:
            s_i = self.sI(input_)
            if 0 <= s_i and s_i <= 255:
                return s_i
            else:
                return None
        
    def rR(self, s_idx, r_idx, r_n, s_n, s_l, r_s, result):
        if len(s_l[r_idx:]) > (r_n*3):
            return result
        if len(s_l[r_idx:]) < (r_n*1):
            return result
        
        v_c = self.vC(s_l[s_idx:r_idx])
        if v_c != None:
            if r_n == 0:
                r_s += str(v_c)
                result.append(r_s)
                return result
            else:
                r_s += str(v_c) + '.'
        else:
            return result
        for i in range(1,4):
            result = self.rR(r_idx, r_idx+i, r_n-1, s_n, s_l, r_s, result)
        return result

    def restoreIpAddresses(self, s: str) -> List[str]:
        s_l = list(s)
        s_n = len(s_l)
        result = []
        for j in range(1,4):
            result = self.rR(0, 0+j, 3, s_n, s_l, '', result)
        return set(result)