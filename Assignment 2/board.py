from stack import Stack
from goat import Goat

class Board:
    columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

    def __init__(self, width, height, obstacle_positions):
        self.width = width
        self.height = height
        self.board = [[Stack() for i in range(int(width))] for j in range(int(height))]
        for i, j in obstacle_positions:
            self.check_row(i)
            self.check_column(j)
            self.board[i-1][self.columns.index(j)].push('X')

    def check_row(self, row):
        if not 1 <= row <= self.height:
            raise Exception(f"Invalid row: {row}.")
    
    def check_column(self, column):
        if column not in self.columns:
            raise Exception(f"Invalid column: {column}.")
    
    def check_obstacle_positions(self, obstacle_positions):
        for i, j in obstacle_positions:
            self.check_row(i)
            self.check_column(j)
    
    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
    
    def get_board(self):
        return self.board
    
    def __str__(self):
        column_header = '      ' + '   '.join(Board.columns)
        row_separator = '  +-' + '-+-'.join(['-'  for i in range(self.width)]) + '-+'

        output = [column_header, row_separator]
        for i in range(self.height):
            row = f"{i+1} |"
            for j in range(self.width):
                stack = self.board[i][j]
                if stack.is_empty():
                    row += '   |'
                else:
                    top_goat = stack.peek()
                    if isinstance(top_goat, Goat):
                        row += f" {top_goat.color[0]} |"
                    else:
                        row += ' X |'
            output.append(row)
            output.append(row_separator)
        return '\n'.join(output)


board = Board(9, 6, [(3, 'B')])

# add 3 goats to the board
board.get_board()[1][1].push(Goat('WHITE', 2, 'B'))

board.get_board()[3][3].push(Goat('BLACK', 2, 'J'))
board.get_board()[5][5].push(Goat('RED', 2, 'I'))

# print the board
print(board)
