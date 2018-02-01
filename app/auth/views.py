from . import auth
from flask import render_template,redirect,url_for,flash,request
from ..models import User
from .forms import LoginForm,RegistrationForm
from .. import db
from flask_login import login_user
from ..models import User

@auth.route('/login',methods=['GET','POST'])
def login():
    login_from = LoginForm()
    if login_from.validate_on_submit():
        user = User.query.filter_by(email = login_from.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    title = "watchlist login"
    return render_template('auth/login.html',login_form = login_form,title=title)

@auth.route('/regester',methods = ["GET","POST"])
def regester():
    form = RegestrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.user.data, password = form.data.password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('auth/registration.html',registration_form = form)
