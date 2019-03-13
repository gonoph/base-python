import logging
from time import time
from flask import Flask, g, request, current_app, redirect
from itsdangerous import json

logger = logging.getLogger(__name__)
app = Flask(__name__)
_init_handlers(app)

@app.route("/")
def index():
    return redirect('/api/healthz')

@app.route("/api/healthz")
def healthz():
    errors = [];
    try:
        open(state.DEMO_FILE_PATH, "a+").close();
    except IOError as ex:
        logger.exception('Unable to read pods')
        errors.append(str(ex))
    try:
        pods = client.nocache_get_my_pods();
        if pods.num < 1:
            raise ValueError('no pods were returned!')
    except Exception as ex:
        logger.exception('unable to access db file')
        errors.append(str(ex))
    return dict(status="ok" if not errors else "error", errors=errors)
