#!/usr/bin/env bash

set -x

mypy core
black core --check
isort --recursive --check-only ../core
flake8
