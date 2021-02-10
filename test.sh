[ -e env.sh ] && source env.sh
export PYTHONPATH="$PYTHONPATH:./"
pytest
