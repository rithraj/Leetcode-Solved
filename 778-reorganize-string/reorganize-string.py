class Solution:
    def reorganizeString(self, s: str) -> str:
        char_count = Counter(s)

        maxHeap = [ [-cnt, char] for char,cnt in char_count.items()]
        heapq.heapify(maxHeap)

        prev = None
        ret = ""
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""

            cnt, char = heapq.heappop(maxHeap)
            ret += char
            cnt += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            
            if cnt != 0:
                prev = [cnt, char]
        return ret
        