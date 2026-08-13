class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []
        heapq.heapify(maxheap)
        for x,y in points:
            dist = -(x**2 + y**2)
            if len(maxheap)>=k:
                heapq.heappushpop(maxheap, [dist,x,y])
            else:
                heapq.heappush(maxheap, [dist,x,y])

        res = []
        while maxheap:
            _, x, y = heapq.heappop(maxheap)
            res.append([x,y])
        return res
        
        
