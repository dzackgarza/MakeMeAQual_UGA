#!/bin/bash

find ./Questions -type f -iname "*.yaml" -exec cat {} + | yq -r '.[] | .question' > test.md            
