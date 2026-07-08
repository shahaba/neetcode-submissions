from heapq import *

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.stones = [-stone for stone in stones]
        heapify(self.stones)

        while len(self.stones) > 1:
            x = -heappop(self.stones)
            y = -heappop(self.stones)

            if x == y:
                continue
            else:
                heappush(self.stones, -(x - y))

        return -self.stones[0] if self.stones else 0