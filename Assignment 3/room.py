# Author: Mohammed Al Robiay
# Collaborators/References: None

import random
from diamond import Diamond

class Room:
    def __init__(self, ID=None, north=None, south=None, east=None, west=None, portal=False, wormhole=False, diamond=None):
        self._ID = ID
        self._north = north
        self._south = south
        self._east = east
        self._west = west
        self._portal = portal
        self._wormhole = wormhole
        self._diamond = diamond

    def get_id(self):
        return self._ID

    def set_id(self, ID: int):
        if not isinstance(ID, int):
            raise ValueError("ID should be an integer")
        self._ID = ID

    def generate_random_room_id(self):
        if not self._wormhole:
            raise ValueError("This room doesn't have a wormhole inside")
        random_id = self._ID
        while random_id == self._ID:
            random_id = random.randint(1, 25)
        return random_id

    def get_portal(self):
        return self._portal

    def set_portal(self, portal: bool):
        self._portal = portal

    def get_wormhole(self):
        return self._wormhole

    def set_wormhole(self, wormhole: bool):
        self._wormhole = wormhole

    def get_diamond(self):
        return self._diamond

    def set_diamond(self, diamond: Diamond):
        self._diamond = diamond

    def get_door(self, direction: str):
        if direction.lower() == "north":
            return self._north
        elif direction.lower() == "south":
            return self._south
        elif direction.lower() == "east":
            return self._east
        elif direction.lower() == "west":
            return self._west
        else:
            raise ValueError("Invalid direction")

    def set_link(self, direction: str, val):
        if direction.lower() == "north":
            self._north = val
        elif direction.lower() == "south":
            self._south = val
        elif direction.lower() == "east":
            self._east = val
        elif direction.lower() == "west":
            self._west = val
        else:
            raise ValueError("Invalid direction")

    def is_there_entrance_exit_door(self):
        doors = [self._north, self._south, self._east, self._west]
        for door in doors:
            if door == "entrance":
                return "entrance"
            if door == "exit":
                return "exit"
        return None