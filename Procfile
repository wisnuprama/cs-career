migrate: bash deployment.sh
web: gunicorn praktikum.wsgi --log-file -
heroku ps:scale web=1 migrate=1 --app