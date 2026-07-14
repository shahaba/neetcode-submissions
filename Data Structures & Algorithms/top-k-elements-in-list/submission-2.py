from heapq import heappush, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        freq = [] # heap

        for num in nums:
            if num not in cnt:
                cnt[num] = 0
            cnt[num] += 1
        
        for key, value in cnt.items():
            heappush(freq, (-value, key))

        res = []
        for i in range(k):
            _, key = heappop(freq)
            res.append(key)
        
        return res