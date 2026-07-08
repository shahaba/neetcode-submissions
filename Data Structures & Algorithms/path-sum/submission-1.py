# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        

        def canReachLeaf(root, curr):
            if not root:
                return False

            curr += root.val
            if not root.left and not root.right:
                return curr == targetSum

            return canReachLeaf(root.left, curr) or canReachLeaf(root.right, curr)

        return canReachLeaf(root, 0)