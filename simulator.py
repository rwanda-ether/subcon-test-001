#!/usr/bin/env python3
#Time-stamp: <Mon Oct 22 02:25:30 JST 2018 hamada>
import random

random.seed(2)

with open("log.txt", "r") as f:
    lines = f.read()

lines = lines.split("\n")
lines.pop(-1)
lines.reverse()

x = 100
n = 1

commits = []

for s in lines:
    c = random.uniform(1.3, 2.)
    #print(n, x, c, s)
    commits.append({'n': n, 'x': x, 'c': c, 'hash': s})
    x = int(x * (c-0.5) + 0.5)
    n += 1


budget_JPY = 8000000

md  = ''
md += "Initial Budget from a Client = %d JPY (example case)" % budget_JPY +"\n\n"
md += '| n | X(n) | C(n) | commit hash | balance (MAK) | Client\'s Budget (JPY) |' + "\n"
md += '|---:|---:|---:|:---| ---:|---:|' + "\n"


accum = 0


plots = []

for s in commits:
    salary = s['x']

    if budget_JPY >= salary:
        budget_JPY -= salary
        accum += salary
    else:
        salary = budget_JPY
        accum += salary
        budget_JPY = 0

    md += "| %d | %d | %1.3f | %s | %d | %d|\n" % (s['n'], salary, s['c'], s['hash'], accum, budget_JPY)
    plots.append({'n': s['n'], 'c': s['c'], 'salary': salary, 'accum': accum, 'budget': budget_JPY})

print (md)


with open("./plotdata.log", "w") as f:
    lines = []
    for p in plots:
        lines.append("%d\t%d\t%1.4f\t%d\t%d\n"%(p['n'], p['salary'], p['c'], p['accum'], p['budget']) )

    for line in lines:
        f.write(line)

