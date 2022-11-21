import requests
from web3 import Web3

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


def create_account():
    # w3 = web3.Web3()
    w3 = Web3(Web3.HTTPProvider("http://localhost:7545"))
    # myAccount = w3.eth.account.create()
    w3.eth.account.enable_unaudited_hdwallet_features()
    myAccount = w3.eth.account.from_mnemonic("spy emotion during shock evoke cluster nature dawn capable faculty trial long") #AQUI ME QUEDE MODIFICAR ESO DE CREAR CUENTA
    print(myAccount)
    myAddress = myAccount.address
    myPrivateKey = myAccount.privateKey
    print('Address: {}'.format(myAccount.address))
    print('Private key (SAVE BUT NOT SHARE THIS): {}'.format(myAccount.privateKey.hex()))
    print('***En el inicio de sesión se pide Usuario y Private Key***')
    return myAddress, myPrivateKey.hex()


def crea():
    w3 = web3.Web3()
    w3.eth.account.enable_unaudited_hdwallet_features()
    # account = web3.eth.account.from_mnemonic(my_mnemonic, account_path="m/44'/60'/0'/0/0")
    account = w3.eth.account.create_with_mnemonic("copy bless artwork pretty obey love off pause athlete reopen absurd shine", account_path="m/44'/60'/0'/0/0")
    myAddress = account.address
    print(myAddress)


# requestToGeth()
# address, privKey = getKeys()
# print('address:', address)
# print('private key:', privKey)