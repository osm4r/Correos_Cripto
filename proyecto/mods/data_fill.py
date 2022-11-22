from web3 import Web3
from .create_address import *
import json


rpcServer, chain_id, mnemonic = get_ganache_config()
w3 = Web3(Web3.HTTPProvider(rpcServer))


def show_users(address):
    print('My Address:', address)
    print('Balance:', w3.eth.get_balance(address), 'wei')

    cant_cuentas = get_account_number()
    cuentas = w3.eth.accounts

    with open('usernames.txt', 'r') as file:
        file_data = file.read()
        usernames = file_data.split('\n')
        usernames.pop()

    print('\n\nCuentas')
    for x in range(cant_cuentas):
        print(f'{x}:\t{usernames[x]}\t{cuentas[x]}\t{w3.eth.get_balance(cuentas[x])}')


def get_enviarCorreo_data(address):
    show_users(address)
    #Pantalla datos del correo
    nreceiver = int(input('¿A qué usuario desea enviarle el correo?: '))
    receiver = w3.eth.accounts[nreceiver]
    subject = str(input('Asunto: '))
    body = str(input('Cuerpo del correo: '))
    return subject, body, receiver


def save_correos(user, correos, tipo):
    dict_correos = {}
    campos = ['Remitente', 'Asunto', 'Body', 'Fecha', 'Destinatario']
    for x in range(len(correos)):
        dict_correos[x] = {}
        for y in range(len(correos[x])):
            dict_correos[x][campos[y]] = correos[x][y]

    if tipo == 1:
        with open(f"usuarios/{user}/correos_recibidos.json", "w") as file:
            file.write(json.dumps(dict_correos, indent=4))
    elif tipo == 2:
        with open(f"usuarios/{user}/correos_enviados.json", "w") as file:
            file.write(json.dumps(dict_correos, indent=4))
    else:
        dict_correos = {}
        with open(f"usuarios/{user}/correos_enviados.json", "w") as file:
            file.write(json.dumps(dict_correos, indent=4))

    return dict_correos
