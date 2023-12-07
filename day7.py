#!/usr/bin/env python3

from parse import compile
from itertools import repeat
from collections import Counter
from functools import cmp_to_key

sort_order = {'A': 0, 'K': 1, 'Q': 2,
              'T':4,
              '9':5,
              '8':6,
              '7':7,
              '6':8,
              '5':9,
              '4':10,
              '3':11,
              '2':12,
              'J':13,
              }

def compare_syms(one, two):
    for (i, j) in zip(list(one[0]), list(two[0])):
        if i == j:
            continue
        sorts = sorted([i, j], key=lambda val: sort_order[val])
        if i == sorts[0]:
            return 1
        else:
            return -1
    return 0

FIVE = 7
FOUR = 6
FULL = 5
THREE = 4
TWO2 = 3
ONE2 = 2
HIGH = 1

def compare(one, two):
    str1 = Counter(one[0])
    str1j = str1['J']
    str2 = Counter(two[0])
    str2j = str2['J']
    type1 = 10
    # Only one type of card
    if len(set(str1)) == 1:
        type1 = FIVE
    # Only two types of card
    elif len(set(str1)) == 2:
        # Most common element is 4
        if str1.most_common(1)[0][1] == 4:
            # Other is J, so FIVE
            if str1j == 1 or str1j == 4:
                type1 = FIVE
            else:
                type1 = FOUR
        # Most common has 3
        if str1.most_common(1)[0][1] == 3:
            # others are J
            if str1j == 3 or str1j == 2:
                type1 = FIVE
            # Else max possible is FULL
            else:
                type1 = FULL
    # If have three of one and two different
    elif str1.most_common(1)[0][1] == 3:
        # If those three are j
        if str1j == 3:
            type1 = FOUR
        # If one of the others is j
        elif str1j == 1:
            type1 = FOUR
        # Else three
        else:
            type1 = THREE
    # two pairs and an odd one out
    elif str1.most_common(2)[0][1] == 2 and str1.most_common(2)[1][1] == 2:
        # j is one of the pairs, it morphs to the other pair
        if str1j == 2:
            type1 = FOUR
        # j makes a full house
        elif str1j == 1:
            type1 = FULL
        # boring
        else:
            type1 = TWO2
    # there is just one pair and everything else is different
    elif str1.most_common(1)[0][1] == 2:
        # j is the pair
        if str1j == 2:
            type1 = THREE
        # j is not the pair
        elif str1j == 1:
            type1 = THREE
        # boring
        else:
            type1 = ONE2
    # everything is different
    elif str1.most_common(1)[0][1] == 1:
        # there is a j!
        if str1j == 1:
            type1 = ONE2
        else:
            type1 = HIGH

    type2 = 10
    if len(set(str2)) == 1:
        type2 = FIVE
    elif len(set(str2)) == 2:
        if str2.most_common(1)[0][1] == 4:
            if str2j == 1 or str2j == 4:
                type2 = FIVE
            else:
                type2 = FOUR
        elif str2.most_common(1)[0][1] == 3:
            if str2j == 3 or str2j == 2:
                type2 = FIVE
            else:
                type2 = FULL
    elif str2.most_common(1)[0][1] == 3:
        if str2j == 3:
            type2 = FOUR
        elif str2j == 1:
            type2 = FOUR
        else:
            type2 = THREE
    elif str2.most_common(2)[0][1] == 2 and str2.most_common(2)[1][1] == 2:
        if str2j == 2:
            type2 = FOUR
        elif str2j == 1:
            print("full")
            type2 = FULL
            print("type2", type2)
        else:
            type2 = TWO2
    elif str2.most_common(1)[0][1] == 2:
        if str2j == 2:
            type2 = THREE
        elif str2j == 1:
            type2 = THREE
        else:
            type2 = ONE2
    elif str2.most_common(1)[0][1] == 1:
        if str2j == 1:
            type2 = ONE2
        else:
            type2 = HIGH

    if str1j > 0 or str2j > 0:
        print(one[0], type1, two[0], type2)
    greater = type1 - type2
    if greater == 0:
        if str1j > 0 or str2j > 0:
            print("comparing", compare_syms(one, two))
        return compare_syms(one, two)

    return greater

filename = "input7"
#filename = "test7"
file = open(filename, 'r')
lines = file.readlines() #[l.split(" ") for l in file.readlines()]
file.close()

hands = []
for l in lines:
    split = l.split()
    hands.append((split[0], int(split[1])))

sorts = sorted(hands, key=cmp_to_key(compare))
total = 0
for i,s in enumerate(sorts):
    total += (i + 1) * s[1]
print(total)
    
