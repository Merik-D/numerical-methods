import numpy as np

from lab3.helpers import calculate_f, initial_guess, max_iterations, epsilon


def extrap_method(f, x0, epsilon, max_iterations):
    m = len(x0)
    q = m
    n = 2 * q + 1
    cond = False

    for k in range(max_iterations):
        if k == 0:
            E = np.zeros((m, m))
        else:
            E = np.eye(m)

        Sn = np.zeros((n, m))

        for i in range(n):
            if i == 0:
                Sn[i] = x0
            else:
                Sn[i] = Sn[i - 1] + np.dot(E, f(Sn[i - 1]))

        if k > 0:
            cond = all(abs(Sn[n - 1] - Sn[n - 2]) / (abs(Sn[n - 2]) + 1e-10) * 100 < epsilon)

        if cond:
            x = Sn[n - 1]
            break
        else:
            x0 = x0 + np.dot(E, f(x0))
        print(f"{k} iteration:\n {x0}")

    return x


print("Extrapolation\n")
result = extrap_method(calculate_f, initial_guess, epsilon, max_iterations)
print(f"Результат: {result}")