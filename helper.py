import numpy as np
import math

np.set_printoptions(precision=3, suppress=True)

def get_probability_matrices(num_dice=6, num_sides=5):
    # calculate the probability matrix of going from i to j dice of the same face (for one roll)
    matrix1 = np.zeros((num_dice, num_dice), dtype=float)
    for i in range(1,num_dice+1):
        for j in range(1,num_dice+1):
            if i > j:
                matrix1[i-1,j-1] = 0
            else:
                p = 1 / num_sides
                n = num_dice - i
                k = j - i
                C = math.comb(n, k) # number of ways to choose k from n (binomial coefficient
                matrix1[i-1,j-1] = C * (p ** k) * ((1 - p) ** (n - k))

    # for two rolls (we can just multiply the matrix by itself)
    matrix2 = matrix1 ** 2

    print(matrix1)
    return matrix1, matrix2