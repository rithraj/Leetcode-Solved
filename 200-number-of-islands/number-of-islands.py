class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        visited = set()
        count = 0

        def dfs(i, j):
            stack = []
            visited.add((i, j))
            stack.append((i,j))

            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            while stack:
                r0, c0 = stack.pop()
                for dr, dc in directions:
                    r, c = r0 + dr, c0 + dc
                    if (r < len(grid) and r >=0 and c < len(grid[0]) and c >= 0 and grid[r][c] == "1" and (r,c) not in visited):
                        stack.append((r,c))
                        visited.add((r,c))


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i, j)
                    count += 1
        
        return count
        