import requests
import web3


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


def getKeys():
    w3 = web3.Web3()
    # myAccount = w3.eth.personal.newAccount()
    myAccount = w3.eth.account.create()
    myAddress = myAccount.address
    myPrivateKey = myAccount.privateKey
    # print('my address is     : {}'.format(myAccount.address))
    # print('my private key is : {}'.format(myAccount.privateKey.hex()))
    return myAddress, myPrivateKey.hex()