#!/bin/bash

cd /home/space/belltower

# source .venv/bin/activate

exec python -m uvicorn api:app --host 0.0.0.0 --port 8456
