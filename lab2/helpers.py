import math

def f(x):
    return math.exp(-x) - x

def df(x):
    return -1 - math.exp(-x)

def check_convergence(x1, x2):
    return abs((x1 - x2) / x1) * 100
