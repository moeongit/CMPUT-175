class Goat:
    colors = ["WHITE", "BLACK", "RED", "ORANGE", "GREEN"]
    columns = ["A", "B", "C", "D", "E", "F", "G", "H"]
    rows = [1, 2, 3, 4, 5, 6, 7, 8]

    def __init__(self, color):
        if color not in self.colors:
            raise ValueError(f"Invalid color: {color}. Valid colors are {self.colors}")
        self.color = color
        self.row = -1
        self.column = -1

    def __str__(self):
        if self.row == -1:
            return f"{self.color} goat"
        else:
            return f"{self.column}{self.row}"

    def get_row(self):
        return self.row

    def get_column(self):
        return self.column

    def get_color(self):
        return self.color

    def set_row(self, row):
        if row not in self.rows:
            raise ValueError(f"Invalid row: {row}. Valid rows are {self.rows}")
        self.row = row

    def set_column(self, column):
        column = column.upper()
        if column not in self.columns:
            raise ValueError(f"Invalid column: {column}. Valid columns are {self.columns}")
        self.column = column
