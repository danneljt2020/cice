import json
from user import User
import stdiomask
from cryptography.fernet import Fernet

key = Fernet.generate_key()

# read the json file
def get_data_users():
    with open("user.json", encoding="utf8") as file:
        return json.load(file)


# write the json file
def write_data(data_json):
    with open("user.json", mode="w", encoding="utf8") as file:
        json.dump(data_json, file, ensure_ascii=False, indent=4)


def verify_exit(new_username):
    users = get_data_users()["users"]
    flag = False
    for user in users:
        if user["username"].lower() == new_username.lower():
            flag = True
    return flag


def add_user(user_obj):
    # fernet = Fernet(key)
    flag = True
    users = get_data_users()
    # encript_pass = fernet.encrypt(user_obj.passw.encode())
    new_user = {
      "pk": len(users["users"]) + 1,
      "username": user_obj.username,
      "name": user_obj.name,
      "pass": user_obj.passw
    }

    users["users"].append(new_user)
    write_data(users)
    return flag


def login(username, passw):
    # fernet = Fernet(key)
    users = get_data_users()["users"]
    flag = False
    for user in users:
        if user["username"].lower() == username.lower():
            # passw_ver = fernet.decrypt(bytes(user["pass"], encoding='utf8')).decode()
            if user["pass"] == passw:
                flag = True
    return flag


def menu():
    user = "r"
    menu = ['1', '2', 'Q', 'q']
    while user.lower() != "q":
        print("Bienvenido a Registro de Personas".center(50, "-"))
        print("1. Registro")
        print("2. Acceder")
        print("Presione la letra Q para salir")
        option_menu = input(":")

        if option_menu in menu:
            if option_menu == "1":
                print("Introduzca sus datos para el registro".center(50, "-"))
                condition = True
                username = "no_user"
                while condition:
                    username = input("Usuario:")
                    if verify_exit(username):
                        print("Ya tenemos un usuario registrado como:", username)
                    else:
                        condition = False

                name = input("Nombre:")
                passw = stdiomask.getpass('Password:')
                new_user = User(username, name, passw)

                add_user(new_user)
                print("Se ha registrado satisfactoriamente el usuario:", username)

            if option_menu == "2":
                print("Introduzca sus credenciales de acceso".center(50, "-"))
                username = input("Usuario:")
                passw = stdiomask.getpass('Password:')

                if login(username, passw):
                    print("SUCCESSFUL")
                else:
                    print("Bads redentials")

            elif option_menu == "q":
                print("Hasta la Proxima!!!".center(40, "-"))
                break
        else:
            print("Ha seleccionado una Opcion no valida! USE ESPEJUELOS")


def main():
    # log = login()
    # if log:
    menu()

main()
#
# message = "hello geeks"
#
# fernet1 = Fernet(key)
# fernet2 = Fernet(key)
#
#
# encMessage = fernet1.encrypt(message.encode())
#
# print("original string: ", message)
# print("encrypted string: ", encMessage)
#
#
# decMessage = fernet2.decrypt(encMessage).decode()
#
# print("decrypted string: ", decMessage)
