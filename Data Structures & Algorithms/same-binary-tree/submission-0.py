# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Either DFS or BFS should return the same result at each iteration
        # I will take the DFS approach, and check if the nodes are the same
        
        # Base Case
        if not p and not q:
            return True

        if not p or not q:
            return False
        
        # if the value of the trees don't match
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        

