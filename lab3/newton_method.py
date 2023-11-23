import numpy as np

from lab3.helpers import calculate_f, calculate_inverse_matrix, calculate_J, initial_guess


def newton_method(initial_guess, epsilon=1e-6, max_iterations=100):
    x = initial_guess
    for iteration in range(max_iterations):
        print(f"{iteration} iteration")

        f = calculate_f(x)
        J = calculate_J(x)

        inverse_J = calculate_inverse_matrix(J)

        x_new = x - np.dot(inverse_J, f)

        if all(abs(x_new - x) / (abs(x) + 1e-10) * 100 < epsilon):
            break
        print(x_new)
        x = x_new

    return f"Результат: {x}"


print("Newton_method:\n")
print(newton_method(initial_guess))