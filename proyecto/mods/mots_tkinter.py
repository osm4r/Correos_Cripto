import re
import os
import time
import tkinter as tk
from tkinter import *
from tkinter import messagebox,ttk
from idlelib.tooltip import Hovertip


def ventana_inicio():
    global ventana_principal
    pestas_color="DarkGrey"
    ventana_principal=Tk()
    ventana_principal.geometry("300x250")#DIMENSIONES DE LA VENTANA
    ventana_principal.title("Login con tkinter")#TITULO DE LA VENTANA
    Label(text="Escoja su opción", bg="LightGreen", width="300", height="2", font=("Calibri", 13)).pack()#ETIQUETA CON TEXTO
    Label(text="").pack()
    Button(text="Acceder", height="2", width="30", bg=pestas_color, command=login).pack() #BOTÓN "Acceder"
    Label(text="").pack()
    Button(text="Registrarse", height="2", width="30", bg=pestas_color, command=registro).pack() #BOTÓN "Registrarse".
    Label(text="").pack()
    ventana_principal.mainloop()

def registro():
    global ventana_registro
    ventana_registro = Toplevel(ventana_principal)
    ventana_registro.title("Registro")
    ventana_registro.geometry("300x250")
 
    global user
    global privKey
    global entrada_user
    global entrada_privKey
    user = StringVar() 
    privKey = StringVar() 
 
    Label(ventana_registro, text="Introduzca datos", bg="LightGreen").pack()
    Label(ventana_registro, text="").pack()
    etiqueta_user = Label(ventana_registro, text="Nombre de usuario * ")
    etiqueta_user.pack()
    entrada_nombre = Entry(ventana_registro, textvariable=user) #ESPACIO PARA INTRODUCIR EL NOMBRE.
    entrada_nombre.pack()
    etiqueta_privKey = Label(ventana_registro, text="Contraseña * ")
    etiqueta_privKey.pack()
    entrada_privKey = Entry(ventana_registro, textvariable=privKey, show='*') #ESPACIO PARA INTRODUCIR LA PRIVKEY.
    entrada_privKey.pack()
    Label(ventana_registro, text="").pack()
    Button(ventana_registro, text="Registrarse", width=10, height=1, bg="LightGreen", command = registro_usuario).pack() #BOTÓN "Registrarse"

#CREAMOS VENTANA PARA LOGIN.

def login():
    global ventana_login
    ventana_login = Toplevel(ventana_principal)
    ventana_login.title("Acceso a la cuenta")
    ventana_login.geometry("300x250")
    Label(ventana_login, text="Introduzca nombre de usuario y contraseña").pack()
    Label(ventana_login, text="").pack()
 
    global verifica_usuario
    global verifica_privKey
 
    verifica_usuario = StringVar()
    verifica_privKey = StringVar()
 
    global entrada_login_usuario
    global entrada_login_privKey
 
    Label(ventana_login, text="Nombre usuario * ").pack()
    entrada_login_usuario = Entry(ventana_login, textvariable=verifica_usuario)
    entrada_login_usuario.pack()
    Label(ventana_login, text="").pack()
    Label(ventana_login, text="Contraseña * ").pack()
    entrada_login_privKey = Entry(ventana_login, textvariable=verifica_privKey, show= '*')
    entrada_login_privKey.pack()
    Label(ventana_login, text="").pack()
    Button(ventana_login, text="Acceder", width=10, height=1, command = verifica_login).pack()

#VENTANA "VERIFICACION DE LOGIN".

def verifica_login():
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
 
def registro_usuario(): ##AQUI TENGO DUDA CON LO QUE HACE EL REGISTRO, LO MANDO AL DOCUMENTO PERO NO SE 
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
 





def show_selection(opc):
    # Obtener la opción seleccionada.
    ventana2 = tk.Tk()
    ventana2.config(width=500, height=250)
    selection = opc.get()
    if opc == 1:
        with open('usernames.txt', 'r') as file:
            file_data = file.read()
            usernames = file_data.split('\n')
            usernames.pop()
        txt1 = ttk.Label(ventana2, text = "Correo: ")
        txt1.place(x=20, y=20)
        y = 20
        for x in range (len(usernames)):
            txt2 = ttk.Label(ventana2, text = f"{x}: {usernames[x]}")
            txt2.place(x=42, y=y)
            y = y + 10

        txt3 = ttk.Label(ventana2, text = "Asunto: ")
        txt3.place(x=20, y=40)

        captura = ttk.Entry()
        captura.place (x=40, y=40)

        txt4 = ttk.Label(ventana2, text = "cuerpo: ")
        txt4.place(x=20, y=60)

        captur2 = ttk.Entry()
        captur2.place (x=40, y=60)

        enviar = ttk.Button(text="Enviar")
        enviar.place(x= 20, y=15)

        ventana2.mainloop()
    elif opc == 2:
        ventana3 = tk.Tk()
        ventana3.config(width=500, height=250)
  
        txt1 = ttk.Label(ventana3, text = " Ingrese el codigo aqui(BORRAR ESTE CODIGO)")
        txt1.place(x=20, y=20)
     
        ventana3.mainloop()
    elif opc == 3:
        ventana4 = tk.Tk()
        ventana4.config(width=500, height=250)
  
        txt1 = ttk.Label(ventana4, text = " Ingrese el codigo aqui(BORRAR ESTE CODIGO)")
        txt1.place(x=20, y=20)
     
        ventana4.mainloop()
    elif opc == 4:
        ventana5 = tk.Tk()
        ventana5.config(width=500, height=250)
  
        txt1 = ttk.Label(ventana5, text = " Ingrese el codigo aqui(BORRAR ESTE CODIGO)")
        txt1.place(x=20, y=20)
     
        ventana5.mainloop()
    else:
        quit()          

def show_selection2(opc):
    # Obtener la opción seleccionada.
    if opc == 1:
        selection = opc.get()
        messagebox.showinfo(
        message=f"La opción seleccionada es: {selection}",
        title="Selección")
    else:
        quit()

def menu():

    ventana = tk.Tk()
    ventana.title("---ACCIONES DE SAMRT CONTRACT---")
    ventana.config(width=500, height=250)

    menu = ttk.Label(ventana, text = " 1.- Enviar Correo\n 2.- Ver correos recibidos\n 3.- Ver Correos enviados\n 4.- Eliminar bandeja de entrada\n 5.-Exit")
    menu.place(x=20, y=20)

    opc = ttk.Combobox(
        state="readonly",
        values=["1", "2", "3", "4", "5"]
    )
    opc.place(x=120, y=150)

    enviar = ttk.Button(text="Enviar",
    command=show_selection(opc))
    enviar.place(x= 20, y=15)

    ventana.whithdraw()

    ventana. mainloop()

def menu2():

    ventana = tk.Tk()
    ventana.title("---ACCIONES DE SAMRT CONTRACT---")
    ventana.config(width=500, height=150)

    menu = ttk.Label(ventana, text = " 1.-Deploy Contact\n 2.-Exit")
    menu.place(x=20, y=20)

    opc = ttk.Combobox(
        state="readonly",
        values=["1", "2"]
    )
    opc.place(x=120, y=150)
    
    enviar = ttk.Button(text="Enviar", 
    command=show_selection2(opc))
    enviar.place(x= 20, y=15)

    ventana. mainloop()

