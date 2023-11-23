import math


def f(x):
    return math.sqrt((1 + x) / (1 - x))


def simpson_method(a, b, m=10):
    integral = 0
    n = 2 * m
    h = (b - a) / n
    fa = f(a)
    fb = f(b)

    for i in range(1, n, 2):
        x = a + i * h
        integral += 4 * f(x)
    for i in range(2, n - 1, 2):
        x = a + i * h
        integral += 2 * f(x)

    integral = (h / 3) * (fa + fb + integral)

    return integral


if __name__ == "__main__":
    print(f"Метод Сімпсона: {simpson_method(0, 0.5)}")
