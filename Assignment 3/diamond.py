from typing import Optional

class Diamond:
    def __init__(self, diamonds: int = 1):
        self.set_diamonds(diamonds)

    def __str__(self):
        return f"Number of Diamonds: {self.diamonds}"

    def get_diamonds(self) -> int:
        return self.diamonds

    def set_diamonds(self, diamonds: int):
        if diamonds < 0:
            raise ValueError("Number of diamonds cannot be negative.")
        self.diamonds = diamonds