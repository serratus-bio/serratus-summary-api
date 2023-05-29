[ -e env.sh ] && source env.sh
export FLASK_APP=application.py
export FLASK_ENV=development

export FLASK_RUN_HOST=0.0.0.0
export FLASK_RUN_PORT=5000

flask run
