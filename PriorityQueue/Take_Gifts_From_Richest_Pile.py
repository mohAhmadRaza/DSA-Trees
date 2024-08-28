class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        negative_gifts = [-elem for elem in gifts]
        heapq.heapify(negative_gifts)  # Converts the list into a heap

        
        for i in range(k):
            currGift = -heapq.heappop(negative_gifts)
            power = math.floor(pow(currGift, 0.5))
            heapq.heappush(negative_gifts, -power)
        
        return sum(negative_gifts)*-1
        
