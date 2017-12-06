#!/bin/bash

# run python virtual env
source env/bin/activate
echo "Python virtual env is running"
echo "Run server"
python3 manage.py runserver 8000
