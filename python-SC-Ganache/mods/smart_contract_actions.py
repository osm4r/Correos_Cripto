from solcx import compile_standard, install_solc
from web3 import Web3
import json
from pprint import pprint

w3 = Web3(Web3.HTTPProvider("http://localhost:7545"))
chain_id = 1337


def deploy(address, private_key):
    with open("CorreoContract.sol", "r") as file:
        contact_list_file = file.read()

    install_solc("0.8.0")
    compiled_sol = compile_standard(
        {
            "language": "Solidity",
            "sources": {"CorreoContract.sol": {"content": contact_list_file}},
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
    with open("compiled_code.json", "w") as file:
        json.dump(compiled_sol, file)

    bytecode = compiled_sol["contracts"]["CorreoContract.sol"]["Correo_contract"]["evm"]["bytecode"]["object"]
    global abi
    abi = json.loads(compiled_sol["contracts"]["CorreoContract.sol"]["Correo_contract"]["metadata"])["output"]["abi"]
    
    # For connecting to ganache
    # w3 = Web3(Web3.HTTPProvider("http://localhost:7545"))
    # chain_id = 1337
    # address = "0x10f1AEA2815e23D387E93b5fFe329877224a3905"
    # private_key = "37b61a20694ab7e489b00fcb516630986bbc92343a28cec72ecc4d61de85d7f6"
    # Create the contract in Python
    ContactList = w3.eth.contract(abi=abi, bytecode=bytecode)
    # Get the number of latest transaction
    nonce = w3.eth.getTransactionCount(address)


    # build transaction
    transaction = ContactList.constructor().buildTransaction(
        {
            "chainId": chain_id,
            "gasPrice": w3.eth.gas_price,
            "from": address,
            "nonce": nonce,
        }
    )
    # Sign the transaction
    sign_transaction = w3.eth.account.sign_transaction(transaction, private_key=private_key)
    print("Deploying Contract!")
    # Send the transaction
    transaction_hash = w3.eth.send_raw_transaction(sign_transaction.rawTransaction)
    # Wait for the transaction to be mined, and get the transaction receipt
    print("Waiting for transaction to finish...")
    global transaction_receipt
    transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)
    print(f"Done! Contract deployed to {transaction_receipt.contractAddress}")

    contact_list = w3.eth.contract(address=transaction_receipt.contractAddress, abi=abi)
    return contact_list

    
def interact(contact_list, address, private_key):
    nonce = w3.eth.getTransactionCount(address)
    store_contact = contact_list.functions.enviarCorreo(
        "xdxdxd", "esto se envia al correo 1", "0xE922C4bbD20a24EDfD34B83F4175619DA0B1B94d"
    ).buildTransaction({"chainId": chain_id, "from": address, "gasPrice": w3.eth.gas_price, "nonce": nonce})
    

    # Sign the transaction
    sign_store_contact = w3.eth.account.sign_transaction(
        store_contact, private_key=private_key
    )
    # Send the transaction
    send_store_contact = w3.eth.send_raw_transaction(sign_store_contact.rawTransaction)
    transaction_receipt = w3.eth.wait_for_transaction_receipt(send_store_contact)
    print(transaction_receipt)
    menu(True)


def call(contact_list):
    print(contact_list.functions.leerCorreo().call())
    menu(True)


def menu(dep = False):
    options = ['Interact Functions', 'Call Functions', 'Exit']
    print('\n\n---Que desea hacer?---')
    for x in range(len(options)):
        print(f'{x + 1}. {options[x]}')
    op = int(input('op: '))
    if op < 3 and dep == False:
        global contact_list
        contact_list = deploy('0xE922C4bbD20a24EDfD34B83F4175619DA0B1B94d', 'ba850f0b002d14fb731fceedb9a5d4d36cca674daec5b14daf27666199e1a30f')
    if op == 1:
        interact(contact_list, '0xE922C4bbD20a24EDfD34B83F4175619DA0B1B94d', 'ba850f0b002d14fb731fceedb9a5d4d36cca674daec5b14daf27666199e1a30f')
    elif op == 2:
        call(contact_list)
    elif op == 3:
        quit()
    else:
        menu()