#!/usr/bin/env python3

filename = "input2"
# filename = "test2"
file = open(filename, 'r')
lines = file.readlines() #[l.split(" ") for l in file.readlines()]
file.close()

red = 0
blue = 0
green = 0

m = {"red": 12, "green": 13, "blue": 14}
redt = 12
greent = 13
bluet = 14
total = 0
for l in lines:
    words = l.split(':')
    game = int(words[0].split(' ')[1].strip(':'))
    d = words[1].split(';')
    valid = True
    for g in d:
        colors = g.split(',')
        for c in colors:
            ms = c.strip().split(' ')
            print(ms)
            if m[ms[1].strip()] < int(ms[0].strip()):
                print("indvalid", ms)
                valid = False
    if valid:
        total += game
        print(game)

print(total)
