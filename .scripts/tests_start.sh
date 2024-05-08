#! /usr/bin/env bash
set -e

python tests_pre_start.py

bash test.sh "$@"
