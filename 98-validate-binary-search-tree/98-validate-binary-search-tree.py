# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import copy 
class Solution:
    def vR(self, tree, result, c_l):
            if not result:
                return result
            print(tree.val)
            for key in c_l:
                if key[1] and tree.val >= key[0]: 
                    return False * result
                if not key[1] and tree.val <= key[0]: 
                    return False * result
            if tree.left != None:
                l_tree = tree.left
                t_l = copy.deepcopy(c_l)
                t_l.append([tree.val, True])
                result = self.vR(l_tree, result, t_l)
            if tree.right != None:
                r_tree = tree.right
                t_l = copy.deepcopy(c_l)
                t_l.append([tree.val, False])
                result = self.vR(r_tree, result, t_l)
            return result
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        print(root)
        c_tree = root
        result = True
        c_l = []
        if c_tree.left != None:
            l_tree = c_tree.left
            t_l = copy.deepcopy(c_l)
            t_l.append([c_tree.val, True])
            result = self.vR(l_tree, result, t_l)
        if c_tree.right != None and result:
            r_tree = c_tree.right
            t_l = copy.deepcopy(c_l)
            t_l.append([c_tree.val, False])       
            result = self.vR(r_tree, result, t_l)
        return result