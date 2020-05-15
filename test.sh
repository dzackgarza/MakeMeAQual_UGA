#!/bin/bash

find ./Questions -type f -iname "*.yaml" -exec cat {} + | yq -r '.[] | .question' | while read linetext; do
  echo === $linetext ===
done
