class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = float('inf')
        cumsum, left = 0, 0

        for right in range(len(nums)):
            cumsum += nums[right]

            while cumsum >= target:
                length = min(length, right - left + 1)
                cumsum -= nums[left]
                left += 1

        return 0 if length == float('inf') else length
        