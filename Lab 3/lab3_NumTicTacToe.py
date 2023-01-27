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
        # print row indices
        print("\n ", end="")
        for i in range(self.size):
            print("  ", i, end="")
        # print board cells
        for i in range(self.size):
            # print column index
            print("\n", i, " ", end="")
            for j in range(self.size):
                # print cell value
                print(self.board[i][j], end=" ")
                if (j + 1) != self.size:
                    # print column separator
                    print("|", end=' ')
            if (i + 1) != self.size:
                # print row separator
                print("\n   -----------", end="")
        print()

    def squareIsEmpty(self, row, col):
        return True if self.board[row][col] == 0 else False

    def update(self, row, col, num):
        # check if square is empty
        if self.squareIsEmpty(row, col):
            # set square to num
            self.board[row][col] = num
            # return true to indicate success
            return True
        # return false to indicate failure
        return False

    def boardFull(self):
        # for each row
        for i in range(self.size):
            # for each column
            for j in range(self.size):
                # check if cell is empty
                if self.board[i][j] == 0:
                    # return false to indicate board is not full
                    return False
        # return True to indicate board if full
        return True

    def isWinner(self):
        # row & column checks
        for i in range(self.size):
            rowSum = 0
            colSum = 0
            for j in range(self.size):
                rowSum += self.board[i][j]
                colSum += self.board[j][i]
            if rowSum == 15 or colSum == 15:
                return True
        # diagonal checks
        lDiag = 0
        rDiag = 0
        n = self.size - 1
        for i in range(self.size):
            lDiag += self.board[i][i]
            rDiag += self.board[i][n - i]
        if lDiag == 15 or rDiag == 15:
            return True
        # return false to indicate not a winner
        return False


if __name__ == "__main__":
    board = NumTicTacToe()
    # print("Contents of board attribute when object first created")
    # print(myBoard.board)

    # draw board
    board.drawBoard()
    # player identifier
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
                print("That position is not empty. Choose another spot please.")
        board.drawBoard()
        if board.isWinner():
            print("Player ", player, " wins. Congrats!")
            choice = input("Do you want to play another game? (Y/N): ")
            if choice.lower() == "y":
                board = NumTicTacToe()
            else:
                print("Thank you for playing.") 