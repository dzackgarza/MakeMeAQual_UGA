SHELL:=/bin/zsh

json:
	@ find ./Questions -type f -iname "*.yaml" -exec cat {} + | python3 -c 'import sys, yaml, json; json.dump(yaml.load(sys.stdin), sys.stdout, indent=4)' > Webtool/Frontend/AllQuestions.json
	@ echo "YAML files found:"
	find ./Questions -type f -iname "*.yaml"
	@ echo "JSON file generated: Webtool/Frontend/AllQuestions.json"


testpdf:
	@ find ./Questions -type f -iname "*.yaml" -exec cat {} + > Combined_Questions.yaml
	./make_md_doc.py # --> Combined_Questions.md
	cat "Combined_Questions.md" | pandoc -f markdown -r markdown+fenced_divs+tex_math_single_backslash+citations --template=pandoc_template.tex -o "Combined_Questions.tex";
	@mkdir -p tex_tempfiles;
	@latexmk --shell-escape -pdf Combined_Questions.tex -quiet -outdir=tex_tempfiles && cp tex_tempfiles/Combined_Questions.pdf . 2>&1 >/dev/null;
	echo "Output written at Combined_Questions.pdf"

update:
	make json
	git add *; git commit -am "Save"; git push && ssh zack@dzackgarza.com 'cd MakeMeAQual && git pull'

clean:
	@ rm Combined_Questions.*
	echo "Removed combined questions"

.ONESHELL:

