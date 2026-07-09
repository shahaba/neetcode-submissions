class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        counts = {}
        for char in s:
            if char not in counts:
                counts[char] = 0
            counts[char] += 1
        
        print(counts)
        
        for char in t:
            if char in counts and counts[char] > 0:
                counts[char] -= 1
            else:
                return False
        
        print(counts)
        for key in counts:
            if counts[key] != 0:
                return False
        
        return True

        