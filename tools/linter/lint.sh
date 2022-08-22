#!/bin/bash -e

BASE_DIR=$(dirname $0)
ROOT_DIR="$(cd $BASE_DIR && pwd -P)"
echo "root dir = $ROOT_DIR"

echo "****************************************************************"
echo "executing pycodestyle"
pycodestyle --max-line-length=120 .

echo "****************************************************************"
echo "executing pyflakes"
python ${ROOT_DIR}/run-pyflakes.py

echo "****************************************************************"
echo "executing mccabe"
python ${ROOT_DIR}/run-mccabe.py 7

echo "****************************************************************"
echo "executing pylint"
pylint code
