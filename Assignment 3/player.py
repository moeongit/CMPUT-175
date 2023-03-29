# Author: Mohammed Al Robiay
# Collaborators/References: None

class Player:
    def __init__(self, player_id: int):
        self._player_id = player_id
        self._position = None
        self._diamonds = 0
        self._path = []

    def __str__(self):
        return f"Player {self._player_id}. Diamond count: {self._diamonds}"

    def get_position(self):
        return self._position

    def set_position(self, id: int):
        if id > 25 or id < 1:
            raise ValueError("ID is out of range")
        self._position = id

    def get_player_id(self):
        return self._player_id

    def get_diamonds(self):
        return self._diamonds

    def set_diamonds(self, count: int):
        self._diamonds = count

    def print_path(self):
        path_str = " -> ".join([f"{room_id} -> {door_id}" for room_id, door_id in self._path])
        print(path_str)

    def add_to_path(self, room_id: int, door_id: str):
        self._path.append((room_id, door_id))

    def move(self, room_id: int):
        self.set_position(room_id)
