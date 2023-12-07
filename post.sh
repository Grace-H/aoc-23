#!/bin/bash

# Usage: post.sh <1|2> <answer>

day=7

if [[ $1 -eq "1" ]] ; then
	cp day${day}.py day${day}b.py
fi

wget --post-data="level=$1&answer=$2" \
	-O- -S \
	--no-cookies --header "Cookie: $ADVENT_COOKIE" \
	https://adventofcode.com/2023/day/$day/answer
