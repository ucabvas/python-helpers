#!/usr/bin/python

import fileinput

for line in fileinput.input():
    vals = line.strip().split(' ')
    print vals[0] + '\t' + ' '.join(vals[1:-1]) + '\t' + vals[-1]

