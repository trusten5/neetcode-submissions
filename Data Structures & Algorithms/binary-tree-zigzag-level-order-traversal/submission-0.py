# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        q.append(root)
        res=[]
        while q:
            leng=len(q)
            lis=[]
            for i in range(leng):
                node=q.popleft()
                if node:
                    lis.append(node.val)
                    q.append(node.right)
                    q.append(node.left)
            print(res, len(res)%2)
            if len(res)%2==0:
                lis.reverse()
            if lis:
                res.append(lis)
            

        return res

                