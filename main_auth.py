import json
import stdiomask
from user import User, Auth


'''
some_value + secret + random
'''

DB = "./user.json"


def get_users(json_file):
    with open(json_file, encoding="utf8") as file:
        return json.load(file)


def create_user(data, json_file):
    with open(json_file, "w", encoding="utf8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


auth = Auth(DB)
user = ""
while user != "q":
    print("1. Crear usuario")
    print("2. Log in")

    if auth.verify_token():
        print("3. Dashboard")
        print("4. Logout")

    user = input("Seleccione: ")
    if user == "1":
        user_name = input("Usuario: ")
        user_pwd = stdiomask.getpass('Password:')
        user_instance = User(user_name, user_pwd)
        auth.create_user(user_instance.user_dict)

    elif user == "2":
        user_name = input("Usuario: ")
        user_pwd = stdiomask.getpass('Password:')
        user_instance = User(user_name, user_pwd)
        if auth.log_in(user_instance):
            print("Te has logueado satisfactoriamente")
        else:
            print("NO se encuentra registrado en el sistema")

    elif user == "3":
        print("Menu Autorizado")

    elif user == "4":
        empty = {"tokens": {}}
        json_cookies = open('cookies.json', "w", encoding="utf8")
        json.dump(empty, json_cookies, indent=3, ensure_ascii=False)
        json_cookies.close()
        print("Adios!!")
