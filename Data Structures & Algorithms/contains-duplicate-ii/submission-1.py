class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        left, right = 0, 1

        if len(nums) <= 1:
            return False
        
        window.add(nums[left])

        while right < len(nums):

            if nums[right] in window:
                return True
            
            window.add(nums[right])

            if right - left == k:
                window.remove(nums[left])
                left += 1
            
            right += 1


        return False