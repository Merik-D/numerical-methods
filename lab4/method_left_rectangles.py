import math


def f(x):
    return math.sqrt((1 + x) / (1 - x))


def method_left_rectangles(a, b, n=30):
    h = (b - a) / n
    x = a
    integral = 0
    while x < b:
        integral = integral + f(x)
        x += h
    integral = integral * h
    return integral


if __name__ == "__main__":
    print(f"Метод лівих прямокутників: {method_left_rectangles(0, 0.5)}")