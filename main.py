from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

import sha

app = Flask(__name__)
app.config.from_envvar('QUASSELFLASK_SETTINGS')

db = SQLAlchemy(app)
db.reflect(app=app)

from views import quassel
app.register_blueprint(quassel)
