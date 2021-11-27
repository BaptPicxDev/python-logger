SHELL := /bin/bash
.SHELLFLAGS = -ec
.ONESHELL:
.SILENT:

.EXPORT_ALL_VARIABLES:
REPO_DIRECTORY:=$(shell pwd)
AIRFLOW_HOME?=${REPO_DIRECTORY}/airflow
PYTHONPATH:=${PYTHONPATH}:${REPO_DIRECTORY}
PROJECT_PATH="${HOME}/Documents/Projects/python-logger"

.PHONY: help
help:
	grep -E '^\.PHONY: [a-zA-Z0-9_-]+ .*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = "(: |##)"}; {printf "\033[36m%-30s\033[0m %s\n", $$2, $$3}'

.PHONY: build-env ## Construct the virtual env
build-env:
	python3 -m venv "${PROJECT_PATH}/venv"
	source "${PROJECT_PATH}/venv/bin/activate"
	pip install -r "${PROJECT_PATH}/requirements.txt"

.PHONY: clean-env ## Clean the virtual env
clean-env:
	rm -r -f "${PROJECT_PATH}/venv"

.PHONY: unittest ## Run unittests
unittest:
	pytest -vv

.PHONY: clean ## Clean the project 
clean:
	echo "Cleaning"
