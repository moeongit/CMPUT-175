from stack import Stack
from goat import Goat

class Board:
    columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    
    def __init__(self, width, height, obstacle_positions):
        self.width = width
        self.height = height
        self.board = [[Stack() for _ in range(width)] for _ in range(height)]
        for r, c in obstacle_positions:
            self.check_row(r)
            self.check_column(c)
            self.board[r-1][self.columns.index(c)].push('X')
    
    def check_row(self, row):
        if not 1 <= row <= self.height:
            raise Exception(f"Invalid row: {row}")
    
    def check_column(self, column):
        if column not in self.columns:
            raise Exception(f"Invalid column: {column}")
    
    def check_obstacle_positions(self, obstacle_positions):
        for r, c in obstacle_positions:
            self.check_row(r)
            self.check_column(c)
    
    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
    
    def get_board(self):
        return self.board
    
    def __str__(self):
        column_header = '   ' + '   '.join(self.columns)
        row_separator = '+---' * self.width + '+'
        output = [column_header, row_separator]
        for r in range(self.height):
            row = str(r+1) + ' |'
            for c in range(self.width):
                stack = self.board[r][c]
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
