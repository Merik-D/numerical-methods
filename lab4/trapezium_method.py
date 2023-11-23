import math


def f(x):
    return math.sqrt((1 + x) / (1 - x))


def trapezium_method(a, b, n=30):
    h = (b - a) / n
    x = a + h
    integral = 0
    fa = f(a)
    fb = f(b)
    while x <= b:
        integral = integral + f(x)
        x += h
    integral = h * ((fa + fb) / 2 + integral)
    return integral


if __name__ == "__main__":
    print(f"Метод трапеції: {trapezium_method(0, 0.5)}")