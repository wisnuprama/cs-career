#!/bin/bash

echo "Run unit test"
source env/bin/activate
coverage run --include='app_*/*' manage.py test
coverage report -m
echo "Stopping ..."
