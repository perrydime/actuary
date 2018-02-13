import json
import sys
from scipy.linalg import solve
import numpy as np
import matplotlib.pyplot as plt
from sympy import diff
from sympy import integrate
from sympy import Symbol
# print(sys.argv)

# print("LIT.json")
stockName = sys.argv[1][:-5]
data = json.load(open(sys.argv[1]))

dates01 = ['2017-01-04',
'2017-01-06',
'2017-01-09',
'2017-01-11',
'2017-01-13',
'2017-01-17',
'2017-01-18',
'2017-01-20',
'2017-01-23',
'2017-01-25',
'2017-01-27',
'2017-01-30']
dates02 = ['2017-02-01',
'2017-02-03',
'2017-02-06',
'2017-02-08',
'2017-02-10',
'2017-02-13',
'2017-02-15',
'2017-02-17',
'2017-02-21',
'2017-02-22',
'2017-02-24',
'2017-02-27']
dates03 = ['2017-03-01',
'2017-03-03',
'2017-03-06',
'2017-03-08',
'2017-03-10',
'2017-03-13',
'2017-03-15',
'2017-03-17',
'2017-03-20',
'2017-03-22',
'2017-03-24',
'2017-03-29']
dates04 = ['2017-04-03',
'2017-04-05',
'2017-04-07',
'2017-04-10',
'2017-04-12',
'2017-04-13',
'2017-04-17',
'2017-04-19',
'2017-04-21',
'2017-04-24',
'2017-04-26',
'2017-04-28']
dates05 = ['2017-05-01',
'2017-05-03',
'2017-05-05',
'2017-05-08',
'2017-05-10',
'2017-05-12',
'2017-05-15',
'2017-05-17',
'2017-05-19',
'2017-05-22',
'2017-05-24',
'2017-05-30']
dates06 = ['2017-06-01',
'2017-06-05',
'2017-06-07',
'2017-06-09',
'2017-06-12',
'2017-06-14',
'2017-06-16',
'2017-06-19',
'2017-06-21',
'2017-06-23',
'2017-06-26',
'2017-06-30']
dates07 = ['2017-07-03',
'2017-07-05',
'2017-07-07',
'2017-07-10',
'2017-07-12',
'2017-07-14',
'2017-07-17',
'2017-07-19',
'2017-07-21',
'2017-07-24',
'2017-07-26',
'2017-07-28']
dates08 = ['2017-08-02',
'2017-08-04',
'2017-08-07',
'2017-08-09',
'2017-08-11',
'2017-08-14',
'2017-08-16',
'2017-08-18',
'2017-08-21',
'2017-08-23',
'2017-08-25',
'2017-08-28']
dates09 = ['2017-09-01',
'2017-09-05',
'2017-09-06',
'2017-09-08',
'2017-09-11',
'2017-09-13',
'2017-09-15',
'2017-09-18',
'2017-09-20',
'2017-09-22',
'2017-09-25',
'2017-09-29']
dates10 = ['2017-10-02',
'2017-10-04',
'2017-10-06',
'2017-10-09',
'2017-10-11',
'2017-10-13',
'2017-10-16',
'2017-10-18',
'2017-10-20',
'2017-10-23',
'2017-10-25',
'2017-10-27']
dates11 = ['2017-11-01',
'2017-11-03',
'2017-11-06',
'2017-11-08',
'2017-11-10',
'2017-11-13',
'2017-11-15',
'2017-11-17',
'2017-11-20',
'2017-11-22',
# '2017-11-24',
# '2017-11-27'
]
dates12 = ['2017-12-01',
'2017-12-04',
'2017-12-06',
'2017-12-08',
'2017-12-11',
'2017-12-13',
'2017-12-15',
'2017-12-18',
'2017-12-20',
'2017-12-22',
'2017-12-27',
'2017-12-19']


systemDates = ['Week 1 Mon',
'Week 1 Wed',
'Week 1 Fri',
'Week 2 Mon',
'Week 2 Wed',
'Week 2 Fri',
'Week 3 Mon',
'Week 3 Wed',
'Week 3 Fri'
'Week 4 Mon',
'Week 4 Wed',
'Week 4 Fri']




count = 0
# print "January"
jan = ''
for i in (dates01):
    jan = jan + str(count) + "," + str(data['Time Series (Daily)'][i]['4. close']) + '\n'
    count = count + 1
jan = jan[:-1]

count = 0
# print "February"
feb = ''
for i in (dates02):
    feb = feb + str(count) + "," + str(data['Time Series (Daily)'][i]['4. close']) + '\n'
    count = count + 1
feb = feb[:-1]

count = 0
# print "March"
mar = ''
for i in (dates03):
    mar = mar + str(count) + "," + str(data['Time Series (Daily)'][i]['4. close']) + '\n'
    count = count + 1
mar = mar[:-1]

count = 0
# print "April"
apr = ''
for i in (dates04):
    apr = apr + str(count) + "," + str(data['Time Series (Daily)'][i]['4. close']) + '\n'
    count = count + 1
apr = apr[:-1]

count = 0
# print "May"
may = ''
for i in (dates05):
    may = may + str(count) + "," + str(data['Time Series (Daily)'][i]['4. close']) + '\n'
    count = count + 1
may = may[:-1]

count = 0
# print "June"
jun = ''
for i in (dates06):
    jun = jun + str(count) + "," + str(data['Time Series (Daily)'][i]['4. close']) + '\n'
    count = count + 1
jun = jun[:-1]

count = 0
# print "July"
jul = ''
for i in (dates07):
    jul = jul + str(count) + "," + str(data['Time Series (Daily)'][i]['4. close']) + '\n'
    count = count + 1
