from Roll import Roll

class Player:
    def __init__(self, player_number):
        self.scores = {
            'ones': 0,
            'twos': 0,
            'threes': 0,
            'fours': 0,
            'fives': 0,
            'sixes': 0,
            'three_of_a_kind': 0,
            'four_of_a_kind': 0,
            'full_house': 0, # three of a kind and a pair
            'small_straight': 0, # sequence of four
            'large_straight': 0, # sequence of five
            'yahtzee': 0,
            'bonus': 0,
        }

        self.player_number = player_number
        self.total_score = 0
        self.base_rerolls = 2
        self.cur_rerolls = self.base_rerolls

        self.roller = Roll()

    def calculate_total_score(self):
        self.total_score = sum(self.scores.values())

    def change_score(self, category, score):
        if category not in self.scores:
            raise ValueError(f'Invalid category: {category}')

        self.scores[category] = score

    def make_roll(self):
        self.roller.roll_all()