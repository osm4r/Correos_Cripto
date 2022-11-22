from web3 import Web3
from .create_address import *
import json

w3 = Web3(Web3.HTTPProvider("http://localhost:7545"))

def show_users(address):
    print('My Address: ', address)
    print('Balance', w3.eth.get_balance(address))

    cant_cuentas = get_account_number()
    cuentas = w3.eth.accounts
    print('\n\nCuentas')
    for x in range(cant_cuentas):
        print(f'{x}: {cuentas[x]}   {w3.eth.get_balance(cuentas[x])}')


def get_enviarCorreo_data(address):
    show_users(address)
    nreceiver = int(input('¿A qué usuario desea enviarle el correo?: '))
    receiver = w3.eth.accounts[nreceiver]
    subject = str(input('Asunto: '))
    body = str(input('Cuerpo del correo: '))
    return subject, body, receiver


def save_correos(user, correos):
    dict_correos = {}
    campos = ['Asunto', 'Body']
    for x in range(len(correos)):
        dict_correos[x] = {}
        for y in range(len(correos[x])):
            dict_correos[x][campos[y]] = correos[x][y]

    with open(f"usuarios/{user}/last_call_correos.json", "w") as file:
        file.write(json.dumps(dict_correos, indent=4))

    return dict_correos
