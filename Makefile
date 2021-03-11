SHELL:=/bin/zsh

json:
	@ find ./Questions -type f -iname "*.yaml" -exec cat {} + | python3 -c 'import sys, yaml, json; json.dump(yaml.load(sys.stdin), sys.stdout, indent=4)' > Webtool/Frontend/AllQuestions.json
	@ echo "YAML files found:"
	find ./Questions -type f -iname "*.yaml"
	@ echo "JSON file generated: Webtool/Frontend/AllQuestions.json"


testpdf:
	@ find ./Questions -type f -iname "*.yaml" -exec cat {} + > combined_questions.yaml
	./make_md_doc.py # --> Combined_Questions.md
	./latex_preview -f Combined_Questions.md -v -j
	cat "Combined_Questions.md" | pandoc -f markdown -r markdown+fenced_divs+tex_math_single_backslash+citations --template=/home/zack/MakeMeAQual/pandoc_template.tex --pdf-engine=xelatex -o "CombinedQuestions.pdf"
	echo "Output written at Combined_Questions.pdf"

update:
	make json
	git add *; git commit -am "Save"; git push && ssh zack@dzackgarza.com 'cd MakeMeAQual && git pull'

clean:
	rm combined_questions.*

.ONESHELL:

