#Importar
from cryptography.fernet import Fernet  #JsonCorreos
import json
from ast import literal_eval


#--------- FERNET JSONCORREOS ---------#

#GENERAR LLAVE
def FernetK():
  #Generar Llave
  key = Fernet.generate_key()
  #Guardar Llave
  with open('FileGen/filekey.key', 'wb') as filekey:
    filekey.write(key)
  return key


#CIFRAR DICCIONARIO Y GUARDAR EN JSON
def FernetC(DictC):
  with open('FileGen/filekey.key', 'rb') as filekey:
    key = filekey.read()
  fernet = Fernet(key)
  '''with open("FileGen/correo.json", "r") as file:
    original = json.load(file)'''
  original = json.dumps(DictC).encode('utf-8')
  encrypted = fernet.encrypt(original)
  with open('FileGen/Correo_Cifrado.enc', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)

#DESCIFRAR JSON Y GUARDAR EN DICCIONARIO
def FernetD():
  with open('FileGen/filekey.key', 'rb') as filekey: 
    key = filekey.read() 
  fernet = Fernet(key) 
  with open('FileGen/Correo_Cifrado.enc', 'rb') as enc_file: 
    encrypted = enc_file.read()
  decrypted = fernet.decrypt(encrypted)
  print(type(decrypted))
  print(decrypted)
  dict_dec = literal_eval(decrypted.decode('utf-8'))
  print(type(dict_dec))
  print(dict_dec)
  return dict_dec
  #with open('FileGen/Correo_Descifrado.json', 'wb') as dec_file:
    #dec_file.write(decrypted) 
#--------------------------------------#



#Dump
'''def Ejemplo(DictC):
  with open('FileGen/filekey.key', 'rb') as filekey:
    key = filekey.read()
  fernet = Fernet(key)
  original = json.dumps(DictC).encode('utf-8')
  print(type(original))
  print(original)
  encrypted = fernet.encrypt(original)
  with open('FileGen/Correo_Cifrado.json', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)'''


# Leer json
'''with open("FileGen/correo.json", "r") as file:
        original = json.load(file)'''

# Guardar json
'''diccionario = {1: 'xd'}
  with open("path", "w") as file:
        file.write(json.dumps(diccionario, indent=4))'''
