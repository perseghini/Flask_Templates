from flask_wtf import Form
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired, ValidationError
from .models import User


class LoginForm(Form):
    """Form handling the login process"""
    login = StringField('login', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

    def validate_password(form, field):

        # getting a default user until we have a db to store them.
        user = User.get(1)

        if user is None or form.login.data.lower() != 'admin':
            raise ValidationError("Invalid user")

        if not user.is_valid_password(form.password.data):
            raise ValidationError("Invalid password")
        form.user = user
        form.remember = form.remember_me.data