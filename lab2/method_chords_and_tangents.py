from lab2.helpers import check_convergence, f, df


def combined_method(a, b, e):
    x1 = 0
    x2 = 0
    while check_convergence(a, b) > e:
        fa = f(a)
        fb = f(b)

        x1 = a - (fa * (b - a)) / (fb - fa)
        fx = f(x1)

        if abs(fx) < e:
            return x1

        if fx * fa > 0:
            a = x1
            x2 = b
        else:
            b = x1
            x2 = a

        fx2 = f(x2)
        dfx2 = df(x2)

        x2 = x2 - fx2 / dfx2

        if abs(a - x1) < e:
            b = x2
        else:
            a = x2

    return (x1 + x2) / 2


print(combined_method(-2, 3, 0.001))
