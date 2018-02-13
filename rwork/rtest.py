import rpy2.robjects as robj

robj.r["MYdata = read.csv['data.csv', header=TRUE]"]
robj.r["fit = lm(Y ~ X, data=MYdata)"]
print(robj.r["summary(fit)"])
