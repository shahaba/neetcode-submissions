# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        

        def canReachLeaf(root, targetSum):
            if not root:
                return False

            targetSum -= root.val

            if targetSum == 0 and not root.left and not root.right:
                return True

            if canReachLeaf(root.left, targetSum):
                return True
            if canReachLeaf(root.right, targetSum):
                return True

            targetSum += root.val

            return False

        return canReachLeaf(root, targetSum)