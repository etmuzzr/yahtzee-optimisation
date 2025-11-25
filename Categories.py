import numpy as np

class Category:
    def __init__(self, name, num_dice):
        self.satisfied = False
        self.has_category = False
        self.probability = 0.0
        self.score = 0
        self.candidate_number = 0
        self.reroll_mask = np.zeros(num_dice, dtype=int)

        self.name = name

    def print_category(self):
        if self.satisfied: return
        print(f'Category: {self.name} \n Has Category: {self.has_category} \n Probability: {self.probability} \n Score: {self.score}\n')

    def choose(self):
        self.satisfied = True

class Three_of_a_kind(Category):
    def __init__(self, num_dice=5):
        super().__init__('Three of a Kind', num_dice)

    def check_category(self, dice):
        counts = np.bincount(dice)
        self.has_category = np.any(counts >= 3)
        self.candidate_number = np.argmax(counts) if self.has_category else 0

    def get_reroll_locations(self, dice):
        if self.has_category:
            return

        counts = np.bincount(dice)
        likely_candidate = np.argmax(counts)
        self.reroll_mask = np.where(dice == likely_candidate, 0, 1)

    def probability(self, dice):
        #Calculate the number of dice to be rerolled for three-of-a-kind
        pass

    def get_score(self, dice):
        if not self.has_category:
            self.score = 0
            return

        self.score = np.sum(dice, where=(dice == self.candidate_number))