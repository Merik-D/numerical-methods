from lab2.helpers import check_convergence, df, f


def simplified_method_newton(x, e):
    f_dx = df(x)

    xold = x
    x = x - f(x) / f_dx
    while check_convergence(x, xold) > e:
        xold = x
        x = x - f(x) / f_dx
    return x


print(simplified_method_newton(-2, 0.01))
