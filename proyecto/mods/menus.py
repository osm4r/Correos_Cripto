from .gen_cerkey import *
from .create_address import *
from .smart_contract_actions import *
import time


def contract_menu(address, privKey):
    if os.path.isdir("contracts/CorreoContract/CorreoContract.json"):
        options = ['Deploy Contract', 'Interact Functions', 'Call Functions', 'Exit']
    else:
        options = ['Deploy Contract', 'Exit', '9. InitialTRANSACTION']
    op = 0
    while op != 4:
        print('\n\n---ACCIONES DE SMART CONTRACT---')
        for x in range(len(options)):
            print(f'{x + 1}. {options[x]}')
        op = int(input('op: '))
        if op == 1:
            contract_address = deploy(address, privKey)
        if op == 2 and len(options) == 4:
            interact(address, privKey, contract_address)
        elif op == 3 and len(options) == 4:
            call(contract_address)
        elif op == 4 and len(options) == 4:
            op = 4
        elif op == 2 and len(options) == 2:
            op = 4
        elif op == 9:
            initialtransaction(address, privKey)


def main_menu():
    print("---LOGIN---")
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
            address = get_user_address(user)
            contract_menu(address, privKey)
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
        contract_menu(address, privKey)
    else:
        print("opción inválida")
