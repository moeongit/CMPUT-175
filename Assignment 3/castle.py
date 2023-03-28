# Author: Mohammed Al Robiay
# Collaborators/References: None

from room import Room

class Castle:
    def __init__(self):
        self.rooms = {}

    def add_room(self, room: Room):
        if room.get_id() in self.rooms:
            raise ValueError("Room already exists in the castle")
        self.rooms[room.get_id()] = room

    def get_room(self, id: int):
        if id not in self.rooms:
            raise ValueError("Room not found in the castle")
        return self.rooms[id]

    def change_room(self, id: int, new_room: Room):
        if id > 25 or id < 1:
            raise ValueError("ID is out of range")
        self.rooms[id] = new_room

    def get_entrance_id(self):
        for id, room in self.rooms.items():
            if room.is_there_entrance_exit_door() == "entrance":
                return id
        raise ValueError("Entrance not found")

    def get_exit_id(self):
        
        for id, room in self.rooms.items():
            if room.is_there_entrance_exit_door() == "exit":
                return id
        raise ValueError("Exit not found")

    def get_next_room(self, room_id: int, door: str):
        current_room = self.get_room(room_id)
        next_room = current_room.get_door(door)


        if next_room == "entrance":
            return "entrance"
        if next_room == "exit":
            return "exit"
        if next_room is None:
            print("No room found")
            return current_room.get_id()
        else:
            next_room = self.get_room(next_room)
            next_room_id = next_room.get_id()

        if next_room.get_wormhole():
            
            next_room_id = next_room.generate_random_room_id()
            print("A wormhole devoured you")
        elif next_room.get_portal():
            entrance_id = self.get_entrance_id()
            print("You entered a portal")
            return entrance_id
        return next_room_id