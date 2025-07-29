class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.grid = [[0] * self.n for i in range(self.n)]

    def checkVertical(self, col: int, player:int):
        count = 0
        for i in range(self.n):
            if self.grid[i][col] == player:
                count += 1
        if count == self.n:
            return player
        else:
            return 0
        
    def checkHorizontal(self, row: int, player: int):
        count = 0
        for i in range(self.n):
            if self.grid[row][i] == player:
                count += 1
        if count == self.n:
            return player
        else:
            return 0
    
    def checkDiagonal(self, row, col, player):
        if row != col and (row + col) != (self.n - 1):
            return 0
        top_down = 0
        for i in range(self.n):
            if self.grid[i][i] == player:
                top_down += 1
        


        bottom_up = 0
        i, j = 0, self.n - 1
        while i < self.n and j >= 0:
            if self.grid[i][j] == player:
                bottom_up += 1
            i += 1
            j -= 1

        
        if top_down == self.n or bottom_up == self.n:
            return player
        else:
            return 0

    def move(self, row: int, col: int, player: int) -> int:
        self.grid[row][col] = player
        h = self.checkHorizontal(row, player)
        v = self.checkVertical(col, player)
        d = self.checkDiagonal(row, col, player)

        if h == player or v == player or d == player:
            return player
        else:
            return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)