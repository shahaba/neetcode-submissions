class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum, currSum = -math.inf, 0
        for num in nums:
            currSum = max(currSum, 0) + num
            
            maxSum = max(maxSum, currSum)
        
        return maxSum