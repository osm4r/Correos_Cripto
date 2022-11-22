from .gen_cerkey import *
from .create_address import *
from .smart_contract_actions import *
from .data_fill import *
import time


def contract_menu(user, address, privKey):
    op = 0
    while op != 4:
        if os.path.isfile(f"contracts/CorreoContract/CorreoContract.json"):
            options = ['Enviar Correo', 'Leer Correo', 'Exit']
        else:
            options = ['Deploy Contract', 'Exit']
        print('\n\n---ACCIONES DE SMART CONTRACT---')
        for x in range(len(options)):
            print(f'{x + 1}. {options[x]}')
        op = int(input('op: '))
        if op == 1 and len(options) == 2:
            deploy(address, privKey)
        if op == 1 and len(options) == 3:
            interact(address, privKey)
        elif op == 2 and len(options) == 2:
            op = 4
        elif op == 2 and len(options) == 3:
            call(user, address)
        elif op == 3 and len(options) == 3:
            op = 4


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
            contract_menu(user, address, privKey)
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

        with open(f'usernames.txt', 'a') as file:
            file.write(f'{user}\n')
        #BORRAR ESTO
        with open('passwords.txt', 'a') as file:
            file.write(user + '\t' + address + '\t' + privKey + '\n')
        #HASTA AQUI

        time.sleep(15)
        os.system('cls')
        contract_menu(user, address, privKey)
    else:
        print("opción inválida")
