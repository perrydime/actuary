import numpy as np

#############################################
### Note: Start varibale out with decimal ###
#############################################

# Accumlated Amount
A = 100
# Principal
P = 10000.0
# Interest Rate
i = 0.12
# Number of Terms
t = 5.0


# Simple Interest
#A = P*(1 + (i*t))
#P = A/(1 + (i*t))
#t = (A - P)/(i*P)
#i = (A - P)/(t*P)


# Compound Interest
#A = P*((1 + i)**t)
P = A/((1 + i)**t)
#t = (np.log(A/P))/(np.log(1+i))
#i = ((A/P)**(1/t)) - 1


print(P)
