# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # I can do some inorder traversal here, using DFS, to follow the same path
        # along both trees

        # Approach:
        #   Step 1: Search root tree for subroot start
        #   Step 2: Iterate through root tree and subroot tree to see if matching
        #       2.a: If not, return False
        if not subRoot:
            return True
        
        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def sameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        
        if not root or not subRoot:
            return False

        if root.val != subRoot.val:
            return False
        
        return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)

        