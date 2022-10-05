
#/bin/bash

export FLASK_ENV=development
export FLASK_APP=wsgi.py

flask run --host="0.0.0.0" --port=8888