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
        Returns: None
        """
        print("\n ", end="")
        for i in range(self.size):
            print("  ", i, end="")
        for i in range(self.size):
            print("\n", i, " ", end="")
            for j in range(self.size):
                print(self.board[i][j], end=" ")
                if (j+1) != self.size:
                    print("|", end=' ')
            if (i+1) != self.size:
                print("\n   -----------", end="")
        print()

    def squareIsEmpty(self, row, col):
        '''
        Checks if a given square is empty, or if it already contains a number 
        greater than 0.
        Inputs:
           row (int) - row index of square to check
           col (int) - column index of square to check
        Returns: True if square is empty; False otherwise
        '''
        return True if self.board[row][col] == 0 else False
        
    def update(self, row, col, num):
        '''
        Assigns the integer, num, to the board at the provided row and column, 
        but only if that square is empty.
        Inputs:
           row (int) - row index of square to update
           col (int) - column index of square to update
           num (int) - entry to place in square
        Returns: True if attempted update was successful; False otherwise
        '''
        if self.squareIsEmpty(row, col):
            self.board[row][col] = num
            return True
        else:
            return False

    def boardFull(self):
        '''
        Checks if the board has any remaining empty squares.
        Inputs: none
        Returns: True if the board has no empty squares (full); False otherwise
        '''
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    return False
        return True

    def isWinner(self):
        '''
        Checks whether the current player has just made a winning move.  In order
        to win, the player must have just completed a line (of 3 squares) that 
        adds up to 15. That line can be horizontal, vertical, or diagonal.
        Inputs: none
        Returns: True if current player has won with their most recent move; 
                 False otherwise
        '''
        for i in range(self.size):
            sum_of_col = 0
            sum_of_row = 0
            for j in range(self.size):
                sum_of_row += self.board[i][j]
                sum_of_col += self.board[j][i]
            if sum_of_row == 15 or sum_of_col == 15:
                return True
        right_diagonal = 0
        left_diagonal = 0
        number = self.size - 1
        for i in range(self.size):
            right_diagonal += self.board[i][number - i]
            left_diagonal += self.board[i][i]
        if left_diagonal == 15 or right_diagonal == 15:
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
                print(f"Player {player}, please enter an odd number (1-9): ", end="")
            else:
                print(f"Player {player}, please enter an even number (2-8): ", end="")
            num = int(input())
            row = int(input("Player {}, please enter a row: ".format(player)))
            col = int(input("Player {}, please enter a column: ".format(player)))
            if board.update(row, col, num):
                break
            else:
                print("That spot is filled. Please select another spot.")
        board.drawBoard()
        if board.isWinner():
            print(f"Player {player} wins. Congratulations!")
            play = input("Do you want to play another game? (Y/N): ")
            if play.lower() == "y":
                board = NumTicTacToe()
            else:
                print("Thanks for playing TicTacToe.") 