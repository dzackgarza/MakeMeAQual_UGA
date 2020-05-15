#!/usr/bin/python3

#find ./Questions -type f -iname "*.yaml" -exec cat {} + | yq '.[] | .question' | while read linetext; do
  #echo === $linetext ===
#done

import yaml

with open(r'combined_questions.yaml') as file:
    fruits_list = yaml.load(file)

    print(fruits_list)
