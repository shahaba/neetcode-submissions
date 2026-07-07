class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash_map = {}

        for word in strs:
            char_list = [0] * 26
            for w in word:
                char_list[(ord(w) - ord('a'))] += 1
            key = tuple(char_list)
            if key not in hash_map:
                hash_map[key] = [word]
            else:
                hash_map[key].append(word)

        return hash_map.values()

