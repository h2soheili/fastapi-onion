#! /usr/bin/env bash

echo "________________"
echo "PWD:"$PWD
# Let the DB start
python backend_pre_start.py



# Run migrations
alembic upgrade head

# Create initial data in DB
python initial_data.py
