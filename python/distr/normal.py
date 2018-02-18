from sympy import *
init_printing(use_unicode=False)
x = symbols('x')

# Peak of distribution
peak = 3


# c = b^2/4a + ln(-a/pi)/2
b = 0
d = sqrt(1/(2*pi))
c = ln(d)

# (peak/d) sets the peak
y = (exp((-(x**2)/2) + b*x + c))*(peak/d)

plot(y,(x,-4,4))


pprint(y)
