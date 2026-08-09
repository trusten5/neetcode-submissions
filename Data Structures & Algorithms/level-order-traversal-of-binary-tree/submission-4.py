# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # que up the initial root, look at the length of que, for each 
        # elem in the queue enqueue both children, append t list, then 
        # add that list to res

        q = collections.deque()
        q.append(root)
        res=[]

        while q:
            runs = len(q)
            lists=[]
            while runs>0:
                curr=q.popleft()
                if curr:
                    q.append(curr.left)
                    q.append(curr.right)
                    lists.append(curr.val)
                runs-=1
            if lists:
                res.append(lists)

        return res