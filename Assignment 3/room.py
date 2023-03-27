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
    
    def set_id(self, ID):
        if not isinstance(ID, int):
            raise ValueError("ID must be an integer.")
        self._ID = ID
    
    def generate_random_room_id(self):
        if not self._wormhole:
            raise ValueError("Cannot generate a random ID for a room without a wormhole.")
        new_id = self._ID
        while new_id == self._ID:
            new_id = random.randint(1, 100)
        self._ID = new_id
    
    def get_portal(self):
        return self._portal
    
    def set_portal(self, portal):
        self._portal = portal
    
    def get_wormhole(self):
        return self._wormhole
    
    def set_wormhole(self, wormhole):
        self._wormhole = wormhole
    
    def get_diamond(self):
        return self._diamond
    
    def set_diamond(self, diamond):
        self._diamond = diamond
    
    def get_door(self, direction):
        if direction == "north":
            return self._north
        elif direction == "south":
            return self._south
        elif direction == "east":
            return self._east
        elif direction == "west":
            return self._west
        else:
            raise ValueError("Invalid direction.")
    
    def set_link(self, direction, val):
        if direction == "north":
            self._north = val
        elif direction == "south":
            self._south = val
        elif direction == "east":
            self._east = val
        elif direction == "west":
            self._west = val
        else:
            raise ValueError("Invalid direction.")
    
    def isthere_entrance_exit_door(self):
        if self._ID == "entrance" or self._ID == "exit":
            return True
        else:
            return False
