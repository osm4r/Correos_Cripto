from .gen_cerkey import *
from .create_address import *
from .smart_contract_actions import *
from getpass import getpass

def main_menu():
    print("---Elige una opción---")
    print("1. Iniciar sesión")
    print("2. Registrarse")
    op = int(input("op: "))
    if op == 1:
        user = str(input("Usuario: "))
        privKey = str(getpass("Private Key: "))
        result = login(user, privKey)
        print(result)
    elif op == 2:
        user = str(input("Usuario: "))
        print(f'Usuario: {user}')
        address, privKey = create_account()
        register(user, address, privKey)
    else:
        print("opción inválida")
