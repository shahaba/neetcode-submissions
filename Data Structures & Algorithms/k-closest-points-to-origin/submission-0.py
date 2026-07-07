class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.min_heap = [(x1**2 + x2**2, [x1, x2]) for x1, x2 in points]
        heapq.heapify(self.min_heap)

        results = []
        for i in range(k):
            results.append(heapq.heappop(self.min_heap)[1])
        
        return results