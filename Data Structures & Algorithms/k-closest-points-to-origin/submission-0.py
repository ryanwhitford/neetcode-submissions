class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = [(-point[0]**2 - point[1]**2, point) for point in points]
        heapq.heapify(maxheap)
        while len(maxheap) > k:
            heapq.heappop(maxheap)

        res = []
        for tup in maxheap:
            res.append(tup[1])
        return res
        
        
