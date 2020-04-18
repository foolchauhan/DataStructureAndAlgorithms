import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if stones is None:
            return 0
        heap = []
        for stone in stones:
            heapq.heappush(heap, -1*stone)
            
        while len(heap) > 1:
            first = -1*heapq.heappop(heap)
            second = -1*heapq.heappop(heap)
            if first != second:
                heapq.heappush(heap, -1*abs(first-second))
        return -1*heapq.heappop(heap) if len(heap)==1 else 0            
        
        