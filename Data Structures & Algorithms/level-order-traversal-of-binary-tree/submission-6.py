# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=collections.deque()
        res=[]

        q.append(root)

        while q:

            ql=len(q)

            lis=[]
            for _ in range(ql):

                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    lis.append(node.val)
            if lis:
                res.append(lis)

        return res
