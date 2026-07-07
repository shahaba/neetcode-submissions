class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # create a list of size 26
        count_chars = [0] * 26

        for elem in s:
            count_chars[(ord(elem) - 97) % 26] += 1
        
        for elem in t:
            count_chars[(ord(elem) - 97) % 26] -= 1
        
        for c in count_chars:
            if c != 0:
                return False
        
        return True