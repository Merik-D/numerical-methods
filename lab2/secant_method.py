from lab2.helpers import check_convergence, f


def secant_method(x0, x1, e):
    xold = x0
    x = x1
    xnew = None
    while check_convergence(x, xold) > e:
        xnew = x - f(x) / ((f(xold) - f(x)) / (xold - x))
        xold = x
        x = xnew
    return xnew


print(secant_method(-2, 3, 0.001))
