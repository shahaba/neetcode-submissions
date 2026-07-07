# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_path = 0
        
        def helper(root):
            if not root:
                return 0

            left_sub = helper(root.left)
            right_sub = helper(root.right)

            self.max_path = max(self.max_path, left_sub + right_sub)

            return 1 + max(left_sub, right_sub)
        
        helper(root)
        return self.max_path