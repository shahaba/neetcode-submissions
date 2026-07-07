# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def helper(root):
            if not root:
                return 0
            
            left_sub = helper(root.left)
            if left_sub == -1:
                return -1

            right_sub = helper(root.right)
            if right_sub == -1:
                return -1

            if abs(left_sub - right_sub) > 1:
                return -1

            return 1 + max(left_sub, right_sub)

        return helper(root) != -1