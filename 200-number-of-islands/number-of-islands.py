class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        m = len(grid)
        n = len(grid[0])
        count = 0
        def dfs(i, j):
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            stack = []
            stack.append((i,j))
            while stack:
                i,j = stack.pop()
                for dx,dy in directions:
                    if i + dx >= 0 and i + dx < m and j + dy >= 0 and j + dy < n and grid[i+dx][j+dy] == "1" and (i+dx, j + dy) not in visited:
                        stack.append((i+dx, j+dy))
                        visited.add((i+dx,j+dy))
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i,j)
                    count += 1
        return count