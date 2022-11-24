from .gen_cerkey import *
from .create_address import *
from .smart_contract_actions import *
from .data_fill import *
import time
from pprint import pprint


def contract_menu(user, address, privKey):
    op = 0
    while op != 999:
        if os.path.isfile(f"contracts/CorreoContract/CorreoContract.json"):
            options = ['Enviar Correo', 'Ver correos recibidos', 'Ver correos enviados' , 'Eliminar bandeja de entrada', 'Exit']
        else:
            options = ['Deploy Contract', 'Exit']
        print('\n\n---ACCIONES DE SMART CONTRACT---')
        for x in range(len(options)):
            print(f'{x + 1}. {options[x]}')
        op = int(input('op: '))
        if op == 1 and len(options) == 2:
            pdeploy = deploy(address, privKey)
            pprint(pdeploy)
        elif op == 1 and len(options) == 5:
            subject, body, receiver = get_enviarCorreo_data(address)
            interact_enviarCorreo(address, privKey, subject, body, receiver)
        elif op == 2 and len(options) == 2:
            op = 999
        elif op == 2 and len(options) == 5:
            pleerCorreosRecibidos = call_leerCorreosRecibidos(user, address)
            pprint(pleerCorreosRecibidos)
        elif op == 3 and len(options) == 5:
            pleerBandejaEntrada = call_leerBandejaEntrada(user, address)
            pprint(pleerBandejaEntrada)
        elif op == 4 and len(options) == 5:
            pcall_eliminarBandejaEntrada = call_eliminarBandejaEntrada(user, address)
            pprint(pcall_eliminarBandejaEntrada)
        elif op == 5 and len(options) == 5:
            op = 999


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
        print('Guarda tu private key porque se borrará la pantalla en 8 segundos')

        with open(f'usernames.txt', 'a') as file:
            file.write(f'{user}\n')
            
        time.sleep(8)
        os.system('cls')
        contract_menu(user, address, privKey)
    else:
        print("opción inválida")
