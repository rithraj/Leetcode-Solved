class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)

        g_pointer = 0
        s_pointer = 0
        count = 0

        while g_pointer < len(g) and s_pointer < len(s):
            if g[g_pointer] <= s[s_pointer]:
                g_pointer += 1
                s_pointer += 1
                count += 1
            else:
                s_pointer += 1
        
        return count

        