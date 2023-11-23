import numpy as np

initial_guess = np.array([0.5, 0.5])
epsilon = 1e-6
max_iterations = 100


def calculate_f(x):
    f1 = x[0]**2 + 0.8 * x[1]**2 + 0.1 - x[0]
    f2 = 2 * x[0] * x[1] - 0.1 - x[1]
    return [f1, f2]


def calculate_J(x):
    J = [[0.0, 0.0], [0.0, 0.0]]
    J[0][0] = 2 * x[0] - 1
    J[0][1] = 1.6 * x[1]
    J[1][0] = 2 * x[1]
    J[1][1] = 2 * x[0] - 1
    return J


def calculate_inverse_matrix(A):
    A = np.array(A)
    n = A.shape[0]
    m = np.hstack((A, np.eye(n)))

    for nrow, row in enumerate(m):
        divider = row[nrow]
        if divider != 0:
            row /= divider

        # row /= divider
        for lower_row in m[nrow + 1:]:
            factor = lower_row[nrow]
            lower_row -= factor * row
    for k in range(n - 1, 0, -1):
        for row_ in range(k - 1, -1, -1):
            if m[row_, k]:
                m[row_, :] -= m[k, :] * m[row_, k]

    return m[:, n:].tolist()
