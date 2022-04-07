class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        count = 0
        
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        boundry = lambda i,j : 0 <= i < m and 0 <= j < n
        isValid = lambda i,j : grid[i][j] == '1'
        
        def dfs(i,j):
            grid[i][j] = '#'
            for d in directions:    
                newX = d[0] + i
                newY = d[1] + j
                if boundry(newX,newY):
                    if isValid(newX,newY):                        
                        dfs(newX,newY)
        
        for i in range(m):
            for j in range(n):
                if isValid(i,j):
                    count += 1
                    dfs(i,j)
        
        return count