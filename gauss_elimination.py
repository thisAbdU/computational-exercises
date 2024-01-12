import numpy as np


def gauss_elimination(a_matrix, b_matrix):
    if a_matrix.shape[0] != a_matrix.shape[1]:
        print("ERROR: square matrix is not given!")
        return
    if b_matrix.shape[1] > 1 or b_matrix.shape[0] != a_matrix.shape[0]:
        print("ERROR: constant vector incorrectly sized")
        return

    n = len(b_matrix)
    x = np.zeros(n)
    i = 0
    new_line = "\n"

    augmented_matrix = np.concatenate((a_matrix, b_matrix), axis=1).astype(float)
    print(f"The initial augmented matrix is {new_line} {augmented_matrix}")
    print("Solving for upper triangular matrix...")

    # Partial pivoting
    for i in range(n):
        for p in range(i + 1, n):
            if abs(augmented_matrix[i][i]) < abs(augmented_matrix[p][i]):
                augmented_matrix[[i, p]] = augmented_matrix[[p, i]]

        if augmented_matrix[i][i] == 0.0:
            print("Divide by Zero error")
            return

        for j in range(i + 1, n):
            scaling_factor = augmented_matrix[j][i] / augmented_matrix[i][i]
            augmented_matrix[j] = augmented_matrix[j] - (scaling_factor * augmented_matrix[i])
            print(augmented_matrix)
            print("----------------------")

    # Backward substitution
    x[n - 1] = augmented_matrix[n - 1][n] / augmented_matrix[n - 1][n - 1]

    for k in range(n - 2, -1, -1):
        x[k] = augmented_matrix[k][n]

        for j in range(k + 1, n):
            x[k] -= augmented_matrix[k][j] * x[j]

        x[k] = x[k] / augmented_matrix[k][k]

    for answer in range(n):
        print(f"X({answer}) is '{x[answer]:.3f}'")


variable_matrix = np.asarray([[1, 1, 1, 0, 0],
                              [0, 0, 0, 9, 3],
                              [9, 3, 1, 0, 0],
                              [0, 0, 0, 25, 5],
                              [0, 0, 25, 5, 1],
                              ])
constant_matrix = np.asarray([[2], [3], [3], [9], [9]])
print("Gauss Elimination With Partial Pivoting")
print("=" * 50)
gauss_elimination(variable_matrix, constant_matrix)
