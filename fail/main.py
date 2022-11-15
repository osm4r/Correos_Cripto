from mods import *


def main():
    requestToGeth()
    address, privKey = getKeys()
    print('address:', address)
    print('private key:', privKey)


if __name__ == '__main__':
    main()