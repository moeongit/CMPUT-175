from goat import Goat

class Player:
    def __init__(self, color):
        self.color = color
        self.goats = []

    def __str__(self):
        code = f"{self.color}\nGoats:\n"
        if len(self.goats) == 0:
            code += "None"
        else:
            for goat in self.goats:
                code += f"{goat.color} {goat.column}{goat.row}\n"
        return code
        
    def add_goat(self, goat):
        self.goats.append(goat)

    def remove_goat(self, goat):
        self.goats.remove(goat)
        
    def get_color(self):
        return self.color
    
    def get_num_goats(self):
        return len(self.goats)