class NumTicTacToe:
    def __init__(self):
        '''
        Initializes an empty Numerical Tic Tac Toe board.
        Inputs: none
        Returns: None
        '''       
        self.board = [] # list of lists, where each internal list represents a row
        self.size = 3   # number of columns and rows of board
        
        # populate the empty squares in board with 0
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(0)
            self.board.append(row)

    def drawBoard(self):
        """
        Displays the current state of board, formatted with colum and row
        indicies shown.
        Inputs: none
        :return: none
        """
        print("\n ", end="")
        for i in range(self.size):
            print("  ", i, end="")
        for i in range(self.size):
            print("\n", i, " ", end="")
            for j in range(self.size):
                print(self.board[i][j], end=" ")
                if (j + 1) != self.size:
                    print("|", end=' ')
            if (i + 1) != self.size:
                print("\n   -----------", end="")
        print()

    def squareIsEmpty(self, row, col):
        return True if self.board[row][col] == 0 else False

    def update(self, row, col, num):
        if self.squareIsEmpty(row, col):
            self.board[row][col] = num
            return True
        return False

    def boardFull(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    return False
        return True

    def isWinner(self):
        for i in range(self.size):
            rowSum = 0
            colSum = 0
            for j in range(self.size):
                rowSum += self.board[i][j]
                colSum += self.board[j][i]
            if rowSum == 15 or colSum == 15:
                return True
        lDiag = 0
        rDiag = 0
        n = self.size - 1
        for i in range(self.size):
            lDiag += self.board[i][i]
            rDiag += self.bard[i][n - i]
        if lDiag == 15 or rDiag == 15:
            return True
        return False

if __name__ == "__main__":
    board = NumTicTacToe()
    board.drawBoard()
    player = 0
    while not board.isWinner() and not board.boardFull():
        player = (player % 2) + 1
        while True:
            if player == 1:
                print("Player ", player, ", please enter an odd number (1-9): ", end="")
            else:
                print("Player ", player, ", please enter an even number (2-8): ", end="")
            num = int(input())
            row = int(input("Player {} - please enter a row: ".format(player)))
            col = int(input("Player {} - please enter a column: ".format(player)))
            if board.update(row, col, num):
                break
            else:
                print("That spot is filled. Please select another spot.")
        board.drawBoard()
        if board.isWinner():
            print(f"Player {player} wins. Congratulations!")
            choice = input("Do you want to play another game? (Y/N): ")
            if choice.lower() == "y":
                board = NumTicTacToe()
            else:
                print("Thanks for playing TicTacToe.") 