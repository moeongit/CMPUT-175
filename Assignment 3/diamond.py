# Author: Mohammed Al Robiay
# Collaborators/References: None

class Diamond:
    def __init__(self, diamonds: int = 1):
        if diamonds < 0:
            raise ValueError("Number of diamonds cannot be negative")
        self._diamonds = diamonds

    def __str__(self):
        return f"Number of Diamonds: {self._diamonds}"

    def get_diamonds(self):
        return self._diamonds

    def set_diamonds(self, diamonds: int):
        if diamonds < 0:
            raise ValueError("Number of diamonds cannot be negative")
        self._diamonds = diamonds