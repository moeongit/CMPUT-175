# Author: Mohammed Al Robiay
# Collaborators/References: None

import random

from castle import Castle
from player import Player
from diamond import Diamond
from room import Room

class Game:
    def __init__(self):
        self._castle = None
        self._players = [Player(0), Player(1)]
        self._finished = [False, False]
        self._turn = 0

    def initialize_from_file(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()

        entrance_line = lines.pop(0).strip()
        entrance_room, entrance_door = entrance_line.split(': ')[1].split(', ')
        exit_line = lines.pop(0).strip()
        exit_room, exit_door = exit_line.split(': ')[1].split(', ')
        self._castle = Castle()

        for line in lines:
            line = line.strip().replace(" ","")
            room_id = line.split(':')[0]
            other = line.split(':')[1]
            north, south, east, west, *content = other.split(',')
            room_id = int(room_id)
            diamond = content[0].count('D')            
            portal = 'P' in content[0]
            wormhole = 'W' in content[0]
            room = self.build_room(room_id, diamond, portal, wormhole)
            
            
            room.set_link('north', None if north == '0' else self.try_block(north))            
            room.set_link('south', None if south == '0' else self.try_block(south))            
            room.set_link('east', None if east == '0' else self.try_block(east))            
            room.set_link('west', None if west == '0' else  self.try_block(west))

            if room_id == int(entrance_room):
                room.set_link(self.get_direction(entrance_door), 'entrance')
                for player in self._players:
                    player.set_position(room_id)

            if room_id == int(exit_room):
                room.set_link(self.get_direction(exit_door), 'exit')

            self._castle.add_room(room)

    def get_turn(self):
        return self._turn

    def set_turn(self, turn: int):
        self._turn = turn

    def get_player(self, player_id: int):
        return self._players[player_id]

    def build_room(self, room_id: int, diamond: int, portal: bool, wormhole: bool):
        
        return Room(ID=room_id, north=None, south=None, east=None, west=None, portal=portal, wormhole=wormhole, diamond=Diamond(diamond) if diamond > 0 else None)

    def move(self):
        player = self._players[self._turn]
        room_id = player.get_position()
        room = self._castle.get_room(room_id)
        direction = self.get_direction( input("Please input a direction (North, South, East, West): "))

        if direction not in ['north', 'south', 'east', 'west']:
            raise ValueError("Invalid direction")

        print(f"Player {self._turn + 1} previous room {room_id}")

        next_room_id = self._castle.get_next_room(room_id, direction)
        
        
        if next_room_id == "exit":
            self._finished[self._turn] = True
            print(f"Player {self._turn+1} exited the castle! {direction}")
            next_room_id = self._castle.get_exit_id()
            player.add_to_path(room_id, direction)
            return
        if next_room_id == "entrance":
            next_room_id = self._castle.get_entrance_id()
        
        player.move(next_room_id)
        self.update_diamonds()
        print(f"Player {self._turn + 1}, {direction}, New room {player.get_position()}")
        player.add_to_path(room_id, direction)

    def is_finished(self):
        if all(self._finished):
            for player in self._players:
                player.print_path()
            print(f"Final score is Player {self._players[0].get_player_id()+1}: {self._players[0].get_diamonds()} diamonds, Player {self._players[1].get_player_id()+1}: {self._players[1].get_diamonds()} diamonds! Good Game!")
            return True
        return False

    def update_diamonds(self):
        player = self._players[self._turn]
        room_id = player.get_position()
        room = self._castle.get_room(room_id)
        diamonds = room.get_diamond()
        
        if diamonds is not None:
            
            total_diamonds = player.get_diamonds() + diamonds.get_diamonds()
            player.set_diamonds( total_diamonds)
            print(f"{diamonds} TOTAL: {total_diamonds}")
            room.set_diamond(None)
            

        if room.get_portal():            
            player.clear_path()
            player.set_position(self._castle.get_entrance_id())


    def play(self,filename):
        self.initialize_from_file(filename)

        while not self.is_finished():
            print(f"It's player {self._turn + 1} turn")
            self.move()
            self.set_turn((self._turn + 1) % len(self._players))
            if self._finished[self._turn]:            
                self.set_turn((self._turn + 1) % len(self._players))
    
    def try_block(self,temp):
                try: 
                    return int(temp) 
                except ValueError: 
                    return None
    
    def get_direction(self,chrs):
        if chrs[0].lower() == 'w':
            return 'west'
        elif chrs[0].lower() == 'n':
            return 'north'
        elif chrs[0].lower() == 's':
            return 'south'
        elif chrs[0].lower() == 'e':
            return 'east'
        else:
            return None