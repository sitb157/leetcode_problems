# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rI(self, tree, result):
        if tree != None:
            result = self.rI(tree.left, result)
            result.append(tree.val)
            result = self.rI(tree.right, result)
        return result
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.rI(root, [])
        