from web3 import Web3
import os


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
    myAccount = w3.eth.account.from_mnemonic("write chicken noise expand album valley picture cover occur quote random step", account_path = f"m/44'/60'/0'/0/{index}")
    myAddress = myAccount.address
    myPrivateKey = myAccount.privateKey
    print('Address: {}'.format(myAccount.address))
    print('Private key (NO COMPARTIR): {}'.format(myAccount.privateKey.hex()))
    return myAddress, myPrivateKey.hex()
