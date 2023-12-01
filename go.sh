#!/bin/bash

# Usage: go.sh <day>

wget -O input$1 --no-cookies --header "Cookie: $ADVENT_COOKIE"  https://adventofcode.com/2023/day/$1/input

export DAY="$1"

cp starter.py day$1.py
