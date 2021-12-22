import json
from hashlib import sha256
from random import random
from functools import wraps


class User:
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


class Admin(User):
    def __init__(self, username, pwd):
        super().__init__(username, pwd)

    @property
    def users(self):
        with open("user.json", encoding="utf8") as file:
            return json.load(file)

    def change_name(self, username, new_username):
        auth = Auth("./user.json")
        result = auth.get_user_by_username(username)

        if result.get('index'):
            user_obj = result["user_obj"]
            index = result["index"]
            user_obj["username"] = new_username

            users = self.users
            users["data"][index] = user_obj

            dat = open("user.json", "w", encoding="utf8")
            json.dump(users, dat, indent=3, ensure_ascii=False)
            dat.close()


SECRET = b"cice"


class Auth:

    def __init__(self, db):
        self.db = db

    @property
    def users(self):
        with open(self.db, encoding="utf8") as file:
            return json.load(file)

    @property
    def cookies(self):
        with open('cookies.json', encoding="utf8") as file:
            return json.load(file)

    def gen_token(self, user):
        token = sha256(user.username.encode())
        token.update(SECRET)
        token.update(str(random()).encode())
        return token.hexdigest()

    def get_user_by_username(self, username):
        users = self.users["data"]
        result = {}
        for i, user in enumerate(users):
            if user["username"].lower() == username.lower():
                result["user_obj"] = user
                result["index"] = i
        return result

    # def autenticate(self, func):
    #     @wraps(func)
    #     def verify_token(*args, **kwargs):
    #         cookies = self.cookies["tokens"]
    #         users = self.users["data"]
    #         flag = False
    #         if cookies.get('token'):
    #             for user in users:
    #                 if user["token"] == cookies["token"]:
    #                     flag = True
    #         return flag
    #
    #     return verify_token

    def verify_token(self):
        cookies = self.cookies["tokens"]
        users = self.users["data"]
        flag = False
        if cookies.get('token'):
            for user in users:
                if user["token"] == cookies["token"]:
                    flag = True
        return flag

    def create_user(self, user):
        users = self.users
        users["data"].append(user)
        with open(self.db, "w", encoding="utf8") as file:
            json.dump(users, file, ensure_ascii=False, indent=4)

    def log_in(self, user):
        user_obj_index = self.get_user_by_username(user.username)
        token = self.gen_token(user)
        flag = False
        if user_obj_index.get('user_obj'):
            user_obj = user_obj_index["user_obj"]
            index = user_obj_index["index"]
            if user_obj["pwd"] == user.pwd:
                user_obj["token"] = token
                users = self.users
                users["data"][index] = user_obj

                dat = open(self.db, "w", encoding="utf8")
                json.dump(users, dat, indent=3, ensure_ascii=False)
                dat.close()

                cookies = self.cookies
                cookie_token = {'username': user.username, 'token': token}
                cookies["tokens"] = cookie_token

                json_cookies = open('cookies.json', "w", encoding="utf8")
                json.dump(cookies, json_cookies, indent=3, ensure_ascii=False)
                json_cookies.close()

                flag = True

        return flag
