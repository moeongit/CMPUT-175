class Player:
    def __init__(self, color):
        valid_colors = ["WHITE", "BLACK", "RED", "ORANGE", "GREEN"]
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
        str = f"{self.color}\nGoats:\n"
        for goat in self.goats:
            str += f"{goat}\n"
        return str

p1 = Player("WHITE")
print(p1.get_color())  # Output: WHITE

g1 = Goat("WHITE")
g2 = Goat("WHITE")
g3 = Goat("WHITE")
p1.add_goat(g1)
p1.add_goat(g2)
p1.add_goat(g3)
print(p1.get_num_goats())  # Output: 3

p1.remove_goat(g2)
print(p1.get_num_goats())  # Output: 2

print(p1)  # Output: WHITE
           #         Goats:
           #         WHITE A1
           #         WHITE E1
