from goat import Goat

class Player:
    def __init__(self, color):
        self.color = color
        self.goats = []

    def __str__(self):
        output = f"{self.color}\nGoats:\n"
        if len(self.goats) == 0:
            output += "None"
        else:
            for goat in self.goats:
                output += f"{goat.color} {goat.column}{goat.row}\n"
        return output
        
    def add_goat(self, goat):
        if goat.color != self.color:
            raise ValueError(f"Goat color '{goat.color}' does not match player color '{self.color}'")
        if goat in self.goats:
            raise ValueError("Goat already exists in player's list")
        self.goats.append(goat)

    def remove_goat(self, goat):
        if goat not in self.goats:
            raise ValueError("Goat not found in player's goats")
        self.goats.remove(goat)
        
    def get_color(self):
        return self.color
    
    def get_num_goats(self):
        return len(self.goats)