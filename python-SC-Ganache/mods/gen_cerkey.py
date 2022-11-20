import base64
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
from nacl.signing import SigningKey
from getpass import getpass
import os


def encrypt(data: bytes, password: bytes):
    encrypted_array: list = []
    i=0
    for d in data:
        encrypted_array.append(((d + password[i]) % 256).to_bytes(1, "big"))
        i+=1
        if i >= len(password):
            i=0
    return b''.join(encrypted_array)


def decrypt(data: bytes, password: bytes):
    decrypted_array: list = []
    i=0
    for d in data:
        decrypted_array.append(((d - password[i]) % 256).to_bytes(1, "big"))
        i+=1
        if i >= len(password):
            i=0
    return b''.join(decrypted_array)


def write(data: bytes, path: str):
    try:
        with open(f"usuarios/{path}", "wb") as file:
            file.write(data)
        print(f"Archivo {path} creado correctamente")
    except:
        print(f"Error al crear el archivo {path}")


def read(path: bytes):
    if os.path.isfile(f"usuarios/{path}"):
        with open(f"usuarios/{path}", "rb") as file:
            return file.read()
    else:
        print(f"Error: El archivo {path} no existe")
        quit()


def genKeyPair():
    kp = SigningKey.generate()
    return kp._seed


def bytesToString(data: bytes):
    return base64.encodebytes(data).decode("utf-8")


def stringToBytes(data: str):
    return base64.decodebytes(data.encode("utf-8"))


def sign(msg: str, seed: bytes):
    sign_key = SigningKey(seed)
    signed_raw = sign_key.sign(msg.encode("utf-8"))
    return signed_raw


def register(username: str, address: str, password: str):
    seed: bytes = genKeyPair()
    signed: dict = sign(address, seed)
    if not os.path.isdir("usuarios"):
        os.mkdir("usuarios")
    if not os.path.isdir(f"usuarios/{username}"):
        os.mkdir(f"usuarios/{username}")
    else:
        print("Error: Nombre de usuario inválido")
        quit()
    write(encrypt(seed, password.encode("utf-8")), f"{username}/{address}.key")
    # print(signed)
    write(signed, f"{username}/{address}.cer")


def login(username: str, address: str, password: str):
    seed: bytes = decrypt(read(f"{username}/{address}.key"), password.encode("utf-8"))
    signed_raw: bytes = read(f"{username}/{address}.cer")
    # print(signed_raw)
    verify_key = SigningKey(seed).verify_key
    # print(verify_key._key)
    try:        
        verify_key.verify(signed_raw)
        return True
    except BadSignatureError:
        return False



