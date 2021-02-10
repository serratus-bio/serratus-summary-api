[ -e env.sh ] && source env.sh
export FLASK_APP=application.py
export FLASK_ENV=development
flask run
