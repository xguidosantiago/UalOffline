import scripts.mainmenu as m
import scripts.banner as b
import hashlib
import os
import json
import getpass

base_path = os.path.dirname(os.path.abspath(__file__))
path_users = os.path.join(base_path, 'db', 'users.json')

def hash_string(s):
    return hashlib.sha256(s.encode()).hexdigest()

def login():
    os.system("cls")
    b.clsBanner()
    usuario = input("Usuario: ")
    password = getpass.getpass("Contraseña: ")

    hashed_pass = hash_string(password)

    with open(path_users, "r") as u:
        lstUsers = json.load(u)
        for user in lstUsers:
            if user["user"] == usuario and user["password"] == hashed_pass:
                m.showmenu()
        else:
            input("usuario incorrecto, intente nuevamente")
            login()

if __name__ == "__main__":
    
    login()
    
        