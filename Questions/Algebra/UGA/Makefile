SHELL:=/bin/zsh

define renew_md = 
{echo "---\n title: 'UGA Qualifying Exam Questions: Algebra'\n book: true\n---\n\n" && fd --full-path ./sections | sort -n | sed 'N;s/\(.*\)\n\(.*\)/\2\n\1/' | grep "md" | sort -nr | awk -F ":" '{print "!include " $$1 "\n";}' } > CombinedQuestions.md 2>&1
endef

renew: 
	@$(renew_md)
	echo "Done"

compile:
	make renew
	latex_preview -f ./CombinedQuestions.md -j
	echo "Make done"

watch:
	make renew
	latex_preview -f ./CombinedQuestions.md

view: 
	make renew
	latex_preview -f ./CombinedQuestions.md -v

.ONESHELL:

