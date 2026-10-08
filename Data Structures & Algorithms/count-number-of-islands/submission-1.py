class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid[0])
        cols = len(grid)
        islands = 0
        def dfs(r,c):
            if grid[r][c] != 1:
                return 0
            if r < 0 or c < 0 or r > rows or c > cols:
                return 0
            grid[r][c] = "X"
            islands +=1
            return islands
            
        for r in grid[c]:
            for c in grid:
                if grid[r][c] != 1:
                    return dfs(r+1,c), dfs(r-1,c), dfs(r,c+1), dfs(r,c-1)
                   