#!/usr/bin/env bash

# current directory
SCRIPT_DIR=$(
    cd "$(dirname "$0")"
    pwd
)
echo "SCRIPT_DIR: $SCRIPT_DIR"
# parent directory
PARENT_DIR=$(
    cd "$SCRIPT_DIR/.."
    pwd
    cd "$SCRIPT_DIR"
)
echo "PARENT_DIR: $PARENT_DIR"

PYTHONPATH=${PARENT_DIR}:${PYTHONPATH} python3 -m unittest discover -v -s ${SCRIPT_DIR} -p 'test_*.py'
