import tkinter as tk
from tkinter import *
from tkinter import ttk
from functools import partial
from .gen_cerkey import *
from .create_address import *
import time


#CREAMOS VENTANA PARA LOGIN.
def login_function(btn):
    global btnpress
    btnpress = btn
    global login_window
    login_window=Toplevel(main_window)
    hide_window(main_window)
    # main_window.destroy()
    login_window.geometry("300x250")#DIMENSIONES DE LA VENTANA
    login_window.title("Iniciar Sesión")
    Label(login_window, text="Introduzca nombre de usuario y contraseña").pack()
    Label(login_window, text="").pack()
 
    Label(login_window, text="Nombre usuario * ").pack()
    txtUser = Entry(login_window)
    txtUser.pack()
    Label(login_window, text="").pack()
    Label(login_window, text="Contraseña * ").pack()
    txtPass = Entry(login_window, show= '*')
    txtPass.pack()


    # entrada_login_usuario.delete(0, END) #BORRA INFORMACIÓN DEL CAMPO "Nombre usuario *" AL MOSTRAR NUEVA VENTANA.
    # entrada_login_privKey.delete(0, END) #BORRA INFORMACIÓN DEL CAMPO "Contraseña *" AL MOSTRAR NUEVA VENTANA.

    Label(login_window, text="").pack()

    #VENTANA "VERIFICACION DE LOGIN".
    def verifica_login():
        global user
        global address
        global password
        user = txtUser.get()
        password = txtPass.get()
        result = login(user, password)
        if result:
            address = get_user_address(user)
            Label(login_window, text=f'Bienvenido {user}\nAddress: {address}\nPrivate Key: {password}').pack()
            time.sleep(3)
            login_window.destroy()
            main_window.destroy()
        else:
            Label(login_window, text=f'Credenciales del usuario {user} incorrectas').pack()
            time.sleep(3)
            quit()


    Button(login_window, text="Acceder", width=10, height=1, bg="LightGreen", command = verifica_login).pack() # login() de genkey
    login_window.mainloop()


    
#REGISTRO.
def registro_function(btn):
    global btnpress
    btnpress = btn
    global register_window
    register_window=Toplevel(main_window)
    hide_window(main_window)
    # main_window.destroy()
    register_window.geometry("300x250")#DIMENSIONES DE LA VENTANA
    register_window.title("Registrarse")
    register_window.geometry("300x250")
 
    Label(register_window, text="Introduzca datos", bg="LightGreen").pack()
    Label(register_window, text="").pack()
    Label(register_window, text="Nombre de usuario * ").pack()
    txtUser = Entry(register_window)
    txtUser.pack()

    Label(register_window, text="").pack()

    def verifica_registro():
        global user2
        global address2
        global privKey2
        user2 = txtUser.get()
        address2, privKey2 = create_account()
        register(user2, address2, privKey2)
        with open(f'usernames.txt', 'a') as file:
            file.write(f'{user2}\n')
        Label(register_window, text=f'Bienvenido {user2}\nAddress: {address2}\nPrivate Key: {privKey2}').pack()
        time.sleep(3)
        register_window.destroy()
        main_window.destroy()


    Button(register_window, text="Registrarse", width=10, height=1, bg="LightGreen", command = verifica_registro).pack() # register() de genkey
    register_window.mainloop()
    #return user2, address2, privKey2
    


def ventana_inicio():
    global main_window
    pestas_color="DarkGrey"
    main_window=Tk()
    main_window.geometry("300x250")#DIMENSIONES DE LA VENTANA
    main_window.title("Login con tkinter")#TITULO DE LA VENTANA
    Label(text="Escoja su opción", bg="LightGreen", width="300", height="2", font=("Calibri", 13)).pack()#ETIQUETA CON TEXTO
    Label(text="").pack()
    Button(text="Iniciar Sesión", height="2", width="30", bg=pestas_color, command=lambda:login_function(1)).pack() #BOTÓN "Acceder"
    Label(text="").pack()
    Button(text="Registrarse", height="2", width="30", bg=pestas_color, command=lambda:registro_function(2)).pack() #BOTÓN "Registrarse".
    Label(text="").pack()
    
    main_window.mainloop()
    if btnpress == 2:
        return user2, address2, privKey2
    else:
        return user, address, password

    
def hide_window(window):
    window.withdraw()

def show_window(window):
    window.deiconify()

def destroy_show(window1, window2):
    window1.destroy()
    show_window(window2)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------