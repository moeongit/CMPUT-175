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
        '''
        Initializes the game
        '''
        self.board = Board(width, height, obstacle_positions)
        self.players = []
        self.current_turn = 0
        self.phase = 1
        self.goats_per_player = [GOATS_PER_PLAYER, GOATS_PER_PLAYER]
        self.turn = 0  # Add this line to define and set the initial value of the `turn` attribute
        self.current_player = 0


    def __str__(self) -> str:
        board = str(self.board)
        current_player = str(self.current_player)
        phase = str(self.phase)
        turn = str(self.turn)
        # blocked_goats = str(self.get_goats_blocked(self.current_player))
        return f"{board}\nPlayers: {current_player}\nPhase: {phase}\nPlayer whose turn it is: {turn}"


    def get_phase(self) -> int:
        '''Returns the game phase'''
        return self.phase


    def get_turn(self) -> int:
        '''Returns the index of the player whose turn it is'''
        return self.turn


    def get_current_player(self) -> Player:
        '''Returns the current player'''
        return self.players[self.turn]

    
    def get_goats_blocked(self, player):
        goats_blocked = 0
        for goat in player.goats:
            if self.board.check_goat_blocked(goat):
                goats_blocked += 1
        return goats_blocked



    def get_goats_per_player(self, player_index: int) -> int:
        '''
        Returns the number of goats for the player at the given index
        '''
        if player_index < 0 or player_index >= len(self.players):
            return -1
        
        player_goats = 0
        for goat_count in self.goats_per_player:
            if self.players.index(player_index) % 2 == self.goats_per_player.index(goat_count):
                player_goats = goat_count
        
        return player_goats



    def set_phase(self, phase: int) -> None:
        '''Sets the game phase'''
        self.phase = phase


    def set_turn(self, turn: int) -> None:
        '''Sets the game turn'''
        self.turn = turn % len(self.players)



    def add_player(self, player_index: int) -> Player:
        if len(self.players) >= 2:
            raise ValueError("The game already has two players.")
        player = Player(player_index)
        self.players.append(player)
        return player



    def add_goat(self, row: int, column: str) -> None:
        '''Add goat to stack in given location (row, column).'''
        # Check if the given column is valid
        if column not in VALID_COLUMNS:
            raise ValueError(f"Invalid column '{column}'")

        # Get the corresponding column index
        col_index = VALID_COLUMNS.index(column)

        # Check if the given row and column indices are within bounds
        if row < 0 or row >= self.board.num_rows() or col_index < 0 or col_index > self.board.num_cols():
            raise ValueError(f"Invalid goat position ({row}, {column})")

        # Check if the maximum number of goats per player has been reached
        if self.goats_per_player[self.turn] >= GOATS_PER_PLAYER:
            raise ValueError(f"Player {self.turn} has reached the maximum number of goats")

        # Check if the starting position is valid for the current game phase
        if self.phase == 1 and (row, col_index) not in [(0, 3), (0, 4), (1, 4)]:
            raise ValueError("Goat must be placed in one of the starting positions in phase 1")

        # Check if there is already a goat in the given position
        if self.board.get_cell(row, col_index) is not None:
            raise ValueError(f"A goat already exists in position ({row}, {column})")

        # Add the goat to the board and update the count for the current player
        self.board.set_cell(row, col_index, Goat(self.turn))
        self.goats_per_player[self.turn] += 1


    def move_sideways(self, move):
        '''Executes sideways move if valid'''
        player = self.get_current_player()
        goat = player.get_selected_goat()
        column = move[0][1]
        current_row, current_col = goat.get_position()

        if column == current_col:
            print("Error: Cannot move goat to its current column")
            return False

        if column not in VALID_COLUMNS:
            print("Error: Invalid column")
            return False

        if abs(VALID_COLUMNS.index(column) - VALID_COLUMNS.index(current_col)) > SIDE_JUMP_SIZE:
            print("Error: Cannot move goat more than 1 column at a time")
            return False

        # Check if the move is blocked by another goat
        if self.board.is_blocked_by_goat(goat, move):
            print("Error: Goat is blocked by another goat")
            return False

        # Check if the move is blocked by an obstacle
        if self.board.is_blocked_by_obstacle(current_row, current_col, column):
            print("Error: Goat is blocked by an obstacle")
            return False

        # Move the goat
        goat.move_to(column, current_row)

        # Update the board
        self.board.update_board()
        return True


    def move_forward(self, move, dice_outcome):
        '''
        Executes forward move if valid
        '''
        if self.current_turn != move[0]:
            raise ValueError("It's not this player's turn.")
        if dice_outcome not in range(1, 4):
            raise ValueError("The dice outcome must be between 1 and 3.")
        player_goats = self.board.get_player_goats(move[0])
        goat = player_goats[move[1]]
        if goat.is_blocked():
            raise ValueError("This goat is blocked and cannot be moved.")
        new_row = goat.get_row() - (dice_outcome * FORWARD_JUMP_SIZE)
        new_col_index = VALID_COLUMNS.index(goat.get_column())
        if new_row not in range(self.board.get_height()):
            raise ValueError("The goat cannot be moved to this row.")
        if new_col_index not in range(self.board.get_width()):
            raise ValueError("The goat cannot be moved to this column.")

        new_col = VALID_COLUMNS[new_col_index]

        if self.board.is_location_occupied(new_row, new_col):
            raise ValueError("This location is already occupied by another goat.")
        self.board.move_goat(goat, new_row, new_col)
        if new_row == 0:
            goat.set_status(Goat.STATUS_BLOCKED)
        elif self.board.is_adjacent_to_blocked(goat):
            goat.set_status(Goat.STATUS_BLOCKED)
        else:
            goat.set_status(Goat.STATUS_FREE)
        self.increment_turn()
        self.update_phase()

    def check_row(self, row: int) -> None:
        '''Checks if a row is valid'''

        if row > self._height or row < 0:
            raise ValueError("Invalid row")

    def check_valid_move_format(self, move: List) -> bool:
        '''Checks if the given location is an appropriate list of tuples'''
        if not isinstance(move, list) or len(move) != 2:
            return False
        
        if not all(isinstance(coord, tuple) and len(coord) == 2 for coord in move):
            return False
        
        if not all(isinstance(row, int) and isinstance(col, str) for row, col in move):
            return False
        
        if not all(0 <= row < self.board.height and col in VALID_COLUMNS for row, col in move):
            return False
        
        return True

    def check_nonempty_row(self, row):
        """
        Returns True if there are non-blocked goats in a given row, False otherwise
        """
        for col in range(self.board.width):
            cell = self.board.get_cell(row, col)
            if isinstance(cell, Goat) and not cell.is_blocked():
                return True
        return False

    def check_starting_goat_placement(self, row: int) -> bool:
        '''Checks that goat is not placed in a high stack'''

        # Check if there are any non-blocked goats in the row
        if not self.check_nonempty_row(row):
            return True
        
        # Get the topmost non-blocked goat in the row
        topmost_goat = None
        for goat in self.board.get_row(row):
            if goat is not None and not goat.blocked:
                topmost_goat = goat
        if topmost_goat is None:
            return True
        
        # Check if the topmost goat is at the bottom of the stack
        return topmost_goat == self.board.get_top_goat(topmost_goat.row, topmost_goat.column)

    def check_winner(self) -> bool:
        '''
            Returns whether one player has won by getting 
            the necessary goats to the Destination
        '''
        for player in self.players:
            if len(player.goats_destination) >= WINNING_NUMBER_GOATS:
                return True
        return False

    def check_tie(self) -> bool:
        '''
        Returns whether there is a tie since no player has possible moves
        '''
        for player in self.players:
            if self.get_valid_moves(player):
                return False
        return True

if __name__ == '__main__':

    pass

game = Game(width=9, height=6, obstacle_positions=[(3,"C"), (3,"B"), (4,"A"), (4,"G")])

# Add players
game.add_player("Player 1")
game.add_player("Player 2")

# Print the board
print(game)

# Move a goat
game.move_forward(1, (1,1), (2,1))

# Print the board again to see the changes
print(game)

# Check the winner
winner = game.check_winner()
if winner is not None:
    print(f"{winner} wins!")
else:
    print("No winner yet.")

# Check for a tie
tie = game.check_tie()
if tie:
    print("It's a tie!")
else:
    print("No tie yet.")