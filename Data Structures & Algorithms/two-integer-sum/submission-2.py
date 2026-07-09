class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {nums[idx]:idx for idx in range(len(nums))}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in idx and idx[diff] != i:
                return [i, idx[diff]]

        return False