import numpy as np
from Categories import Three_of_a_kind

class Roll:
    def __init__(self, num_dice=5, sides=6):
        self.num_dice = num_dice
        self.sides = sides
        self.dice = np.zeros(num_dice, dtype=int)

        self.categories = {
            'three_of_a_kind': Three_of_a_kind(),
        }

    def roll_all(self):
        self.dice = np.random.randint(1, self.sides + 1, size=self.num_dice)
        print(self.dice)
        self.categories['three_of_a_kind'].check_category(self.dice)
        self.categories['three_of_a_kind'].find_probability(self.dice, rerolls_remaining=2)
        self.categories['three_of_a_kind'].find_score(self.dice)
        self.categories['three_of_a_kind'].find_weight()
        self.categories['three_of_a_kind'].print()

    def roll_selected(self, indices_mask):
        if np.sum(indices_mask) == self.num_dice:
            self.roll_all()
            return

        tmp = self.dice
        self.dice = np.where(np.array(indices_mask) == 1, np.random.randint(1, self.sides + 1, size=self.num_dice), tmp)