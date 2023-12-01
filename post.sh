#!/bin/bash

# Usage: post.sh <day> <1|2> <answer>

wget --post-data="level=$2&answer=$3" \
	-O- -S \
	--no-cookies --header "Cookie: $ADVENT_COOKIE" \
	https://adventofcode.com/2023/day/$1/answer
