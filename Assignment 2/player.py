class Player:
    def __init__(self, color):
        self.color = color
        self.goats = []

    def add_goat(self, goat):
        if goat.color != self.color:
            raise ValueError("Goat color does not match player color")
        self.goats.append(goat)

    def remove_goat(self, goat):
        if goat not in self.goats:
            raise ValueError("Goat not found in player's goats")
        self.goats.remove(goat)

    def get_color(self):
        return self.color

    def get_num_goats(self):
        return len(self.goats)

    def __str__(self):
        output = f"{self.color}\nGoats:\n"
        for goat in self.goats:
            output += f"{goat}\n"
        return output
