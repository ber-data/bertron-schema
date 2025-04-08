MAKEFLAGS += --warn-undefined-variables
SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := help
.DELETE_ON_ERROR:
.SUFFIXES:
.SECONDARY:

# environment variables
.EXPORT_ALL_VARIABLES:
ifdef LINKML_ENVIRONMENT_FILENAME
include ${LINKML_ENVIRONMENT_FILENAME}
else
include config.public.mk
endif

RUN = uv run
SRC_DIR = src
DEST_DIR = project
DOC_DIR = docs
EXAMPLE_DIR = examples
SCHEMA_NAME = $(LINKML_SCHEMA_NAME)
SOURCE_SCHEMA_PATH = $(LINKML_SCHEMA_SOURCE_PATH)
SOURCE_SCHEMA_DIR = $(SRC_DIR)/schema
SOURCE_SAMPLE_DATA_DIR = $(SRC_DIR)/sample_data
PYMODEL_DIR = $(SOURCE_SCHEMA_DIR)/datamodel
JSONSCHEMA_DIR = $(SOURCE_SCHEMA_DIR)/jsonschema
DOCTEMPLATES_DIR = $(SRC_DIR)/docs/templates
SHEET_MODULE = $(LINKML_SCHEMA_GOOGLE_SHEET_MODULE)
SHEET_ID = $(LINKML_SCHEMA_GOOGLE_SHEET_ID)
SHEET_TABS = $(LINKML_SCHEMA_GOOGLE_SHEET_TABS)
SHEET_MODULE_PATH = $(SOURCE_SCHEMA_DIR)/sheets/$(SHEET_MODULE).yaml

# Use += to append variables from the variables file
CONFIG_YAML =
ifdef LINKML_GENERATORS_CONFIG_YAML
CONFIG_YAML += "--config-file"
CONFIG_YAML += ${LINKML_GENERATORS_CONFIG_YAML}
endif

GEN_DOC_ARGS =
ifdef LINKML_GENERATORS_DOC_ARGS
GEN_DOC_ARGS += ${LINKML_GENERATORS_DOC_ARGS}
endif

GEN_OWL_ARGS =
ifdef LINKML_GENERATORS_OWL_ARGS
GEN_OWL_ARGS += ${LINKML_GENERATORS_OWL_ARGS}
endif

GEN_JAVA_ARGS =
ifdef LINKML_GENERATORS_JAVA_ARGS
GEN_JAVA_ARGS += ${LINKML_GENERATORS_JAVA_ARGS}
endif

GEN_TS_ARGS =
ifdef LINKML_GENERATORS_TYPESCRIPT_ARGS
GEN_TS_ARGS += ${LINKML_GENERATORS_TYPESCRIPT_ARGS}
endif


# basename of a YAML file in model/
.PHONY: all clean setup gen-project gen-examples gendoc git-init-add git-init git-add git-commit git-status

# note: "help" MUST be the first target in the file,
# when the user types "make" they should get help info
help: status
	@echo ""
	@echo "make setup -- initial setup (run this first)"
	@echo "make site -- makes site locally"
	@echo "make install -- install dependencies"
	@echo "make test -- runs tests"
	@echo "make lint -- perform linting"
	@echo "make testdoc -- builds docs and runs local test server"
	@echo "make deploy -- deploys site"
	@echo "make update -- updates linkml version"
	@echo "make help -- show this help"
	@echo ""

status: check-config
	@echo "Project: $(SCHEMA_NAME)"
	@echo "Source: $(SOURCE_SCHEMA_PATH)"

# generate products and add everything to github
setup: check-config git-init install gen-project gen-examples gendoc git-add git-commit

# install any dependencies required for building
install:
	uv sync
.PHONY: install

# ---
# Project Synchronization
# ---
#
# check we are up to date
check: cruft-check
cruft-check:
	cruft check
cruft-diff:
	cruft diff

update: update-template update-linkml
update-template:
	cruft update

# todo: consider pinning to template
# update-linkml:
# 	poetry add -D linkml@latest

# EXPERIMENTAL
create-data-harmonizer:
	npm init data-harmonizer $(SOURCE_SCHEMA_PATH)

all: site
site: gen-project gendoc
%.yaml: gen-project
deploy: all mkd-gh-deploy

compile-sheets:
	$(RUN) sheets2linkml --gsheet-id $(SHEET_ID) $(SHEET_TABS) > $(SHEET_MODULE_PATH).tmp && mv $(SHEET_MODULE_PATH).tmp $(SHEET_MODULE_PATH)

