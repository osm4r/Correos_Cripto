import base64
import ast


def CifB(Dict, file):
  D_text = str(Dict)
  B_text = D_text.encode('utf-8')
  C_B64 = base64.b64encode(B_text)
  #CS_B64 = str(C_B64)

  with open(file, 'wb') as encrypted_file:
    encrypted_file.write(C_B64)


def DecB(file):
  with open(file, 'rb') as encrypted_file:
    dict_en = encrypted_file.read()
    dict_decb = base64.b64decode(dict_en)
    dict_dec = dict_decb.decode('utf-8')
    dict_dec2 = ast.literal_eval(dict_dec)
    return dict_dec2
  
'''diccionario = {1: 'sadas', 2: 'asdasd'}
CifB(diccionario)'''

'''diccionario = DecB(file)
print(diccionario)'''
