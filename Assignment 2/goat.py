class Goat:
    def __init__(self, color, row, col):
        valid_colors = ["WHITE", "BLACK", "RED", "ORANGE", "GREEN"]
        if color not in valid_colors:
            raise ValueError("Invalid color.")
        self.color = color
        self.row = row
        self.column = col

    def __str__(self):
        if self.row == -1 or self.column == -1:
            return "-1"
        col = chr(self.column + ord('A'))
        return col + str(self.row + 1)

    def get_location(self):
        if self.row == -1 or self.column == -1:
            return -1
        return (self.row, self.column)

    def get_row(self):
        return self.row
    
    def get_column(self):
        return self.column
    
    def get_color(self):
        return self.color
    
    def set_location(self, row, column):
        if not isinstance(row, int) or not isinstance(column, str) or len(column) != 1:
            raise TypeError("Row must be an integer and column must be a single character string")
        if row < 1 or row > 6:
            raise ValueError("Row must be between 1 and 6.")
        col = column.upper()
        if col < 'A' or col > 'I':
            raise ValueError("Column must be between A and I.")
        self.row = row - 1
        self.column = ord(col) - ord('A')