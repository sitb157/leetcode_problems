# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rR(self, max_t, min_t, c_t, max_, min_, s_l):
        if c_t.left != None:
            t_t = c_t
            s_l = self.rR(t_t, min_t, c_t.left, c_t.val, min_, s_l)
        if (min_ != None) and (c_t.val <= min_):
            s_l.append([min_t, c_t])
        if (max_ != None) and (c_t.val >= max_):
            s_l.append([c_t, max_t])
        if c_t.right != None:
            t_t = c_t
            s_l = self.rR(max_t, t_t, c_t.right, max_, c_t.val, s_l)
        return s_l
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        print(root)
        c_t = root
        s_l = []
        s_l = self.rR(None, None, c_t, None, None, s_l)
        s1 = s_l[0][0]
        s2 = s_l[-1][1]
        s1.val, s2.val = s2.val, s1.val
            
            
            
        