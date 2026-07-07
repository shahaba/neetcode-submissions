class Solution:
    def climbStairs(self, n: int) -> int:
        memo = defaultdict(int)
        memo[0] = 0
        memo[1] = 1

        for step in range(2, n+2):
            memo[step] = memo[step-1] + memo[step-2]
        
        print(memo)
        return memo[step]
