import re
import os
import time
import tkinter as tk
from tkinter import *
from idlelib.tooltip import Hovertip
from gen_cerkey import *


def clearventana():
    for widget in ventana_principal.winfo_children():
        widget.destroy()

        
#CREAMOS VENTANA PARA LOGIN.
def login_function():
    clearventana()
    ventana_principal.title("Acceso a la cuenta")
    Label(ventana_principal, text="Introduzca nombre de usuario y contraseña").pack()
    Label(ventana_principal, text="").pack()
 
    user = str
    privkey = str
 
    Label(ventana_principal, text="Nombre usuario * ").pack()
    entrada_login_usuario = Entry(ventana_principal, textvariable=user)
    entrada_login_usuario.pack()
    Label(ventana_principal, text="").pack()
    Label(ventana_principal, text="Contraseña * ").pack()
    entrada_login_privKey = Entry(ventana_principal, textvariable=privkey, show= '*')
    entrada_login_privKey.pack()

    user = entrada_login_usuario.get()
    privkey = entrada_login_privKey.get()

    # entrada_login_usuario.delete(0, END) #BORRA INFORMACIÓN DEL CAMPO "Nombre usuario *" AL MOSTRAR NUEVA VENTANA.
    # entrada_login_privKey.delete(0, END) #BORRA INFORMACIÓN DEL CAMPO "Contraseña *" AL MOSTRAR NUEVA VENTANA.

    Label(ventana_principal, text="").pack()
    Button(ventana_principal, text="Acceder", width=10, height=1, bg="LightGreen", command = print('login funcional')).pack() # login() de genkey
    ventana_principal.mainloop()

    
#REGISTRO.
def registro_function():
    clearventana()
    ventana_principal.title("Registro")
    ventana_principal.geometry("300x250")

    user = StringVar() #DECLARAMOS "string" COMO TIPO DE DATO PARA "user"
    privKey = StringVar() #DECLARAMOS "sytring" COMO TIPO DE DATO PARA "privKey"
 
    Label(ventana_principal, text="Introduzca datos", bg="LightGreen").pack()
    Label(ventana_principal, text="").pack()
    etiqueta_user = Label(ventana_principal, text="Nombre de usuario * ")
    etiqueta_user.pack()
    entrada_nombre = Entry(ventana_principal, textvariable=user) #ESPACIO PARA INTRODUCIR EL NOMBRE.
    entrada_nombre.pack()
    etiqueta_privKey = Label(ventana_principal, text="Contraseña * ")
    etiqueta_privKey.pack()
    entrada_privKey = Entry(ventana_principal, textvariable=privKey, show='*') #ESPACIO PARA INTRODUCIR LA PRIVKEY.
    entrada_privKey.pack()
    Label(ventana_principal, text="").pack()
    Button(ventana_principal, text="Registrarse", width=10, height=1, bg="LightGreen", command = print('register funcional')).pack() # register() de genkey


def ventana_inicio():
    global ventana_principal
    pestas_color="DarkGrey"
    ventana_principal=Tk()
    ventana_principal.geometry("300x250")#DIMENSIONES DE LA VENTANA
    ventana_principal.title("Login con tkinter")#TITULO DE LA VENTANA
    Label(text="Escoja su opción", bg="LightGreen", width="300", height="2", font=("Calibri", 13)).pack()#ETIQUETA CON TEXTO
    Label(text="").pack()
    Button(text="Iniciar Sesión", height="2", width="30", bg=pestas_color, command=login_function).pack() #BOTÓN "Acceder"
    Label(text="").pack()
    Button(text="Registrarse", height="2", width="30", bg=pestas_color, command=registro_function).pack() #BOTÓN "Registrarse".
    Label(text="").pack()
    
    ventana_principal.mainloop()



# ------------------------------------------------------------------------------------------------------------------------------------------------------------


    


