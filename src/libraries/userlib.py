import binascii
import hashlib
import os

from src.models.users import site

SALT_LENGTH = 16
HASH_METHOD = "SHA512"

class UserLib():
    def __init__(self):
        print ("Initialized User Lib")

    def password_hashing(self, password, salt=None):
        if not salt:
            salt = binascii.hexlify(os.urandom(SALT_LENGTH / 2)).decode()

        hash_library = hashlib.new(HASH_METHOD)
        salted_client_hash = str(password + salt)
        hash_library.update(salted_client_hash)
        server_hash = hash_library.hexdigest()
        return (server_hash, salt)

    @property
    def validate_input(self):
        if "site_name" not in self.user_info:
            return "missing key 'site_name'", False

        if "email_id" not in self.user_info:
            return "missing key 'email_id'", False

        if "password" not in self.user_info:
            return "missing key 'password'", False

        users = site.objects.filter(email_id=self.user_info["email_id"])
        if users.count() > 0:
            return "user already exists", False

        return "Success", True

    def createUser(self, user_info):
        '''

        :param user_info: JSON data posted on API.
        :return: "user created successfully"
        '''
        self.user_info = user_info

        message, status = self.validate_input

        if(status):
            print("validation is successful", self.user_info)

            password_hash, salt = self.password_hashing(self.user_info["password"])
            print (password_hash, salt)

            self.user_info["password"] = password_hash
            self.user_info["salt"] = salt

            site.objects.create(**self.user_info)
        else:
            return message, False

        return "user created successfully", True

