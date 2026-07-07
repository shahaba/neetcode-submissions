class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for idx, val in enumerate(nums):
            diff = target - val
            if val in seen:
                return [seen[val], idx]
            
            seen[diff] = idx
