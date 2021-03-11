#!/bin/zsh

./replace.sh "→" "\\to" **/*.yaml;
./replace.sh "µ" "\\mu" **/*.yaml;
./replace.sh "×" "\\times" **/*.yaml;
./replace.sh "≤" "\\leq" **/*.yaml;
