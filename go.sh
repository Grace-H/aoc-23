#!/bin/bash

# Usage: go.sh

day=15

wget -O input$day \
	--no-cookies --header "Cookie: $ADVENT_COOKIE"  \
	https://adventofcode.com/2023/day/$day/input

cp starter.py day$day.py
sed -i "" "s/XX/${day}/g" day${day}.py
