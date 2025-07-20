class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indeg = [0] * numCourses

        for c, preq in prerequisites:
            adj[preq].append(c)
            indeg[c] += 1
        
        q = deque([i for i in range(numCourses) if indeg[i] == 0])
        ret = []
        while q:
            cur = q.popleft()
            ret.append(cur)
            for nxt in adj[cur]:
                indeg[nxt] -=1
                if indeg[nxt] == 0:
                    q.append(nxt)
        
        if len(ret) == numCourses:
            return ret
        else:
            return []

        

        