from .gen_cerkey import *
from .create_address import *
from .smart_contract_actions import *
from .data_fill import *
import time
from pprint import pprint
from .mots_tkinter import *
from .mods_tkinter2 import *


def contract_menu(user, address, privKey):
    op = 0
    while op != 999:
        if os.path.isfile(f"contracts/CorreoContract/CorreoContract.json"):
            #pantalla con contract
            menu(user, address, privKey)
            options = ['Enviar Correo', 'Ver correos recibidos', 'Ver correos enviados' , 'Eliminar bandeja de entrada', 'Exit']
        else:
            #pantalla sin contract
            menu2(user, address, privKey)
            options = ['Deploy Contract', 'Exit']
            menu(user, address, privKey)
        '''print('\n\n---ACCIONES DE SMART CONTRACT---')
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
            op = 999'''


def main_menu():
    #Pantalla login
    user, address, privkey = ventana_inicio()
    print(user, address, privkey)
    contract_menu(user, address, privkey)
    '''print("---LOGIN---") 
    print("1. Iniciar sesi??n")
    print("2. Registrarse")
    op = int(input("op: "))
    if op == 1:
        #pantalla iniciar sesion
        user = str(input("Usuario: "))
        privKey = str(getpass("Private Key: "))
        result = login(user, privKey)
        print(result)
        if result:
            print('Sesi??n iniciada correctamente')
            time.sleep(3)
            os.system('cls')
            address = get_user_address(user)
            contract_menu(user, address, privKey)
        else:
            print('Usuario y/o contrase??a incorrecto(s)')
            time.sleep(3)
            os.system('cls')
            main_menu()
    elif op == 2:
        #Pantalla Registrar
        user = str(input("Usuario: "))
        address, privKey = create_account()
        register(user, address, privKey)
        print(f'Usuario {user} registrado correctamente')
        print('Guarda tu private key porque se borrar?? la pantalla en 8 segundos')

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
        print("opci??n inv??lida")'''
