from flask_login import UserMixin
from flask_templates import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class User(UserMixin, db.Model):
    """ User Class, used to authentify users across the site."""
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    hash_password = db.Column(db.String(66))
    creation_date = db.Column(db.Date)

    def is_valid_password(self, password):
        """
        Check if user password match with the one in the DB.

        :param password: User password.
        """
        return check_password_hash(self.hash_password, password)

    @staticmethod
    def get_by_id(user_id):
        """
        Get a User in the DB by his ID.

        :param user_id: user ID.
        """
        user = User.query.filter_by(id=user_id).first()
        return user

    @staticmethod
    def get_by_email(user_email):
        """
        Get a User in the DB by his email.

        :param user_email: user email.
        """
        user = User.query.filter_by(email=user_email).first()
        return user

    @staticmethod
    def create(email, password):
        """
        Create a new user.

        :param email: user email address.
        :param password: user password.
        :return if the user has been created (True) or if the email is
                already used (False)
        """
        hash_password = generate_password_hash(password)
        user = User(email=email,
                    hash_password=hash_password,
                    creation_date=datetime.utcnow())

        db.session.add(user)
        db.session.commit()