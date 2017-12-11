migrate: bash deployment.sh
web: gunicorn tp_2_ppw.wsgi --log-file -
heroku ps:scale web=1 migrate=1 --app