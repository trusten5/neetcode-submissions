# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # placeholder for basecase
        if not subRoot:
            return True
        elif not root and subRoot:
            return False

        if self.same(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        
    def same(self, p, q):
        if not p and not q:
            return True
        elif not p or not q:
            return False

        return p.val==q.val and self.same(p.right,q.right) and self.same(p.left,q.left)

        

        