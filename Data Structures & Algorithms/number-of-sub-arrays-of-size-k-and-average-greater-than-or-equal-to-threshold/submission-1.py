class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int: 
        cumsum = 0
        count = 0
        left, right = 0, 0

        while right < len(arr):
            cumsum += arr[right]

            if right - left + 1 == k:
                count += 1 if cumsum / k >= threshold else 0
                cumsum -= arr[left]
                left += 1
            
            right += 1
        
        return count