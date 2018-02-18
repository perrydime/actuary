from sympy import *
init_printing(use_unicode=False)

t = symbols('t')


def convolve(f, g, x, lower_limit, upper_limit):
    y = Symbol('y')
    h = g.subs(x, x - y)
    return integrate(f * h, (y, lower_limit, upper_limit))

a = t**2

b = 3*t*exp(3*t)


print(simplify(convolve(a,b,t, 0, t)))


