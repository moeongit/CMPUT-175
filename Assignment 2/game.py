# Author: Mohammed Al Robiay
# Collaborators/References: None
#----------------------------------------------------
# Game implementation
#----------------------------------------------------

from typing import List
from goat import Goat
from board import Board
from player import Player

GOATS_PER_PLAYER = 4
WINNING_NUMBER_GOATS = 3
VALID_COLUMNS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
SIDE_JUMP_SIZE = 1
FORWARD_JUMP_SIZE = 1

class Game:
    '''
    Represents the Goat Race game
    '''
    ################################################
    #
    # The following methods MUST be in your solution
    # 
    ################################################
    def __init__(self, width: int, height: int, obstacle_positions: List = []):
        self.width = width
        self.height = height
        self.obstacle_positions = obstacle_positions
        self.board = Board(width, height, obstacle_positions)
        self.players = []
        self.turn = 0
        self.phase = 1

    def __str__(self):
        board_str = str(self.board)
        players_str = 'Players: ' + ', '.join([player.color for player in self.players])
        phase_str = f"Phase: {self.phase}"
        turn_str = f"Player whose turn it is: {self.players[self.turn].color if self.turn is not None else 'UNDEFINED'}"

        return f"{board_str}\n\n{players_str}\n{phase_str}\n{turn_str}"


    def get_phase(self):
        return self.phase

    def get_turn(self):
        return self.turn

    def get_current_player(self):
        return self.players[self.turn]

    def get_goats_blocked(self, player: Player):
        blocked_goats = 0
        for goat in player.goats:
            row, col = goat.get_location()
            if row != -1:
                stack = self.board.board[row][col]
                if stack.size() > 1:
                    blocked_goats += 1
        return blocked_goats

    def get_goats_per_player(self):
        return [player.get_num_goats() for player in self.players]

    def set_phase(self, phase: int):
        self.phase = phase

    def set_turn(self, turn: int):
        self.turn = turn

    def add_player(self, player: Player):
        self.players.append(player)

    def add_goat(self, row: int, column: str) -> None:
        '''Add goat to stack in given location (row, column).'''

        self.board.check_row(row)
        self.board.check_column(column)

        if not self.check_starting_goat_placement(row):
            raise Exception(f"Goat cannot be placed on row {row}.")

        goat = Goat(self.get_current_player().color, row - 1, self.board.columns.index(column))
        self.board.get_board()[row - 1][self.board.columns.index(column)].push(goat)
        self.get_current_player().add_goat(goat)

    def move_sideways(self, move):
        '''
        Executes sideways move if valid
        '''
        self.check_valid_move_format(move)
        initial_loc, final_loc = move

        self.check_location(initial_loc)
        self.check_location(final_loc)

        initial_row, initial_col = initial_loc
        final_row, final_col = final_loc

        self.check_same_color(initial_row, initial_col)

        if final_col == initial_col:
            raise Exception("Cannot move goat to the same column.")

        self.board.check_column(final_col)
        self.board.check_row(final_row)

        initial_stack = self.board.get_board()[initial_row][self.board.columns.index(initial_col)]
        final_stack = self.board.get_board()[final_row][self.board.columns.index(final_col)]

        if not initial_stack.is_empty():
            goat = initial_stack.peek()
            if isinstance(goat, Goat):
                if final_stack.is_empty():
                    final_stack.push(initial_stack.pop())
                else:
                    raise Exception("Cannot move goat to a non-empty stack.")
            else:
                raise Exception("Cannot move goat from an empty stack.")
        else:
            raise Exception("Cannot move goat from an empty stack.")


    def move_forward(self, move, dice_outcome):
        '''Executes forward move if valid '''

        # Check that the move is valid
        self.check_valid_move_format(move)

        # Get the starting and ending locations of the move
        start_row, start_col = move[0]
        end_row, end_col = move[1]

        # Check that the move is forward
        if self.get_current_player().get_color() == "WHITE":
            if end_row <= start_row:
                raise Exception("Invalid move. Goats can only move forward.")
        else:
            if end_row >= start_row:
                raise Exception("Invalid move. Goats can only move forward.")

        # Check that the move is within the bounds of the board
        self.check_location((end_row, end_col))

        # Check that the goat being moved is of the current player's color
        goat = self.board.get_board()[start_row - 1][self.board.columns.index(start_col)].peek()
        if goat.get_color() != self.get_current_player().get_color():
            raise Exception("Invalid move. You can only move your own goats.")

        # Check that the destination stack is not blocked
        if self.board.get_board()[end_row - 1][self.board.columns.index(end_col)].size() >= 5:
            raise Exception("Invalid move. Destination stack is blocked.")

        # Check that the goat is jumping over other goats or empty stacks
        jump_size = abs(end_row - start_row)
        if jump_size == FORWARD_JUMP_SIZE:
            if not self.check_jump(end_row, end_col):
                raise Exception("Invalid move. You can only jump over your opponent's goats.")
        elif jump_size == 2*FORWARD_JUMP_SIZE:
            mid_row = (start_row + end_row) // 2
            mid_col = start_col
            if start_col == end_col:
                goat = self.board.get_board()[mid_row - 1][self.board.columns.index(mid_col)].peek()
                if goat is None or goat.get_color() == self.get_current_player().get_color():
                    raise Exception("Invalid move. You can only jump over your opponent's goats.")
            else:
                mid_col = self.board.columns[start_col < end_col and start_col or end_col]
                goat = self.board.get_board()[mid_row - 1][self.board.columns.index(mid_col)].peek()
                if goat is None or goat.get_color() == self.get_current_player().get_color():
                    raise Exception("Invalid move. You can only jump over your opponent's goats.")

        # Move the goat to the destination stack
        goat = self.board.get_board()[start_row - 1][self.board.columns.index(start_col)].pop()
        self.board.get_board()[end_row - 1][self.board.columns.index(end_col)].push(goat)

        # Check for winner or tie
        if self.check_winner():
            self.set_phase(3)
        elif self.check_tie():
            self.set_phase(4)
        else:
            # Update turn if the goat reached destination stack or the dice outcome was even
            if end_row == self.height and self.get_current_player().get_color() == "WHITE":
                self.set_turn((self.get_turn() + 1) % len(self.players))
            elif end_row == 1 and self.get_current_player().get_color() == "BLACK":
                self.set_turn((self.get_turn() + 1) % len(self.players))
            elif dice_outcome % 2 == 0:
                self.set_turn((self.get_turn() + 1) % len(self.players))


    def check_row(self, row: int):
        if not 1 <= row <= self.height:
            raise Exception(f"Invalid row: {row}.")

    def check_valid_move_format(self, move: List):
        if len(move) != 2:
            raise Exception("Invalid move format. Move should contain 2 tuples.")
        for loc in move:
            if not isinstance(loc, tuple) or len(loc) != 2:
                raise Exception("Invalid move format. Each location must be a tuple with 2 elements.")


    def check_nonempty_row(self, row):
        """
        Returns True if there are non-blocked goats in the given row, otherwise False.
        """
        for col in range(self.board.get_width()):
            stack = self.board.get_board()[row - 1][col]
            if not stack.is_empty():
                top_item = stack.peek()
                if isinstance(top_item, Goat) and top_item.get_color() == self.get_current_player().get_color():
                    return True
        return False



    def check_starting_goat_placement(self, row):
        if not 1 <= row <= self.height:
            raise Exception(f"Invalid row: {row}.")
        
        row -= 1
        min_height = min(stack.size() for stack in self.board.board[row])
        
        for j in range(self.width):
            stack = self.board.board[row][j]
            if stack.size() == min_height:
                return True

        return False




    def check_winner(self):
        for player in self.players:
            destination_goats = 0
            for goat in player.goats:
                row, col = goat.get_location()
                if row == self.height - 1:
                    destination_goats += 1
            if destination_goats >= WINNING_NUMBER_GOATS:
                return True
        return False

    def check_tie(self) -> bool:
        '''
            Returns whether there is a tie since 
            no player has possible moves
        '''
        if self.get_phase() != 2:
            return False
        for player in self.players:
            if self.get_goats_blocked(player) < GOATS_PER_PLAYER:
                return False
        return True

if __name__ == '__main__':

    pass