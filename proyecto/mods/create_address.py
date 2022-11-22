from web3 import Web3
import os
import configparser


def get_ganache_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    rpcServer = config['GANACHE']['RPCSERVER']
    chain_id = int(config['GANACHE']['CHAINID'])
    mnemonic = config["GANACHE"]['MNEMONIC']
    return rpcServer, chain_id, mnemonic


rpcServer, chain_id, mnemonic = get_ganache_config()
w3 = Web3(Web3.HTTPProvider(rpcServer))


def get_account_number():
    if not os.path.isdir("usuarios"):
        return 0

    users = os.listdir('usuarios')
    index = len(users)
    return index


def create_account():
    w3.eth.account.enable_unaudited_hdwallet_features()
    index = get_account_number()
    myAccount = w3.eth.account.from_mnemonic(mnemonic, account_path = f"m/44'/60'/0'/0/{index}")
    myAddress = myAccount.address
    myPrivateKey = myAccount.privateKey
    print('Address: {}'.format(myAccount.address))
    print('Private key (NO COMPARTIR): {}'.format(myAccount.privateKey.hex()))
    return myAddress, myPrivateKey.hex()
