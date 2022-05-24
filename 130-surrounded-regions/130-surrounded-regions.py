class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        
        if m <= 1 or n <= 1:
            return
        
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        isBoundary = lambda x, y : -1 < x < m and -1 < y < n
        isValid = lambda x, y : board[x][y] == "O"
        
        def dfs(i, j):
            board[i][j] = "#"
            for x, y in directions:
                newX = x + i
                newY = y + j
                
                if isBoundary(newX, newY):
                    if isValid(newX, newY):
                        dfs(newX, newY)
                        
        for i in range(0, m, m-1):
            for j in range(0, n):
                if board[i][j] == "O":
                    dfs(i,j)
                    
        for j in range(0, n, n-1):
            for i in range(0, m):
                if board[i][j] == "O":
                    dfs(i,j)
                        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "#":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"