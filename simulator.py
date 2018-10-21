#!/usr/bin/env python3
#Time-stamp: <Mon Oct 22 00:50:58 JST 2018 hamada>
import random

random.seed()

with open("log.txt", "r") as f:
    lines = f.read()

lines = lines.split("\n")
lines.pop(-1)
lines.reverse()

x = 100
n = 1

commits = []

for s in lines:
    c = random.uniform(1., 2.)
    #print(n, x, c, s)
    commits.append({'n': n, 'x': x, 'c': c, 'hash': s})
    x = int(x * (c-0.5) + 0.5)
    n += 1


md  = ''
md += '| n | X(n) | C(n) | commit hash | balance (MAK) |' + "\n"
md += '|---:|---:|---:|:---| ---:|' + "\n"

accum = 0

for s in commits:
    accum += s['x']
    md += "| %d | %d | %1.3f | %s | %d |\n" % (s['n'], s['x'], s['c'], s['hash'], accum)


print (md)

