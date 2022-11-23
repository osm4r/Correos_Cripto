import os

def CheckF(Carpeta):
  file_exist = os.path.exists(Carpeta)
  return file_exist

def MDir(Carpeta):
  os.mkdir('FileGen')

def Resta(a,b):
    print("le quitamos 2 a la b")
    b = b - 2
    print("Nuevo valor de la b: ",b)
    return a-b