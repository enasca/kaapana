#!/bin/bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 5000 --root-path $APPLICATION_ROOT