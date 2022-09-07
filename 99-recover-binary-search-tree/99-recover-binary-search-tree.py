# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rR(self, max_t, min_t, c_t, max_, min_, root):
        if (min_ != None) and (c_t.val <= min_):
            min_t.val, c_t.val = c_t.val, min_t.val
            r_t = root
            self.rR(None, None, r_t, None, None, root)
            return None
        if (max_ != None) and (c_t.val >= max_):
            max_t.val, c_t.val = c_t.val, max_t.val
            r_t = root
            self.rR(None, None, r_t, None, None, root)
            return None
        if c_t.left != None:
            t_t = c_t
            self.rR(t_t, min_t, c_t.left, c_t.val, min_, root)
        if c_t.right != None:
            t_t = c_t
            self.rR(max_t, t_t, c_t.right, max_, c_t.val, root)
        return None
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        print(root)
        c_t = root
        self.rR(None, None, c_t, None, None, root)
        