def swap_rows(matrix, i, j):
    matrix[i], matrix[j] = matrix[j], matrix[i]


def gaussian_method(matrix):
    n = len(matrix)
    det = 1

    for k in range(n):
        max_row = max(range(k, n), key=lambda i: abs(matrix[i][k]))
        print(matrix)

        if k != max_row:
            swap_rows(matrix, k, max_row)
            det *= -1

        for i in range(k + 1, n):
            factor = matrix[i][k] / matrix[k][k]
            for j in range(k, n):
                matrix[i][j] -= factor * matrix[k][j]

    det *= 1
    for i in range(n):
        det *= matrix[i][i]

    return det

if __name__ == "__main__":

    A = [
        [8.3, 2.78, 4.1, 1.9],
        [3.92, 8.45, 7.62, 2.46],
        [3.77, 7.37, 8.04, 2.28],
        [2.21, 3.49, 1.69, 6.69]
    ]

    result = gaussian_method(A)
    print("Детермінант:", result)