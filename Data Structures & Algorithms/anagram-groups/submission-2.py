
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}

        for word in strs:
            word_arr = [0] * 26

            for char in word:
                word_arr[ord(char) - ord('a') ] += 1
            
            word_arr = tuple(word_arr)
            
            if word_arr not in words:
                words[word_arr] = []
            words[word_arr].append(word)

        return list(words.values())