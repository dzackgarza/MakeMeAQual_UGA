#!/usr/bin/python3

#find ./Questions -type f -iname "*.yaml" -exec cat {} + | yq '.[] | .question' | while read linetext; do
  #echo === $linetext ===
#done

import yaml

with open(r'combined_questions.yaml') as file:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
    fruits_list = yaml.load(file, Loader=yaml.FullLoader)

    print(fruits_list)
