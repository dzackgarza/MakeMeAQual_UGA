SHELL:=/bin/zsh

json:
	find . -type f -iname "*.yaml" -exec cat {} + | yq '.' > output.json
	echo "JSON file generated: output.json"


.ONESHELL:

