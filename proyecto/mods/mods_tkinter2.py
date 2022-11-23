import tkinter as tk
from tkinter import *
from tkinter import ttk
from functools import partial
from gen_cerkey import *
import time


#CREAMOS VENTANA PARA LOGIN.
def login_function():
    global login_window
    login_window=Toplevel(main_window)
    hide_window(main_window)
    login_window.geometry("300x250")#DIMENSIONES DE LA VENTANA
    login_window.title("Iniciar Sesión")
    Label(login_window, text="Introduzca nombre de usuario y contraseña").pack()
    Label(login_window, text="").pack()
 
    '''user = str
    privkey = str'''
 
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
        user = txtUser.get()
        password = txtPass.get()
        result = login(user, password)
        if result:
            address = get_user_address()
            Label(login_window, text=f'Bienvenido {user} -- {password} -- {address}').pack()
            time.sleep(3)
        else:
            Label(login_window, text=f'Credenciales del usuario {user} incorrectas').pack()
            time.sleep(3)
            quit()


    Button(login_window, text="Acceder", width=10, height=1, bg="LightGreen", command = verifica_login).pack() # login() de genkey

    login_window.mainloop()

    
    

    
#REGISTRO.
def registro_function():
    global register_window
    register_window=Toplevel(login_window)
    hide_window(login_window)
    register_window.geometry("300x250")#DIMENSIONES DE LA VENTANA
    register_window.title("Registro")
    register_window.geometry("300x250")

    user = StringVar() #DECLARAMOS "string" COMO TIPO DE DATO PARA "user"
    privKey = StringVar() #DECLARAMOS "sytring" COMO TIPO DE DATO PARA "privKey"
 
    Label(register_window, text="Introduzca datos", bg="LightGreen").pack()
    Label(register_window, text="").pack()
    Label(register_window, text="Nombre de usuario * ").pack()
    Entry(register_window, textvariable=user).pack()
    Label(register_window, text="Contraseña * ").pack()
    Entry(register_window, textvariable=privKey, show='*').pack()
    Label(register_window, text="").pack()
    Button(register_window, text="Registrarse", width=10, height=1, bg="LightGreen", command = quit).pack() # register() de genkey
    register_window.mainloop()


def ventana_inicio():
    global main_window
    pestas_color="DarkGrey"
    main_window=Tk()
    main_window.geometry("300x250")#DIMENSIONES DE LA VENTANA
    main_window.title("Login con tkinter")#TITULO DE LA VENTANA
    Label(text="Escoja su opción", bg="LightGreen", width="300", height="2", font=("Calibri", 13)).pack()#ETIQUETA CON TEXTO
    Label(text="").pack()
    Button(text="Iniciar Sesión", height="2", width="30", bg=pestas_color, command=login_function).pack() #BOTÓN "Acceder"
    Label(text="").pack()
    Button(text="Registrarse", height="2", width="30", bg=pestas_color, command=registro_function).pack() #BOTÓN "Registrarse".
    Label(text="").pack()
    
    main_window.mainloop()

    
def hide_window(window):
    window.withdraw()

def show_window(window):
    window.deiconify()

def destroy_show(window1, window2):
    window1.destroy()
    show_window(window2)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------


    
'''

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
 
    Label(ventana_registro, text="Registro completado con éxito", fg="green", font=("calibri", 11)).pack()'''
 

ventana_inicio()