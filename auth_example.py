from samba.common import raw_input


def login():
    user = raw_input("Username: ")
    passw = raw_input("Password: ")
    f = open("users.txt", "r")
    for line in f.readlines():
        us, pw = line.strip().split("|")
        if (user in us) and (passw in pw):
            print("Login successful!")
            return True
    print("Wrong username/password")
    return False


def menu():
    pass


def main():
    log = login()
    if log:
        menu()

main()