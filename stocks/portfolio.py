import numpy as np
import csv
stock1 = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
count = 0
with open('stock1.csv', 'rb') as csvfile:
    read = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in read:
        #if(count > 0):
        stock1[count] = float(row[1])
            #print row[0] + ',' + row[1]
        count = count + 1
    count = 0

stock1_returns = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
for count in range(11):
    if(count < 12):
        print(count)
        stock1_returns[count] = (stock1[count+1] - stock1[count])/stock1[count]

stock1_cum_ret = 0.0
for count in range(11):
    stock1_cum_ret += stock1_returns[count]

stock1_avg_daily_ret = stock1_cum_ret / 10.0

stock1_sum_squared_error = 0.0
for count in range(11):
    stock1_sum_squared_error += ((stock1_returns[count] - stock1_avg_daily_ret)**2)
stock1_variance = stock1_sum_squared_error/10.0

stock1_standard_deviation = np.sqrt(stock1_variance)

print(stock1_cum_ret)
print(stock1_variance)
print(stock1_standard_deviation)

'''

stock1[12] = {0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0}
with open('stock2.csv', 'rb') as csvfile:
    read = csv.reader(csvfile, delimiter=',', quotechar='"')
    count = 0
    for row in read:
        #if(count > 0):
        stock2[count] = row[1]
            #print row[0] + ',' + row[1]
        count = count + 1
    count = 0
'''
