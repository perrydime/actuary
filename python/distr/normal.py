from sympy import *
init_printing(use_unicode=False)
x = symbols('x')

# Peak of distribution
# peak = 3


# c = b^2/4a + ln(-a/pi)/2
b = 0
d = sqrt(1/(72*pi))
c = ln(d)

# (peak/d) sets the peak
y = (exp((-((x-36)**2)/72) + b*x + c))# *(peak/d)

plot(y,(x,0,100))


# pprint(y)

print(y.subs(x,0).evalf(20))
