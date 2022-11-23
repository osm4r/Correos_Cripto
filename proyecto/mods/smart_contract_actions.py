import json
from pprint import pprint
from solcx import compile_standard, install_solc
from web3 import Web3
from datetime import datetime
#from cryptography.fernet import Fernet
from .data_fill import *
from .cifB64 import *


rpcServer, chain_id, mnemonic = get_ganache_config()
w3 = Web3(Web3.HTTPProvider(rpcServer))


def get_abi():
    compiled_sol = DecB('contracts/CorreoContract/CorreoContract.json')
    '''with open(f"contracts/CorreoContract/CorreoContract.json", "r") as file:
        compiled_sol = json.load(file)'''
    abi = json.loads(compiled_sol["contracts"]["contracts/CorreoContract/CorreoContract.sol"]["Correo_contract"]["metadata"])["output"]["abi"]
    return abi


def get_contract_address():
    compiled_sol = DecB('contracts/CorreoContract/CorreoContract.json')
    '''with open(f"contracts/CorreoContract/CorreoContract.json", "r") as file:
        compiled_sol = json.load(file)'''
    contract_address = compiled_sol['contractAddress']
    return contract_address


def deploy(address, private_key):
    with open("contracts/CorreoContract/CorreoContract.sol", "r") as file:
        contact_list_file = file.read()

    install_solc("0.8.0")
    compiled_sol = compile_standard(
        {
            "language": "Solidity",
            "sources": {"contracts/CorreoContract/CorreoContract.sol": {"content": contact_list_file}},
            "settings": {
                "outputSelection": {
                    "*": {
                        "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"] # output needed to interact with and deploy contract 
                    }
                }
            },
        },
        solc_version="0.8.0",
    )

    bytecode = compiled_sol["contracts"]["contracts/CorreoContract/CorreoContract.sol"]["Correo_contract"]["evm"]["bytecode"]["object"]
    abi = json.loads(compiled_sol["contracts"]["contracts/CorreoContract/CorreoContract.sol"]["Correo_contract"]["metadata"])["output"]["abi"]
    
    # Create the contract in Python
    CorreoContract = w3.eth.contract(abi=abi, bytecode=bytecode)
    # Get the number of latest transaction
    nonce = w3.eth.getTransactionCount(address)


    # build transaction
    tx = CorreoContract.constructor().buildTransaction(
        {
            "chainId": chain_id,
            "gasPrice": w3.eth.gas_price,
            "from": address,
            "nonce": nonce,
        }
    )
    # Sign the transaction
    sign_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
    print("Deploying Contract!")
    # Send the transaction
    tx_hash = w3.eth.send_raw_transaction(sign_tx.rawTransaction)
    # Wait for the transaction to be mined, and get the transaction receipt
    print("Waiting for transaction to finish...")
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    # print(f"Done! Contract deployed to {tx_receipt.contractAddress}")

    compiled_sol['contractAddress'] = tx_receipt.contractAddress

    CifB(compiled_sol, 'contracts/CorreoContract/CorreoContract.json')
    '''with open(f"contracts/CorreoContract/CorreoContract.json", "w") as file:
        file.write(json.dumps(compiled_sol, indent=4))'''

    return f"Done! Contract deployed to {tx_receipt.contractAddress}"

    
def interact_enviarCorreo(address, private_key, subject, body, receiver):
    abi = get_abi()
    contract_address = get_contract_address()
    # print('Contract address: ', contract_address)
    CorreoContract = w3.eth.contract(contract_address, abi=abi) # address=tx_receipt.contractAddress, 
    nonce = w3.eth.getTransactionCount(address)
    now = datetime.now()
    date = now.strftime("%d/%m/%Y, %H:%M:%S")
    enviarCorreo = CorreoContract.functions.enviarCorreo(
        address, subject, body, date, receiver
    ).buildTransaction({"chainId": chain_id, "from": address, "gasPrice": w3.eth.gas_price, "nonce": nonce})

    # Sign the transaction
    sign_function= w3.eth.account.sign_transaction(
        enviarCorreo, private_key=private_key
    )
    # Send the transaction
    send_function = w3.eth.send_raw_transaction(sign_function.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(send_function)
    pprint(tx_receipt)


def call_leerCorreosRecibidos(username, address):
    abi = get_abi()
    contract_address = get_contract_address()
    CorreoContract = w3.eth.contract(contract_address, abi=abi)
    leerCorreosRecibidos = CorreoContract.functions.leerCorreosRecibidos(address).call()
    print(leerCorreosRecibidos)
    # pprint(save_correos(username, leerCorreosRecibidos, 1))
    return save_correos(username, leerCorreosRecibidos, 1)


def call_leerBandejaEntrada(username, address):
    abi = get_abi()
    contract_address = get_contract_address()
    CorreoContract = w3.eth.contract(contract_address, abi=abi)
    leerBandejaEntrada = CorreoContract.functions.leerBandejaEntrada(address).call()
    print(leerBandejaEntrada)
    # pprint(save_correos(username, leerBandejaEntrada, 2))
    return save_correos(username, leerBandejaEntrada, 2)


def call_eliminarBandejaEntrada(username,private_key, address):
    abi = get_abi()
    contract_address = get_contract_address()
    CorreoContract = w3.eth.contract(contract_address, abi=abi)
    nonce = w3.eth.getTransactionCount(address)
    eliminarBandejaEntrada = CorreoContract.functions.eliminarBandejaEntrada(address).buildTransaction({"chainId": chain_id, "from": address, "gasPrice": w3.eth.gas_price, "nonce": nonce})
    sign_function= w3.eth.account.sign_transaction(
        eliminarBandejaEntrada, private_key=private_key
    )
    # Send the transaction
    send_function = w3.eth.send_raw_transaction(sign_function.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(send_function)
    pprint(tx_receipt)
    dic= {}
    return save_correos(username, dic, 3)
    '''with open(f"usuarios/{username}/correos_enviados.json", "w") as file:
        file.write(json.dumps(, indent=4))'''
