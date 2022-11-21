import json
from pprint import pprint
from solcx import compile_standard, install_solc
from web3 import Web3
from .data_fill import *


w3 = Web3(Web3.HTTPProvider("http://localhost:7545"))
chain_id = 1337


def get_abi(username):
    with open(f"usuarios/{username}/CorreoContract.json", "r") as file:
        compiled_sol = json.load(file)
    abi = json.loads(compiled_sol["contracts"]["contracts/CorreoContract/CorreoContract.sol"]["Correo_contract"]["metadata"])["output"]["abi"]
    return abi


def get_contract_address(username):
    with open(f"usuarios/{username}/CorreoContract.json", "r") as file:
        compiled_sol = json.load(file)
    contract_address = compiled_sol['contractAddress']
    return contract_address


def deploy(username, address, private_key):
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
    print(f"Done! Contract deployed to {tx_receipt.contractAddress}")

    compiled_sol['contractAddress'] = tx_receipt.contractAddress
    with open(f"usuarios/{username}/CorreoContract.json", "w") as file:
        file.write(json.dumps(compiled_sol, indent=4))

    
def interact(username, address, private_key):
    subject, body, receiver = get_enviarCorreo_data(address)
    abi = get_abi(username)
    contract_address = get_contract_address(username)
    CorreoContract = w3.eth.contract(contract_address, abi=abi) # address=tx_receipt.contractAddress, 
    nonce = w3.eth.getTransactionCount(address)
    enviarCorreo = CorreoContract.functions.enviarCorreo(
        f"{subject}", f"{body}", f"{receiver}"
    ).buildTransaction({"chainId": chain_id, "from": address, "gasPrice": w3.eth.gas_price, "nonce": nonce})
    
    print(subject, body, receiver) # PENDIENTE, NO SALEN LOS CORREOSSSSSSSSSSS

    # Sign the transaction
    sign_function= w3.eth.account.sign_transaction(
        enviarCorreo, private_key=private_key
    )
    # Send the transaction
    send_function = w3.eth.send_raw_transaction(sign_function.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(send_function)
    print(tx_receipt)


def call(username):
    abi = get_abi(username)
    contract_address = get_contract_address(username)
    CorreoContract = w3.eth.contract(contract_address, abi=abi)
    leerCorreo = CorreoContract.functions.leerCorreo().call()
    print(leerCorreo)

