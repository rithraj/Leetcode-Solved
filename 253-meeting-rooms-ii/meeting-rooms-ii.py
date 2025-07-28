class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        min_heap = []

        for interval in intervals:
            start, end = interval
            if min_heap and start >= min_heap[0]:
                heapq.heappop(min_heap)
            
            heapq.heappush(min_heap, end)
        
        return len(min_heap)