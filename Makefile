SHELL:=/bin/zsh

json:
	@ find ./Questions -type f -iname "*.yaml" -exec cat {} + | yq . > Webtool/Frontend/AllQuestions.json
	@ echo "YAML files found:"
	find ./Questions -type f -iname "*.yaml"
	@ echo "JSON file generated: Webtool/Frontend/AllQuestions.json"


testpdf:
	@ find ./Questions -type f -iname "*.yaml" -exec cat {} + > combined_questions.yaml
	./make_md_doc.py # --> Combined_Questions.md
	latex_preview -f Combined_Questions.md 
	echo "Output written at Combined_Questions.pdf"

update:
	make json
	git add *; git commit -am "Save"; git push && ssh zack@dzackgarza.com 'cd MakeMeAQual && git pull'

clean:
	rm combined_questions.*

.ONESHELL:

