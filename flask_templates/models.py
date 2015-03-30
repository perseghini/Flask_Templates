from flask_login import UserMixin
import hashlib


class User(UserMixin):
    """ User Class, used to authentify users across the site."""
    id = 0
    email = 'placeholder@example.com'

    def get_id(self):
        return str(self.id)

    def is_valid_password(self, password):

        # temporary password until DB:
        hex_password = ('f95f676b24dbef39663486f756c8f0e7454bbb065aebbf962a'
                        '900e1dd1e7f4693dda8146628ee85b10d55880dce063ffa6a4'
                        '89d2953aa4dff53753555df3b95c')

        encoded_password = password.encode('utf-8')
        return hashlib.sha512(encoded_password).hexdigest() == hex_password

    @staticmethod
    def get(user_id):
        """TODO replace with DB Get."""
        return User()