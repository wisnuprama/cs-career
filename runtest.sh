#!/bin/bash

echo "Run unit test"
source env/bin/activate
python manage.py collectstatic --no-input
python manage.py runserver 8000 &
coverage run --include='lab_*/*' manage.py test
coverage report -m
echo "Stopping ..."
return
