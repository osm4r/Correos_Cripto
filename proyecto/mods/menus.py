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
            deploy('0x4b244010137df1415842855b94943498F66D29E3', '0x4b244010137df1415842855b94943498F66D29E3')
        if op == 2:
            interact('0xe185bAF6Ef527c8998dba2338BD8a5648b24Afb1', '5fb08e5ec41b8051325b78f2d8a24b4a48968556b36250e2df759e6a197a4c18')
        elif op == 3:
            call('0x4b244010137df1415842855b94943498F66D29E3', '0xaae11823d2c13b641c91bfd6badbd8e19b96e296281d5a6c3a33c97431bff9b5')
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
