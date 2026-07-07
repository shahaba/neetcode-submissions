class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded = []
        for word in strs:
            encoded.append(str(len(word))+"#"+word)
        
        print(encoded)
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        start = 0
        results = []
        print(s)
        while start < len(s):
            digit = 0
            while s[start] != '#':
                digit += 1
                start += 1
            length = int(s[start-digit:start])
            stop = start + length
            word = "".join(s[start+1:stop+1])
            print(word, start, stop)

            start += length + 1
            print("New start: ", start)
            results.append(word)
        
        return results