class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Initialize the min-heap with the first k elements
        min_heap = nums[:k]
        heapq.heapify(min_heap)
        
        # Process the remaining elements
        for num in nums[k:]:
            if num > min_heap[0]:  # If the current num is larger than the smallest in the heap
                heapq.heappushpop(min_heap, num)  # Replace the smallest element
        
        # The root of the min-heap is the kth largest element
        return min_heap[0]
