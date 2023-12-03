#!/bin/bash

# Usage: post.sh <1|2> <answer>

day=3

wget --post-data="level=$1&answer=$2" \
	-O- -S \
	--no-cookies --header "Cookie: $ADVENT_COOKIE" \
	https://adventofcode.com/2023/day/$day/answer
