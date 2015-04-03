""" Views redirecting to the appropriate HTML file content. (Flask Routes) """

from flask_templates import app, lm
from flask import render_template, flash, redirect, request, url_for, g
from flask_login import login_required, login_user, logout_user, current_user
from .forms import LoginForm, RegistrationForm
from .models import User


@app.before_request
def before_request():
    g.user = current_user


@lm.user_loader
def load_user(user_id):
    return User.get_by_id(int(user_id))


@app.route('/index')
@app.route('/')
@login_required
def index():
    """Main page of the website."""
    return render_template('index.html')
    pass


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login page of the website."""
    form = LoginForm()
    if form.validate_on_submit():
        login_user(user=form.user, remember=form.remember)
        flash('Logged in successfully')
        return redirect(request.args.get('next') or url_for('index'))
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    """Logout the current user and redirect to the index page."""
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Register page (Create new user)."""
    form = RegistrationForm()
    if form.validate_on_submit():
        User.create(form.login.data, form.password.data)
        flash('Thanks for registering!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)