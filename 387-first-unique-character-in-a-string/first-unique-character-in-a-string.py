class Solution:
    def firstUniqChar(self, s: str) -> int:
        pos = {}

        for i in range(len(s)):
            if s[i] in pos:
                pos[s[i]].append(i)
            else:
                pos[s[i]] = [i]

        lowest = float('inf')
        for k,v in pos.items():
            if len(v) > 1:
                continue
            else:
                lowest = min(lowest, v[0])
        
        return lowest if type(lowest) is int else -1
        