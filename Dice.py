import random

class Dice:
    def __init__(self, sides=6):
        self.sides = sides
        self.value = None

    def roll(self):
        self.value = random.randint(1, self.sides)