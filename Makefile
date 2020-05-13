SHELL:=/bin/zsh

json:
	@ find ./Algebra -type f -iname "*.yaml" -exec cat {} + | yq '.' > Webtool/Frontend/Algebra.json
	@ echo "JSON file generated: Algebra.json"
	@ find ./Real_Analysis -type f -iname "*.yaml" -exec cat {} + | yq '.' > Webtool/Frontend/Real_Analysis.json
	@ echo "JSON file generated: Real_Analysis.json"
	@ find ./Topology -type f -iname "*.yaml" -exec cat {} + | yq '.' > Webtool/Frontend/Topology.json
	@ echo "JSON file generated: Topology.json"
	@ find ./Complex_Analysis -type f -iname "*.yaml" -exec cat {} + | yq '.' > Webtool/Frontend/Complex_Analysis.json
	@ echo "JSON file generated: Complex_Analysis.json"


.ONESHELL:

