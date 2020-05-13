SHELL:=/bin/zsh

json:
	find . -type f -iname "*.yaml" -exec cat {} +
