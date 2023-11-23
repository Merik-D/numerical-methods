import numpy as np

from lab3.helpers import calculate_inverse_matrix, calculate_J, calculate_f, initial_guess, epsilon, max_iterations


def simplified_newton_method(initial_guess, epsilon, max_iterations):
    x = initial_guess
    J = calculate_J(x)
    J_inverse = calculate_inverse_matrix(J)

    for iteration in range(max_iterations):
        f = calculate_f(x)

        delta_x = np.dot(J_inverse, f)

        x_new = x - delta_x
        print(f"{iteration} iteration")

        if all(abs(d) < epsilon * abs(x_new[i]) for i, d in enumerate(delta_x)):
            return x_new
        print(x_new)
        x = x_new


print("Simplified_newton_method:\n")
print(simplified_newton_method(initial_guess, epsilon, max_iterations))