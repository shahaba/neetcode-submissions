class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # sort the list
        nums.sort()
        
        # iterate from 1 : list end
        for i in range(1, len(nums)):
            # if adjacent pairs are match, return True
            if nums[i-1] == nums[i]:
                return True
        
        # if we get through the list without finding a duplicate, return False
        return False