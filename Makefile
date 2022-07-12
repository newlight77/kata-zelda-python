#!make

# Makefile for Demo Auth Serve
SHELL := /bin/sh

#export BUILD = $(shell git describe --always)-$(shell date +%Y%m%d%H%M%S)
#export TAG = $(shell git describe --abbrev=0 --tags)
#BRANCH = $(shell git branch --show-current)
# export VERSION ?= $(shell git describe --always)

# $(info version = $(VERSION))

install:
	@pyenv install 3.10.4
	# @pyenv local 3.10.4
	@pipenv install
	@pipenv shell

lint:
	@./tools/linter/lint.sh

test:
	@PYTHONPATH=. pytest

run:
	@python main.py

unit-test:
	@pytest -vv -x -s -k unit

integration-test:
	@pytest -vv -x -s -k integration

all-test:
	@pytest -vv -x -s
