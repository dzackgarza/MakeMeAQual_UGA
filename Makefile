SHELL:=/bin/zsh

json:
	find ./Algebra -type f -iname "*.yaml" -exec cat {} + | yq '.' > Algebra.json
	echo "JSON file generated: Algebra.json"


.ONESHELL:

