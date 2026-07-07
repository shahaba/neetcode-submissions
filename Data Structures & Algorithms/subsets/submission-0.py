class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        subset = []

        def helper(index):
            results.append(subset.copy())
            
            for i in range(index, len(nums)):
                subset.append(nums[i])
                helper(i + 1)
                subset.pop()

        helper(0)
        return results