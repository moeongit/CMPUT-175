from board import Board
from player import Player


class Game:
    def __init__(self, width, height, obstacle_positions):
        self.board = Board(width, height, obstacle_positions)
        self.players = []
        self.phase = 1
        self.turn = 0

    def __str__(self):
        header = "   " + "   ".join(chr(i + 65) for i in range(self.board.width))
        rows = []
        for i in range(self.board.height):
            row = []
            for j in range(self.board.width):
                cell = self.board.get_cell(i, j)
                if cell.is_obstacle():
                    row.append("| X")
                elif cell.is_goat():
                    row.append("| " + cell.get_stack_string())
                else:
                    row.append("|  ")
            row.append("| " + str(i + 1))
            rows.append("".join(row))
            rows.append(" +" + "---+" * self.board.width)
        rows.append("".join(["  " + c for c in header]))
        rows.append("")
        players_str = "Players: " + ", ".join(str(p) for p in self.players)
        phase_str = "Phase: " + str(self.phase)
        turn_str = "Player whose turn it is: " + str(self.get_current_player())
        return "\n".join(rows) + "\n" + players_str + "\n" + phase_str + "\n" + turn_str + "\n"

    def get_phase(self):
        return self.phase

    def get_turn(self):
        return self.turn

    def get_current_player(self):
        return self.players[self.turn]

    def get_goats_blocked(self, player):
        return self.board.get_goats_blocked(player.color)

    def get_goats_per_player(self):
        return self.board.get_goats_per_player()

    def set_phase(self, phase):
        self.phase = phase

    def set_turn(self, turn):
        self.turn = turn

    def add_player(self, player):
        self.players.append(player)

    def add_goat(self, row, column):
        self.board.add_goat(row, column, self.get_current_player().color)

    def move_sideways(self, move):
        self.check_valid_move_format(move)
        row1, col1 = move[0]
        row2, col2 = move[1]
        if row1 != row2 or abs(col1 - col2) != 1:
            raise Exception("Invalid sideways move")
        self.board.move_goat(row1, col1, row2, col2)

    def move_forward(self, move, dice_outcome):
        self.check_valid_move_format(move)
        row1, col1 = move[0]
        row2, col2 = move[1]
        if row1 != row2 - dice_outcome or abs(col1 - col2) != 1:
            raise Exception("Invalid forward move")
        self.board.move_goat(row1, col1, row2, col2)

    def check_row(self, row):
        if row < 1 or row > self.board.height:
            raise Exception("Invalid row")

    def check_valid_move_format(self, move):
        if not isinstance(move, list) or len(move) != 2:
            raise Exception("Invalid move format")
        for row, col in move:
            self.check_row(row)
            if col < 0 or col >= self.board.width:
                raise Exception("Invalid column")

    def check_nonempty_row(self, row):
        return self.board.check_nonempty_row(row)

    def check_starting_goat_placement(self, row):
        # check if row is valid
        self.check_row(row)
        # get stack with minimum height
        min_stack_height = min([len(stack) for stack in self.board.grid[row-1] if stack is not None])
        # check if stack in the given row has a lower or equal height to min_stack_height
        if len(self.board.grid[row-1][-1]) <= min_stack_height:
            return True
        else:
            return False
