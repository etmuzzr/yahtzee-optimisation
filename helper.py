import numpy as np
import math

def get_probability_matrices(num_dice=6, num_side=5):
    # calculate the probability matrix of going from i to j dice of the same face (for one roll)
    matrix1 = np.zeros((num_dice, num_dice))
    for i in range(num_dice):
        for j in range(num_dice):
            if j < i:
                matrix1[i][j] = 0
            else:
                p = 1 / num_sides
                nCr = math.comb(num_dice - i, i - j)
                matrix1[i][j] = nCr * (p ** i) * ((1 - p) ** (i - j))

    # for two rolls (we can just multiply the matrix by itself)
    matrix2 = matrix1 ** 2

    return matrix1, matrix2