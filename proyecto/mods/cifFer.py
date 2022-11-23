#Importar
from cryptography.fernet import Fernet  #JsonCorreos
import json
from ast import literal_eval


#--------- FERNET JSONCORREOS ---------#

#GENERAR LLAVE
def FernetK(user):
  #Generar Llave
  key = Fernet.generate_key()
  #Guardar Llave
  with open(f'usuarios/{user}.key', 'wb') as filekey:
    filekey.write(key)
  return key


#CIFRAR DICCIONARIO Y GUARDAR EN JSON
def FernetC(DictC, user, key):
  fernet = Fernet(key)
  original = json.dumps(DictC).encode('utf-8')
  encrypted = fernet.encrypt(original)
  with open(f'usuarios/{user}.json', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)

#DESCIFRAR JSON Y GUARDAR EN DICCIONARIO
def FernetD(user):
  with open(f'usuarios/{user}.key', 'rb') as filekey: 
    key = filekey.read()
  fernet = Fernet(key)
  with open(f'usuarios/{user}.json', 'rb') as enc_file: 
    encrypted = enc_file.read()
  decrypted = fernet.decrypt(encrypted)
  # print(type(decrypted))
  # print(decrypted)
  dict_dec = literal_eval(decrypted.decode('utf-8'))
  # print(type(dict_dec))
  # print(dict_dec)
  return dict_dec

'''diccionario = {1: 'asdasd', 2: 'asdsa'}
key = FernetK()
FernetC(diccionario, 'Osmar', key)'''

'''diccionario2 = FernetD('ROmeo')
print(diccionario2)'''