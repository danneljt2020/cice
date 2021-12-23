import json
from hashlib import sha256
from random import random


class Flight:
    def __init__(self, username, pwd):
        self.username = username
        pwd_e = sha256(pwd.encode()).hexdigest()
        self.pwd = pwd_e  # encryp pass

    @property
    def user_dict(self):
        return {
            "username": self.username,
            "pwd": self.pwd
        }

