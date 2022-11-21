import json
from pprint import pprint
from solcx import compile_standard, install_solc
from web3 import Web3


w3 = Web3(Web3.HTTPProvider("http://localhost:7545"))
chain_id = 1337


def get_abi():
    with open("contracts/CorreoContract/CorreoContract.json", "r") as file:
        compiled_sol = json.load(file)
    abi = json.loads(compiled_sol["contracts"]["contracts/CorreoContract/CorreoContract.sol"]["Correo_contract"]["metadata"])["output"]["abi"]
    return abi


'''def get_contract_address():
    with open('contracts/CorreoContract/address.txt', 'r') as file:
        address = file.read().strip()
    return address'''


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
    # pprint(compiled_sol)
    with open("contracts/CorreoContract/CorreoContract.json", "w") as file:
        # json.dump(compiled_sol, file)
        file.write(json.dumps(compiled_sol, indent=4))

    bytecode = compiled_sol["contracts"]["contracts/CorreoContract/CorreoContract.sol"]["Correo_contract"]["evm"]["bytecode"]["object"]
    abi = json.loads(compiled_sol["contracts"]["contracts/CorreoContract/CorreoContract.sol"]["Correo_contract"]["metadata"])["output"]["abi"]
    
    # For connecting to ganache
    # w3 = Web3(Web3.HTTPProvider("http://localhost:7545"))
    # chain_id = 1337
    # address = "0x10f1AEA2815e23D387E93b5fFe329877224a3905"
    # private_key = "37b61a20694ab7e489b00fcb516630986bbc92343a28cec72ecc4d61de85d7f6"
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
    return tx_receipt.contractAddress

    
def interact(address, private_key, contract_address):
    abi = get_abi()
    # contract_address = get_contract_address()
    CorreoContract = w3.eth.contract(contract_address, abi=abi) # address=tx_receipt.contractAddress, 
    nonce = w3.eth.getTransactionCount(address)
    enviarCorreo = CorreoContract.functions.enviarCorreo(
        "Asunto", "Body del correo xd", "0x4b244010137df1415842855b94943498F66D29E3"
    ).buildTransaction({"chainId": chain_id, "from": address, "gasPrice": w3.eth.gas_price, "nonce": nonce})
    

    # Sign the transaction
    sign_function= w3.eth.account.sign_transaction(
        enviarCorreo, private_key=private_key
    )
    # Send the transaction
    send_function = w3.eth.send_raw_transaction(sign_function.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(send_function)
    print(tx_receipt)


def call(contract_address):
    abi = get_abi()
    # contract_address = get_contract_address()
    CorreoContract = w3.eth.contract(contract_address, abi=abi)
    # nonce = w3.eth.getTransactionCount(address)
    leerCorreo = CorreoContract.functions.leerCorreo().call()
    print(leerCorreo)
    # menu(True)


def initialtransaction(address, private_key):
    print('Address: ', address)
    print(w3.eth.get_balance(address))
    print('Coinbase: ', w3.eth.coinbase)
    print(w3.eth.get_balance(w3.eth.coinbase))

    cuentas = w3.eth.accounts
    print('\n\nCuentas')
    for x in range(len(cuentas)):
        print(f'{x}: {cuentas[x]}   {w3.eth.get_balance(cuentas[x])}')
