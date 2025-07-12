class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        # minutes = [int(time[:2]) * 60 + int(time[3:]) for time in timePoints]
        # minutes.sort()

        # ans = min(minutes[i+1] - minutes[i] for i in range(len(minutes) - 1))

        # return min(ans, 24*60 - minutes[-1] + minutes[0])

        minutes = [False] * (24 * 60)

        for time in timePoints:
            minute = int(time[:2]) * 60 + int(time[3:])
            if minutes[minute] == True:
                return 0
            else:
                minutes[minute] = True
        
        prevIndex = float('inf')
        firstIndex = float('inf')
        lastIndex = float('inf')

        ans = float('inf')

        for i in range(24 * 60):
            if minutes[i]:
                if prevIndex != float('inf'):
                    ans = min(ans, i - prevIndex)
                prevIndex = i
                if firstIndex == float("inf"):
                    firstIndex = i
                lastIndex = i
        
        return min(ans, 24*60 - lastIndex + firstIndex)
        


        
        