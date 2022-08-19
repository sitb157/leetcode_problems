class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        r_dict = dict()
        for s_ in strs:
            s_l = ''.join(sorted(list(s_)))
            if s_l in r_dict:
                r_dict[s_l].append(s_)
            else:
                r_dict[s_l] = [s_]
        for k, v in r_dict.items():
            result.append(v)
        return result
        