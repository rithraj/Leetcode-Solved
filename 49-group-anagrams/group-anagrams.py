class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            charCount = [0] * 26
            for c in word:
                idx = ord(c) - ord('a')
                charCount[idx] += 1
            key = tuple(charCount)
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]
        
        return list(groups.values())
