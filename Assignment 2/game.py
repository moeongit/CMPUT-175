#----------------------------------------------------
# Game implementation
#----------------------------------------------------
# Author: Mohammed Al Robiay
# Collaborators/References: None

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
        self.goats = []
        self.phase = 1
        self.turn = 0
        self.goats_blocked = [0, 0]


    def __str__(self) -> str:
        board = str(self.board)        
        players_str = "Players: " + ", ".join([player.color for player in self.players]) 
        phase_str = str(self.phase) 
        turn_str = "Player whose turn it is: " + str(self.players[self.turn].color) if self.turn is not None else "UNDEFINED"
        return f"{board}\n{players_str}\nPhase: {phase_str}\n{turn_str}"


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
        """
        Returns the number of goats that cannot jump for the given player.
        """
        blocked = 0
        for goat in player.goats:
            if goat.blocked:
                blocked += 1
        return blocked


    def get_goats_per_player(self) -> List[int]:
        '''Return a list that contains the number of goats per player.'''
        goats_per_player = [len(player.goats) for player in self.players]
        return goats_per_player


    def set_phase(self, phase: int) -> None:
        '''Sets the game phase'''
        self.phase = phase


    def set_turn(self, turn: int) -> None:
        '''Sets the game turn'''
        self.turn = turn % len(self.players)


    def add_player(self, player: Player) -> None:
        '''Adds a player to the list of players in the game'''
        self.players.append(player)


    def add_goat(self, row: int, column: str) -> None:
        '''Add goat to stack in given location (row, column).'''
        # Check if the given location is valid
        if row < 0 or row > self.rows or column not in self.columns:
            raise Exception(f"Invalid location: ({row}, {column})")
            
        # Check if the stack at the given location is not full
        if len(self.board[row][column]) >= self.stack_size:
            raise Exception(f"Cannot add goat, stack at ({row}, {column}) is already full.")
            
        # Add a goat to the stack at the given location
        self.board[row][column].append("goat")



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

        goat.move_to(column, current_row)
        self.board.update_board()
        
        return True
    

    def move_forward(self, move, dice_outcome):
        '''
        Executes forward move if valid
        '''
        if self.current_turn != move[0]:
            raise ValueError("It isn't this player's turn yet")
        if dice_outcome not in range(1, 6):
            raise ValueError("The dice outcome must be between 1 and 6")
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
            counter = 0
            for goat in player.goats:
                row, col = goat.get_location()
                if col == "I":
                    counter += 1
                if counter == 3:
                    return player
        return None
    
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
# game = Game(9, 6, [(3,"C"), (3,"B"), (4,"A"), (4,"G")])

# game.add_player(Player("WHITE"))
# player1 = Player("WHITE")
# # game.add_player(Player("BLACK"))
# # game.set_location(Player())
# goat1 = Goat("WHITE", 2, "I")
# goat2 = Goat("WHITE", 3, "I")
# goat3 = Goat("WHITE", 4, "I")

# player1.add_goat(goat1)
# player1.add_goat(goat2)
# player1.add_goat(goat3)
# print(game)
# # Check the winner
# winner = game.check_winner()
# if winner is not None:
#     print(f"{winner} wins!")
# else:
#     print("No winner yet.")
# # Check for a tie
# tie = game.check_tie()
# if tie:
#     print("It's a tie!")
# else:
#     print("No tie yet.")