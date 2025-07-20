class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjacency = {}
        indeg = [0] * numCourses
        for c in range(numCourses):
            adjacency[c] = []
        for c, req in prerequisites:
                adjacency[req].append(c)
                indeg[c] += 1

        q = deque([i for i in range(numCourses) if indeg[i] == 0])
        taken = 0
        while q:
            cur = q.popleft()
            taken += 1

            for nxt in adjacency[cur]:
                indeg[nxt] -= 1
                if indeg[nxt] == 0:
                    q.append(nxt)
        return taken == numCourses
