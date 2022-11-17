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
    transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)
    print(f"Done! Contract deployed to {transaction_receipt.contractAddress}")

    
def interact(address, private_key):
    abi = get_abi()
    contact_list = w3.eth.contract('0xb46d64dA44674Feb8c522b557967362570745a10', abi=abi) # address=transaction_receipt.contractAddress, 
    nonce = w3.eth.getTransactionCount(address)
    store_contact = contact_list.functions.enviarCorreo(
        "Asunto", "Body del correo xd", "0x37BdcD6908178ad42c281f20c9d458eAd567f112"
    ).buildTransaction({"chainId": chain_id, "from": address, "gasPrice": w3.eth.gas_price, "nonce": nonce})
    

    # Sign the transaction
    sign_store_contact = w3.eth.account.sign_transaction(
        store_contact, private_key=private_key
    )
    # Send the transaction
    send_store_contact = w3.eth.send_raw_transaction(sign_store_contact.rawTransaction)
    transaction_receipt = w3.eth.wait_for_transaction_receipt(send_store_contact)
    print(transaction_receipt)


def call(address, private_key):
    abi = get_abi()
    contact_list = w3.eth.contract('0xb46d64dA44674Feb8c522b557967362570745a10', abi=abi)
    print(contact_list.functions.leerCorreo().call())
    # menu(True)
