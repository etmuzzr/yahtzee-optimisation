import numpy as np
from helper import get_probability_matrices

class Category:
    def __init__(self, name, num_dice, num_sides):
        self.satisfied = False
        self.has_category = False
        self.probability = 0.0
        self.weight = 0.0
        self.score = 0
        self.num_dice = num_dice
        self.num_sides = num_sides
        self.reroll_mask = np.zeros(num_dice, dtype=int)
        self.name = name

    def print(self):
        if self.satisfied: return
        print(f'Category: {self.name} \nHas Category: {self.has_category} \nProbability: {self.probability} \nDecision Weight: {self.weight} \nScore: {self.score}\n')

    def choose(self):
        self.satisfied = True

class Three_of_a_kind(Category):
    def __init__(self, num_dice=5, num_sides=6):
        super().__init__('three_of_a_kind', num_dice, num_sides)

    def check_category(self, dice):
        counts = np.bincount(dice)
        self.has_category = np.any(counts >= 3)

    def get_reroll_locations(self, dice):
        if self.has_category:
            return

        counts = np.bincount(dice)
        likely_candidate = np.argmax(counts)
        self.reroll_mask = np.where(dice == likely_candidate, 0, 1)

    def find_probability(self, dice, rerolls_remaining):
        if self.has_category:
            self.probability = 1.0
            return

        matrix_one_roll, matrix_two_rolls = get_probability_matrices(self.num_dice, self.num_sides)
        prob_matrix = matrix_one_roll if rerolls_remaining == 1 else matrix_two_rolls

        self.get_reroll_locations(dice)
        i = self.num_dice - np.sum(self.reroll_mask)
        # the probability of going from i matching dice to 3-5 matching dice
        self.probability = np.sum(prob_matrix[i-1, 2:])

    # the decision weight for a category (calculated with our probability, current score and expected category score)
    def find_weight(self):
        max_score = 30
        self.weight = self.probability * (self.score / max_score)

    # plausible score for the category (even if the dice doesn't contain the conditions)
    def find_score(self, dice):
        self.score = np.sum(dice)