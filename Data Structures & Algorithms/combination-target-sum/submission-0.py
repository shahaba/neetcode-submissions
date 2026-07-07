class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        subset = []
        results = []

        def helper(index):
            if sum(subset) == target:
                results.append(subset.copy())
                return
            
            if sum(subset) > target:
                return
            
            for i in range(index, len(nums)):
                subset.append(nums[i])
                helper(i)
                subset.pop()
            
        helper(0)
        return results