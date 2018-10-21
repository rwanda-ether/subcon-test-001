#!/usr/bin/env python3
#Time-stamp: <Mon Oct 22 01:55:56 JST 2018 hamada>
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
    c = random.uniform(1.36, 2.)
    #print(n, x, c, s)
    commits.append({'n': n, 'x': x, 'c': c, 'hash': s})
    x = int(x * (c-0.5) + 0.5)
    n += 1


budget_JPY = 8000000

md  = ''
md += "# Initial Budget from a Client = %d JPY (example case)" % budget_JPY +"\n\n"
md += '| n | X(n) | C(n) | commit hash | balance (MAK) | Client\'s Budget (JPY) |' + "\n"
md += '|---:|---:|---:|:---| ---:|---:|' + "\n"

accum = 0


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



print (md)

