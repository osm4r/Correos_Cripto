#Main#
if __name__ == "__main__":
  #Imports (Modulos Correo y Smart)#
  import EnC 
  import D3C
  import ChF
  #import Python con los diccionarios
  import Diccionarios


  #Inicializar jsonC y guardar contenido del dict en la variable
  jsonC = Diccionarios.dictC
  #Comprobar si existe la carpeta FileGen#
  if ChF.CheckF('FileGen') == False:
    ChF.MDir('FileGen')
  else: #Ejución de modulos 
    print('A')
    
    #EnC.FernetK()
    #EnC.FernetC(jsonC)
    #EnC.FernetD()

    #D3C.CifB(jsonC)
    D3C.DecB()
