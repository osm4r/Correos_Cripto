import requests
from web3 import Web3
import os

def requestToGeth():
    # create persistent HTTP connection
    session = requests.Session()
    # as defined in https://github.com/ethereum/wiki/wiki/JSON-RPC#net_version
    method = 'net_version'
    params = []
    payload= {"jsonrpc":"2.0",
            "method":method,
            "params":params,
            "id":1}
    headers = {'Content-type': 'application/json'}
    response = session.post('HTTP://localhost:7545', json=payload, headers=headers)
    print('raw json response: {}'.format(response.json()))
    print('network id: {}'.format(response.json()['result']))


def get_account_number():
    if not os.path.isdir("usuarios"):
        return 0

    users = os.listdir('usuarios')
    index = len(users)
    return index


def create_account():
    # w3 = web3.Web3()
    w3 = Web3(Web3.HTTPProvider("http://localhost:7545"))
    # myAccount = w3.eth.account.create()
    w3.eth.account.enable_unaudited_hdwallet_features()
    index = get_account_number()
    myAccount = w3.eth.account.from_mnemonic("vocal misery visual antenna swift crane derive calm name excess suspect oil", account_path = f"m/44'/60'/0'/0/{index}")
    myAddress = myAccount.address
    myPrivateKey = myAccount.privateKey
    print('Address: {}'.format(myAccount.address))
    print('Private key (NO COMPARTIR): {}'.format(myAccount.privateKey.hex()))
    print('***En el inicio de sesión se pide Usuario y Private Key***')
    return myAddress, myPrivateKey.hex()


# requestToGeth()
# address, privKey = getKeys()
# print('address:', address)
# print('private key:', privKey)