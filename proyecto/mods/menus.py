from .gen_cerkey import *
from .create_address import *
from .smart_contract_actions import *
import time


def contract_menu():
    options = ['Deploy Contract', 'Interact Functions', 'Call Functions', 'Exit']
    op = 0
    while op != 4:
        print('\n\n---Que desea hacer?---')
        for x in range(len(options)):
            print(f'{x + 1}. {options[x]}')
        op = int(input('op: '))
        if op == 1:
            deploy('0xb01b81D69e18106d7Bbe5d16770d91fEf8b8a1e6', '0x919a44b8ab58295d2437da75f83437ee11710274d8937024cea4b406e2c38f92')
        if op == 2:
            interact('0xe185bAF6Ef527c8998dba2338BD8a5648b24Afb1', '5fb08e5ec41b8051325b78f2d8a24b4a48968556b36250e2df759e6a197a4c18')
        elif op == 3:
            call('0xe185bAF6Ef527c8998dba2338BD8a5648b24Afb1', '5fb08e5ec41b8051325b78f2d8a24b4a48968556b36250e2df759e6a197a4c18')
        elif op == 4:
            op = 4


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
        if result:
            print('Sesión iniciada correctamente')
            time.sleep(3)
            os.system('cls')
            contract_menu()
        else:
            print('Usuario y/o contraseña incorrecto(s)')
            time.sleep(3)
            os.system('cls')
            main_menu()
    elif op == 2:
        user = str(input("Usuario: "))
        address, privKey = create_account()
        register(user, address, privKey)
        print(f'Usuario {user} registrado correctamente')
        print('Guarda tu private key porque se borrará la pantalla en 15 segundos')
        time.sleep(15)
        os.system('cls')
        main_menu()
    else:
        print("opción inválida")
