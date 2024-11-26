#!/bin/sh

uvicorn python_api_template.main:app --port 8080 --host 0.0.0.0
