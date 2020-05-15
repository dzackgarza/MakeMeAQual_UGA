SHELL:=/bin/zsh

json:
	@ find ./Questions -type f -iname "*.yaml" -exec cat {} + | yq . > Webtool/Frontend/AllQuestions.json
	@ echo "JSON file generated: Webtool/Frontend/AllQuestions.json. YAML files found:"
	find ./Questions -type f -iname "*.yaml"


testpdf:
	@ find ./Questions -type f -iname "*.yaml" -exec cat {} + > combined_questions.yaml
	./test.sh
	latex_preview -f combined_questions.md -v

.ONESHELL:


.INTERMEDIATE: combined_questions.md combined_questions.pdf
