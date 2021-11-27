SHELL := /bin/bash
.SHELLFLAGS = -ec
.ONESHELL:
.SILENT:

.EXPORT_ALL_VARIABLES:
REPO_DIRECTORY:=$(shell pwd)
PYTHONPATH:=${PYTHONPATH}:${REPO_DIRECTORY}
PROJECT_PATH="${HOME}/Documents/Projects/python-logger"

.PHONY: help
help:
	grep -E '^\.PHONY: [a-zA-Z0-9_-]+ .*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = "(: |##)"}; {printf "\033[36m%-30s\033[0m %s\n", $$2, $$3}'


.PHONY: build-env ## Construct the virtual env
build-env:
	python3 -m venv ./venv
	source ./venv/bin/activate
	pip install -r requirements.txt


.PHONY: clean-env ## Clean the virtual env
clean-env:
	rm -r -f venv/


.PHONY: unittest ## Run unittests
unittest:
	pytest -vv tests/


.PHONY: quality ## Get the quality of the code
quality:
	find source/ tests/ -type f -name "*.py" | xargs flake8 --count


.PHONY: clean ## Clean the project
clean:
	ls -a -R | grep -e "__pycache__" -e ".pytest_cache" -e "venv" | xargs rm -rf