jul = jul[:-1]

count = 0
# print "August"
aug = ''
for i in (dates08):
    aug = aug + str(count) + "," + str(data['Time Series (Daily)'][i]['4. close']) + '\n'
    count = count + 1
aug = aug[:-1]

count = 0
#print "September"
sep = ''
for i in (dates09):
    sep = sep + str(count) + "," + str(data['Time Series (Daily)'][i]['4. close']) + '\n'
    count = count + 1
sep = sep[:-1]

count = 0
# print "October"
octo = ''
for i in (dates10):
    octo = octo + str(count) + "," + str(data['Time Series (Daily)'][i]['4. close']) + '\n'
    count = count + 1
octo = octo[:-1]

count = 0
# print "November"
nov = ''
for i in (dates11):
    nov = nov + str(count) + "," + str(data['Time Series (Daily)'][i]['4. close']) + '\n'
    count = count + 1
nov = nov[:-1]

print "January"
print jan
print "February"
print feb
print "March"
print mar
print "April"
print apr
print "May"
print may
print "June"
print jun
print "July"
print jul
print "August"
print aug
print "September"
print sep
print "October"
print octo
print "November"
print nov


def graph(y, dy, ddy, dddy, x_range, x_ticks, monthName, stockName):
    x = np.array(x_range)
    ey = eval(y)
    edy = eval(dy)
    eddy = eval(ddy)
    edddy = eval(dddy)
    fig = plt.figure()
    fig.suptitle(stockName + " " + monthName, fontsize=14, fontweight='bold')
    s = fig.add_subplot(111)
    plt.xticks(x, x_ticks, rotation='vertical')
    plt.axhline(0, color='black')
    s.plot(x, ey, label="Price")
    w = fig.add_subplot(111)
    w.plot(x, edy, label="Velocity")
    h = fig.add_subplot(111)
    h.plot(x, eddy, label="Accel")
    j = fig.add_subplot(111)
    j.plot(x, edddy, label="Jerk")
    plt.legend()


def monthlyEquationGraph(monthPoints, monthName, x_ticks):
    pointJan = monthPoints.split("\n")
    yIntJan = pointJan[0].split(',')
    exesJan = [0 for x in range(len(pointJan)-1)]
    whysJan = [0 for x in range(len(pointJan)-1)]
    matrixJan = [[0 for x in range(len(pointJan)-1)] for y in range(len(pointJan)-1)]

    for a in range(1, len(pointJan)):
        xy = pointJan[a].split(",")
        exesJan[a-1] = float(xy[0])
        whysJan[a-1] = float(xy[1]) - float(yIntJan[1])

    for b in range(len(pointJan)-1):
        order = len(pointJan)-1
        for c in range(len(pointJan)-1):
            matrixJan[b][c] = exesJan[b]**order
            order = order - 1

    xJan = solve(matrixJan, whysJan)

    eqJan = ''
    order = len(pointJan)-1
    for d in range(order):
        eqJan = eqJan + str(xJan[d]) + '*x**' + str(order) + '+'
        order = order - 1

    eqJan = eqJan + yIntJan[1]

    # print monthName + ' Raw Equation'
    # print eqJan

    eq = eqJan
    x = Symbol('x')


    eqinty = integrate(eqJan, (x,0,len(pointJan)-1))

    # print monthName + " Integral"
    # print eqinty

    normeq = eq.replace("x","(1/" + str(eqinty) + ")*x")
    normeq = normeq.replace("x**1+","x**1+(1/" + str(eqinty) + ")*")
    # normeq = (1/eqinty)*eq

    # print monthName + ' Normalized Equation'
    # print normeq

    # print integrate(normeq,(x,0,len(pointJan)-1))

    eqdy = diff(eqJan)
    eqddy = diff(eqdy)
    eqdddy = diff(eqddy)


    graph(eqJan, str(eqdy), str(eqddy), str(eqdddy), range(0, 11), x_ticks, monthName, stockName)

    return normeq


janNorm = monthlyEquationGraph(jan, "January 2017", dates01)
febNorm = monthlyEquationGraph(feb, "February 2017", dates02)
marNorm = monthlyEquationGraph(mar, "March 2017", dates03)
aprNorm = monthlyEquationGraph(apr, "April 2017", dates04)
mayNorm = monthlyEquationGraph(may, "May 2017", dates05)
junNorm = monthlyEquationGraph(jun, "June 2017", dates06)
julNorm = monthlyEquationGraph(jul, "July 2017", dates07)
augNorm = monthlyEquationGraph(aug, "August 2017", dates08)
sepNorm = monthlyEquationGraph(sep, "September 2017", dates09)
octNorm = monthlyEquationGraph(octo, "October 2017", dates10)
novNorm = monthlyEquationGraph(nov, "November 2017", dates11)


# system = eval(str(janNorm) + "+" + str(febNorm) + "+" + str(marNorm) + "+" + str(aprNorm) + "+" + str(mayNorm) + "+" + str(junNorm) + "+" + str(julNorm) + "+" + str(augNorm) + "+" + str(sepNorm) + "+" + str(octNorm) + "+" + str(novNorm))
system = str(janNorm) + "+" + str(febNorm) + "+" + str(marNorm) + "+" + str(aprNorm) + "+" + str(mayNorm) + "+" + str(junNorm) + "+" + str(julNorm) + "+" + str(augNorm) + "+" + str(sepNorm) + "+" + str(octNorm) + "+" + str(novNorm)
# print system


sysdy = diff(system)
sysddy = diff(sysdy)
sysdddy = diff(sysddy)



graph(system, str(sysdy), str(sysddy), str(sysdddy), range(0, 11), systemDates, "Month in General", stockName)


plt.show()
