class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        seen = set()
        left = 0

        if not s:
            return 0

        for right in range(len(s)):

            while s[right] in seen:
                length = max(length, right - left)
                seen.remove(s[left])
                left += 1
            
            seen.add(s[right])

    
        return max(length, right - left + 1)