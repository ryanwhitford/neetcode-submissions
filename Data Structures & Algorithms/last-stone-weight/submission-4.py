import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            s1 = -heapq.heappop(heap)
            s2 = -heapq.heappop(heap)
            if s1 > s2:
                heapq.heappush(heap, s2-s1)
        if heap:
            res = heapq.heappop(heap)
        else:
            res = 0
        return -res