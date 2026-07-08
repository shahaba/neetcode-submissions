from heapq import heappush, heappop
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            heappush(heap, (self.dist(point), point))

        return [heappop(heap)[1] for _ in range(k)]

    def dist(self, x):
        return math.sqrt(x[0]**2 + x[1]**2)