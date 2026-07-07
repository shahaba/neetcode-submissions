class Solution:
    def climbStairs(self, n: int) -> int:
        prev, curr = 0, 1

        for step in range(n):
            prev, curr = curr, prev + curr
        
        return curr
