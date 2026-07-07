class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.inOrder(root) != -1

    def inOrder(self, root) -> int:
        if not root:
            return 0
        
        left = self.inOrder(root.left)
        if left == -1: 
            return -1
        
        right = self.inOrder(root.right)
        if right == -1: 
            return -1

        if abs(left - right) > 1:
            return -1
            
        return max(left, right) + 1