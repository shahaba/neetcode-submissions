from heapq import heapify, heappop, heappush

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.stones = [-1* stone for stone in stones]
        heapify(self.stones)
        print(self.stones)
        while len(self.stones) > 1:
            first, second = -1 * heappop(self.stones), -1 * heappop(self.stones)
            print(first, second)
            if first == second:
                continue
            else:
                heappush(self.stones, -1 * (first - second))
        
        return -1 * self.stones[0] if self.stones else 0
        