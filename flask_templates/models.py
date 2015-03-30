from flask_login import UserMixin
import hashlib


class User(UserMixin):
    """ User Class, used to authentify users across the site."""
    id = 0
    email = 'placeholder@example.com'

    def get_id(self):
        return str(self.id)

    def is_valid_password(self, password):

        # temporary password until DB (password = 'admin'):
        hex_password = ('c7ad44cbad762a5da0a452f9e854fdc1e0e7a52a38015f2'
                        '3f3eab1d80b931dd472634dfac71cd34ebc35d16ab7fb8a'
                        '90c81f975113d6c7538dc69dd8de9077ec')

        encoded_password = password.encode('utf-8')
        return hashlib.sha512(encoded_password).hexdigest() == hex_password

    @staticmethod
    def get(user_id):
        """TODO replace with DB Get."""
        return User()