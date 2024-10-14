#!/bin/bash

# Start the FastAPI app with Uvicorn
# Adjust the "main" to point to your FastAPI app file. 
# If your entry point is in a file named main.py, it will look like this:
uvicorn main:app --host 0.0.0.0 --port 8000
