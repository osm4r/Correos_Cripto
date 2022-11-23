from .gen_cerkey import *
from .create_address import *
from .smart_contract_actions import *
from .data_fill import *
import time


def contract_menu(user, address, privKey):
    op = 0
    while op != 999:
        if os.path.isfile(f"contracts/CorreoContract/CorreoContract.json"):
            #pantalla con contract
            options = ['Enviar Correo', 'Ver correos recibidos', 'Ver correos enviados' , 'Eliminar bandeja de entrada', 'Exit']
        else:
            #pantalla sin contract
            options = ['Deploy Contract', 'Exit']
        print('\n\n---ACCIONES DE SMART CONTRACT---')
        for x in range(len(options)):
            print(f'{x + 1}. {options[x]}')
        op = int(input('op: '))
        if op == 1 and len(options) == 2:
            deploy(address, privKey)
        if op == 1 and len(options) == 5:
            interact_enviarCorreo(address, privKey)
        elif op == 2 and len(options) == 2:
            op = 999
        elif op == 2 and len(options) == 5:
            call_leerCorreosRecibidos(user, address)
        elif op == 3 and len(options) == 5:
            call_leerBandejaEntrada(user, address)
        elif op == 4 and len(options) == 5:
            call_eliminarBandejaEntrada(user, address)
        elif op == 5 and len(options) == 5:
            op = 999


def main_menu():
    #Pantalla login
    print("---LOGIN---") 
    print("1. Iniciar sesión")
    print("2. Registrarse")
    op = int(input("op: "))
    if op == 1:
        #pantalla iniciar sesion
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
        #Pantalla Registrar
        user = str(input("Usuario: "))
        address, privKey = create_account()
        register(user, address, privKey)
        print(f'Usuario {user} registrado correctamente')
        print('Guarda tu private key porque se borrará la pantalla en 8 segundos')

        with open(f'usernames.txt', 'a') as file:
            file.write(f'{user}\n')
        #BORRAR ESTO
        with open('passwords.txt', 'a') as file:
            file.write(user + '\t' + address + '\t' + privKey + '\n')
        #HASTA AQUI

        time.sleep(8)
        os.system('cls')
        contract_menu(user, address, privKey)
    else:
        print("opción inválida")
