from flask import Blueprint, render_template, request

import sha
from models import QuasselUser

from main import db

quassel = Blueprint('quassel', __name__, template_folder='templates')

def crypt(password):
    s = sha.new(password)
    return s.hexdigest()

@quassel.route('/', methods=['GET', 'POST'])
def index():
    error1 = ""
    error2 = ""
    success = ""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('oldpass')
        user = QuasselUser.query.filter_by(username=username).first()
        if user and user.password == crypt(password):
            newpass1 = request.form.get('newpass1')
            newpass2 = request.form.get('newpass2')
            if newpass1 and newpass2:
                if newpass1 == newpass2:
                    user.password = crypt(newpass1)
                    db.session.add(user)
                    db.session.commit()
                    success = "password changed"
                else:
                    error2 = "passwords do not match"
            else:
                error2 = "one or both new passwords are empty"
        else:
            error1 = "name or password wrong"
    return render_template('index.html', error1=error1, error2=error2, success=success)
