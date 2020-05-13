SHELL:=/bin/zsh

json:
	find ./Questions -type f -iname "*.yaml" 
	@ find ./Questions -type f -iname "*.yaml" -exec cat {} + | yq '.' > Webtool/Frontend/AllQuestions.json
	@ echo "JSON file generated: Webtool/Frontend/AllQuestions.json"

.ONESHELL:

