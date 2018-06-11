import sympy  as sy
x = sy.symbols('x')
sy.init_printing(use_unicode=False)
# Peak of distribution
# peak = 3


# c = b^2/4a + ln(-a/pi)/2
b = 0
d = sy.sqrt(1/(72*sy.pi))
c = sy.ln(d)

# (peak/d) sets the peak
y = (sy.exp((-((x-36)**2)/72) + b*x + c))# *(peak/d)

#sy.plot(y,(x,0,100))


sy.pprint(y)

# print(y.subs(x,0).evalf(20))