# In future this will be done by conversion
gen-examples:
	cp -r $(SOURCE_SAMPLE_DATA_DIR)/* $(EXAMPLE_DIR)

validate-examples:
	$(RUN) linkml-validate -s $(SOURCE_SCHEMA_PATH) $(SOURCE_SAMPLE_DATA_DIR)/valid/*.json

# generates all project files
gen-project: $(PYMODEL_DIR)
	$(RUN) gen-project ${CONFIG_YAML} -d $(DEST_DIR) $(SOURCE_SCHEMA_PATH) && mv $(DEST_DIR)/*.py $(PYMODEL_DIR)

# non-empty arg triggers owl (workaround https://github.com/linkml/linkml/issues/1453)
ifneq ($(strip ${GEN_OWL_ARGS}),)
	mkdir -p ${DEST_DIR}/owl || true
	$(RUN) gen-owl ${GEN_OWL_ARGS} $(SOURCE_SCHEMA_PATH) >${DEST_DIR}/owl/${SCHEMA_NAME}.owl.ttl
endif
# non-empty arg triggers java
ifneq ($(strip ${GEN_JAVA_ARGS}),)
	$(RUN) gen-java ${GEN_JAVA_ARGS} --output-directory ${DEST_DIR}/java/ $(SOURCE_SCHEMA_PATH)
endif
# non-empty arg triggers typescript
ifneq ($(strip ${GEN_TS_ARGS}),)
	mkdir -p ${DEST_DIR}/typescript || true
	$(RUN) gen-typescript ${GEN_TS_ARGS} $(SOURCE_SCHEMA_PATH) >${DEST_DIR}/typescript/${SCHEMA_NAME}.ts
endif

test: test-schema test-python test-examples

test-schema:
	$(RUN) gen-project ${CONFIG_YAML} -d tmp $(SOURCE_SCHEMA_PATH)

test-python:
	$(RUN) python -m pytest

lint:  ## lint the schema; warnings or errors result in a non-zero exit code
	$(RUN) linkml-lint $(SOURCE_SCHEMA_PATH)

lint-no-warn:  ## lint the schema; warnings do not result in a non-zero exit code
	$(RUN) linkml-lint --ignore-warnings $(SOURCE_SCHEMA_PATH)


gen-artefacts: $(PYMODEL_DIR) $(JSONSCHEMA_DIR)  ## generate standard repo artefacts (JSON Schema and Pydantic versions of the schema)
	$(RUN) gen-json-schema $(SOURCE_SCHEMA_PATH) > $(JSONSCHEMA_DIR)/bertron_schema.json
	$(RUN) gen-pydantic $(SOURCE_SCHEMA_PATH) > $(PYMODEL_DIR)/bertron_schema_pydantic.py

check-config:
ifndef LINKML_SCHEMA_NAME
	$(error **Project not configured**:\n\n - See '.env.public'\n\n)
else
	$(info Ok)
endif

convert-examples-to-%:
	$(patsubst %, $(RUN) linkml-convert  % -s $(SOURCE_SCHEMA_PATH) -C Entity, $(shell ${SHELL} find $(SOURCE_SAMPLE_DATA_DIR) -name "*.yaml"))

examples/%.yaml: $(SOURCE_SAMPLE_DATA_DIR)/%.yaml
	$(RUN) linkml-convert -s $(SOURCE_SCHEMA_PATH) -C Entity $< -o $@
examples/%.json: $(SOURCE_SAMPLE_DATA_DIR)/%.yaml
	$(RUN) linkml-convert -s $(SOURCE_SCHEMA_PATH) -C Entity $< -o $@
examples/%.ttl: $(SOURCE_SAMPLE_DATA_DIR)/%.yaml
	$(RUN) linkml-convert -P EXAMPLE=http://example.org/ -s $(SOURCE_SCHEMA_PATH) -C Entity $< -o $@

test-examples: examples/output

examples/output: src/$(SCHEMA_NAME)/schema/$(SCHEMA_NAME).yaml
	mkdir -p $@
	$(RUN) linkml-run-examples \
		--output-formats json \
		--output-formats yaml \
		--counter-example-input-directory $(SOURCE_SAMPLE_DATA_DIR)/invalid \
		--input-directory $(SOURCE_SAMPLE_DATA_DIR)/valid \
		--output-directory $@ \
		--schema $< > $@/README.md


serve: mkd-serve ## Test documentation locally

# Python datamodel directory
$(PYMODEL_DIR):
	mkdir -p $@

# JSON Schema model directory
$(JSONSCHEMA_DIR):
	mkdir -p $@

# documentation directory
$(DOC_DIR):
	mkdir -p $@

gendoc: $(DOC_DIR)  ## generate Markdown documentation locally
	cp -rf $(SRC_DIR)/docs/files/* $(DOC_DIR) ; \
	$(RUN) gen-doc ${GEN_DOC_ARGS} -d $(DOC_DIR) $(SOURCE_SCHEMA_PATH)
	mkdir -p $(DOC_DIR)/javascripts
	cp $(SRC_DIR)/docs/js/*.js $(DOC_DIR)/javascripts/

gendoc-gh: ## generate HTML documentation for deployment on GitHub Pages
	touch $(DOC_DIR)/.nojekyll
	make gendoc
	make mkd-gh-deploy

testdoc: gendoc serve

MKDOCS = $(RUN) mkdocs
mkd-%:
	$(MKDOCS) $*

git-init-add: git-init git-add git-commit git-status
git-init:
	git init
git-add: .cruft.json
	git add .
git-commit:
	git commit -m 'chore: make setup was run' -a
git-status:
	git status

# only necessary if setting up via cookiecutter
.cruft.json:
	echo "creating a stub for .cruft.json. IMPORTANT: setup via cruft not cookiecutter recommended!" ; \
	touch $@

clean:
	rm -rf $(DEST_DIR)
	rm -rf tmp
	rm -fr $(DOC_DIR)/*
	rm -fr $(PYMODEL_DIR)/*

include project.Makefile
