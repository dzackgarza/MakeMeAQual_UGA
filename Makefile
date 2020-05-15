SHELL:=/bin/zsh

json:
	@ find ./Questions -type f -iname "*.yaml" -exec cat {} + | yq . > Webtool/Frontend/AllQuestions.json
	@ echo "JSON file generated: Webtool/Frontend/AllQuestions.json. YAML files found:"
	find ./Questions -type f -iname "*.yaml"


testpdf:
	@ find ./Questions -type f -iname "*.yaml" -exec cat {} + > combined_questions.yaml
	make_md_doc.py
	latex_preview -f combined_questions.md -v


cleanup:
	rm combined_questions.*

.ONESHELL:

