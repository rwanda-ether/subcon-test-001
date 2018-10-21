#!/usr/bin/env python3
import random

random.seed(0)

with open("log.txt", "r") as f:
    lines = f.read()

lines = lines.split("\n")
lines.pop(-1)
lines.reverse()

x = 100
n = 1

commits = []

for s in lines:
    c = random.uniform(1.4,1.5)
    #print(n, x, c, s)
    commits.append({'n': n, 'x': x, 'c': c, 'hash': s})
    x = int(x * c + 0.5)
    n += 1



for s in commits:
    print (s)
