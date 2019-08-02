import binascii
import hashlib
import os

from src.models import site, Token

SALT_LENGTH = 16
HASH_METHOD = "SHA512"


class LoginLib():
    def __init__(self):
        self.login_detail = None
        print "Login lib is working"

    def password_hashing(self, password, salt=None):
        if not salt:
            salt = binascii.hexlify(os.urandom(SALT_LENGTH / 2)).decode()

        hash_library = hashlib.new(HASH_METHOD)
        salted_client_hash = str(password + salt)
        hash_library.update(salted_client_hash)
        server_hash = hash_library.hexdigest()
        return (server_hash, salt)

    def validateLogin(self, login_detail):
        if "email_id" not in login_detail:
            return "missing key 'email_id'", False

        if "password" not in login_detail:
            return "missing key 'password'", False

        users = site.objects.filter(email_id=login_detail["email_id"])
        if users.count() > 0:

            selected_user = users[0]

            password_from_db = selected_user.password
            salt_from_db = selected_user.salt

            password_hash_req, salt = self.password_hashing(password=login_detail["password"], salt=salt_from_db)

            print password_from_db
            print password_hash_req

            if password_from_db == password_hash_req:
                return "Login Validation Successful", True
            else:
                return "Invalid Password", True

        return "user not found", False

    def login(self, login_detail):
        self.login_detail = login_detail
        message, status = self.validateLogin(login_detail)
        if status:
            #return "continue with login process", True
            token = Token.objects.create(user=login_detail)
            print (token.key)

        else:
            return message, False
