#!/bin/bash

# pytest is baked into the environment image (environment/Dockerfile).
pytest /tests/test_outputs.py -rA --json-ctrf /app/ctrf-report.json

if [ $? -eq 0 ]; then
  echo 1 > /app/reward.txt
else
  echo 0 > /app/reward.txt
fi
