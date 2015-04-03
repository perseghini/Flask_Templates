from flask_wtf import Form
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired, ValidationError, EqualTo
from .models import User


class LoginForm(Form):
    """Form handling the login process."""
    login = StringField('login', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

    @staticmethod
    def validate_password(form, field):

        # getting a default user until we have a db to store them.
        user = User.get_by_email(form.login.data)

        if user is None:
            raise ValidationError("Invalid user")

        if not user.is_valid_password(form.password.data):
            raise ValidationError("Invalid password")
        form.user = user
        form.remember = form.remember_me.data


class RegistrationForm(Form):
    """Form handling the account creation."""
    login = StringField('login', validators=[DataRequired()])
    password = PasswordField('password', validators=[
        DataRequired(),
        EqualTo('confirm', 'Passwords must match')])
    confirm = PasswordField('confirm')