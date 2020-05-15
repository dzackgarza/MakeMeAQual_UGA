#!/usr/bin/python

#find ./Questions -type f -iname "*.yaml" -exec cat {} + | yq '.[] | .question' | while read linetext; do
  #echo === $linetext ===
#done