#VENTANA "VERIFICACION DE LOGIN".
def verifica_login(usuario1, privKey1):
    usuario1 = verifica_usuario.get()
    privKey1 = verifica_privKey.get()
    entrada_login_usuario.delete(0, END) #BORRA INFORMACIÓN DEL CAMPO "Nombre usuario *" AL MOSTRAR NUEVA VENTANA.
    entrada_login_privKey.delete(0, END) #BORRA INFORMACIÓN DEL CAMPO "Contraseña *" AL MOSTRAR NUEVA VENTANA.
 
    lista_archivos = os.system('cls') #TAMBIEN TENGO DUDA AQUI CON LA INFO GENERADA SI AQUI ES EL ARCHIVO QUE REVISA
    if usuario1 in lista_archivos:
        archivo1 = open(usuario1, "r") #APERTURA DE ARCHIVO EN MODO LECTURA
        verifica = archivo1.read().splitlines() #LECTURA DEL ARCHIVO QUE CONTIENE EL nombre Y contraseña.
        #SI LA CONTRASEÑA INTRODUCIDA SE ENCUENTRA EN EL ARCHIVO...
        if privKey1 in verifica:
            exito_login() #...EJECUTAR FUNCIÓN "exito_login()"
        #SI LA CONTRASEÑA NO SE ENCUENTRA EN EL ARCHIVO....
        else:
            no_privKey() #...EJECUTAR "no_privKey()"
    else:
        no_usuario() #..EJECUTA "no_usuario()".


# VENTANA "Login finalizado con exito".

 
def exito_login():
    global ventana_exito
    ventana_exito = Toplevel(ventana_login)
    ventana_exito.title("Exito")
    ventana_exito.geometry("150x100")
    Label(ventana_exito, text="Login finalizado con exito").pack()
    Button(ventana_exito, text="Entrar a contract menu", command=contract_menu).pack()
 
#VENTANA DE "Contraseña incorrecta".
 
def no_privKey():
    global ventana_no_privKey
    ventana_no_privKey = Toplevel(ventana_login)
    ventana_no_privKey.title("ERROR")
    ventana_no_privKey.geometry("150x100")
    Label(ventana_no_privKey, text="Contraseña incorrecta ").pack()
    Button(ventana_no_privKey, text="OK", command=borrar_no_privKey).pack() #EJECUTA "borrar_no_privKey()".
 
#VENTANA DE "Usuario no encontrado".
 
def no_usuario():
    global ventana_no_usuario
    ventana_no_usuario = Toplevel(ventana_login)
    ventana_no_usuario.title("ERROR")
    ventana_no_usuario.geometry("150x100")
    Label(ventana_no_usuario, text="Usuario no encontrado").pack()
    Button(ventana_no_usuario, text="OK", command=borrar_no_usuario).pack() #EJECUTA "borrar_no_usuario()"

#CERRADO DE VENTANAS

def borrar_exito_login():
    ventana_exito.destroy()
 
 
def borrar_no_privKey():
    ventana_no_privKey.destroy()
 
 
def borrar_no_usuario():
    ventana_no_usuario.destroy()

#REGISTRO USUARIO
 
def registro_usuario(address, usuario_info, privKey): ##AQUI TENGO DUDA CON LO QUE HACE EL REGISTRO, LO MANDO AL DOCUMENTO PERO NO SE 
## SI LE DA LA PRIVKEY AUTOMATICO 
 
    usuario_info = user.get()
 
    address, privKey = create_account()
    register(user, address, privKey)
    print(f'Usuario {user} registrado correctamente')
    print('Guarda tu private key porque se borrará la pantalla en 8 segundos')

    with open(f'usernames.txt', 'a') as file:
        file.write(f'{user}\n')
 
    entrada_nombre.delete(0, END)
    entrada_privKey.delete(0, END)
 
    Label(ventana_registro, text="Registro completado con éxito", fg="green", font=("calibri", 11)).pack()
 

ventana_inicio()