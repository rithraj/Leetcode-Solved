class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        visited = set()

        def dfs(i, j):
            stack = []
            visited.add((i,j))
            stack.append((i,j))
            while stack:
                x,y = stack.pop()
                for dx, dy in directions:
                    r, c = dx + x, dy + y
                    if (r,c) not in visited and 0<=r<rows and 0<=c<cols and grid[r][c] == "1":
                        stack.append((r,c))
                        visited.add((r,c))

        count = 0
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and 0<=r<rows and 0<=c<cols and grid[r][c] == "1":
                    dfs(r,c)
                    count += 1


        return count
