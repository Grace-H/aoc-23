#!/usr/bin/env python3

file = open('input1', 'r')
lines = file.readlines()
file.close()

words={"one": "1", "two": "2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9", "zero":"0"}

def fm(l, s):
    return min([i for i in range(len(l)) if l.startswith(s, i)], default=-1) 

def lm(l, s):
    return max([i for i in range(len(l)) if l.startswith(s, i)], default=-1) 

nums = []
for l in lines:
    num = ""
    #find first
    mini = len(l)
    val = '1'
    for key in words:
        if fm(l, key) != -1 and fm(l, key) < mini:
            val = words[key]
            mini = fm(l,key)

    for i, n in enumerate(l):
        if n.isdigit():
            if i < mini:
                val = n
            break
    num += val
    maxi = 0

    for key in words:
        if lm(l, key) != -1 and lm(l, key) + len(key) > maxi:
            val = words[key]
            maxi = lm(l, key) + len(key)
    for i, n in enumerate(reversed(l)):
        if n.isdigit():
            if len(l) - i > maxi:
                val = n
            break
    num += val
    nums.append(int(num))


print(sum(nums))
