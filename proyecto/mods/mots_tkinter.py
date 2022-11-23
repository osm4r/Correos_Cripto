import tkinter as tk
from tkinter import *
from tkinter import ttk
from functools import partial
from .smart_contract_actions import *
from .create_address import *

rpcServer, chain_id, mnemonic = get_ganache_config()
w3 = Web3(Web3.HTTPProvider(rpcServer))

def menu(ruser, raddress, rpassword):
    global ventana1
    global opc
    global user
    global address
    global password
    user = ruser
    address = raddress
    password = rpassword

    ventana1 = tk.Tk()
    ventana1.title("---ACCIONES DE SAMRT CONTRACT---")
    ventana1.config(width=500, height=250)
    
    menu = ttk.Label(ventana1, text = " 1.- Enviar Correo\n 2.- Ver correos recibidos\n 3.- Ver Correos enviados\n 4.- Eliminar bandeja de entrada\n 5.-Exit")
    menu.place(x=20, y=20)

    opc = ttk.Combobox(
        state="readonly",
        values=["1", "2", "3", "4", "5"]
    )
    opc.place(x=120, y=150)
    enviar = ttk.Button(ventana1, text="Enviar", command = partial( show_selection, opc,) )
    enviar.place(x= 20, y=148)


    ventana1. mainloop()


def menu2(duser, daddress, dpassword):
    global ventana
    global opc1
    global user2
    global address2
    global password2
    user2 = duser
    address2 = daddress
    password2 = dpassword

    ventana = tk.Tk()
    ventana.title("---ACCIONES DE SAMRT CONTRACT---")
    ventana.config(width=500, height=150)

    menu = ttk.Label(ventana, text = " 1.-Deploy Contact\n 2.-Exit")
    menu.place(x=20, y=20)

    opc1 = ttk.Combobox(
        state="readonly",
        values=["1", "2"]
    )
    opc1.place(x=120, y=78)
    
    enviar = ttk.Button(text="Enviar", command = partial( show_selection2, opc1,))
    enviar.place(x= 20, y=76)

    ventana. mainloop()

def show_selection(opc):
    # Obtener la opción seleccionada.
    esconder(ventana1)

    if opc.get() == "1":
        ventana2 = Toplevel(ventana1)
        ventana2.config(width=800, height=500)

        with open('usernames.txt', 'r') as file:
            file_data = file.read()
            usernames = file_data.split('\n')
            usernames.pop()
        txt1 = ttk.Label(ventana2, text = "Correo: ")
        txt1.place(x=20, y=20)
        usuarios = ttk.Combobox(ventana2,
        state="readonly",
        values= usernames
        )
        usuarios.place (x=80, y=20)
        y = 20
        # print('receivers', str(receivers))
        # receiver = usernames.index(receivers)
        
        txt3 = ttk.Label(ventana2, text = "Asunto: ")
        txt3.place(x=20, y=50)

        asunto = ttk.Entry(ventana2)
        asunto.place(x=80, y=50, width= 600)

        txt4 = ttk.Label(ventana2, text = "Cuerpo: ")
        txt4.place(x=20, y=80)

        cuerpo = ttk.Entry(ventana2)
        cuerpo.place (x=80, y=80, width = 600, height=400)

        def getvalues():
            namereceiver = usuarios.get()
            indexreceiver = usernames.index(namereceiver)
            receiver = w3.eth.accounts[indexreceiver]
            subject = asunto.get()
            body = cuerpo.get()
            print(address, password, subject, body, receiver)
            interact_enviarCorreo(address, password, subject, body, receiver)
            


        enviar = ttk.Button(ventana2, text="Enviar", command= getvalues)
        enviar.place(x=700,y= 260)


        view = ttk.Button(ventana2, text = "Regresar", command = partial(mostrar, ventana1, ventana2) )
        view.place(rely=1.0, relx=1.0, x=-15, y=-15, anchor=SE)
        # ventana2.withdraw()

        ventana2.mainloop()

    elif opc.get() == "2":
        ventana3 = tk.Tk()
        ventana3.config(width=700, height=1000)

        pleerCorreosRecibidos = call_leerCorreosRecibidos(user, address)
        '''pleerCorreosRecibidos = {0: {'Asunto': 'asdka',
                                    'Body': 'laksjd alskjd asdlkj',
                                    'Destinatario': '0x31d163DB5eF525fcDEE93d3CF9133531C353F275',
                                    'Fecha': '23/11/2022, 00:24:13',
                                    'Remitente': '0x31d163DB5eF525fcDEE93d3CF9133531C353F275'},
    1: {'Asunto': 'osadjk asodj',
        'Body': 'alksd alksjhd aslkdh',
        'Destinatario': '0x31d163DB5eF525fcDEE93d3CF9133531C353F275',
        'Fecha': '23/11/2022, 00:27:38',
        'Remitente': '0x31d163DB5eF525fcDEE93d3CF9133531C353F275'},
    2: {'Asunto': 'osmar',
        'Body': 'jas;dj l;kasjdlkas alskhdasl',
        'Destinatario': '0x31d163DB5eF525fcDEE93d3CF9133531C353F275',
        'Fecha': '23/11/2022, 00:27:49',
        'Remitente': '0x31d163DB5eF525fcDEE93d3CF9133531C353F275'}}'''
        
        n = 20
        for x in pleerCorreosRecibidos:
            txt1 = ttk.Label(ventana3, text = f'Correo {x}')
            txt1.place(x=10, y=n)
            for key, y in pleerCorreosRecibidos[x].items():
                txt1 = ttk.Label(ventana3, text = f'{key}: {y}')
                txt1.place(x=74, y=n)
                n = n+20
            n += 30
        
        view = ttk.Button(ventana3, text = "Regresar", command = partial(mostrar, ventana1, ventana3) )
        view.place(rely=1.0, relx=1.0, x=-15, y=-15, anchor=SE)

        ventana3.mainloop()
    elif opc.get() == "3":
        ventana4 = tk.Tk()
        ventana4.config(width=700, height=1000)
  
        pleerCorreosEnviados = call_leerBandejaEntrada(user, address)
        '''pleerCorreosEnviados = {0: {'Asunto': 'asdka',
                                    'Body': 'laksjd alskjd asdlkj',
                                    'Destinatario': '0x31d163DB5eF525fcDEE93d3CF9133531C353F275',
                                    'Fecha': '23/11/2022, 00:24:13',
                                    'Remitente': '0x31d163DB5eF525fcDEE93d3CF9133531C353F275'},
    1: {'Asunto': 'osadjk asodj',
        'Body': 'alksd alksjhd aslkdh',
        'Destinatario': '0x31d163DB5eF525fcDEE93d3CF9133531C353F275',
        'Fecha': '23/11/2022, 00:27:38',
        'Remitente': '0x31d163DB5eF525fcDEE93d3CF9133531C353F275'},
    2: {'Asunto': 'osmar',
        'Body': 'jas;dj l;kasjdlkas alskhdasl',
        'Destinatario': '0x31d163DB5eF525fcDEE93d3CF9133531C353F275',
        'Fecha': '23/11/2022, 00:27:49',
        'Remitente': '0x31d163DB5eF525fcDEE93d3CF9133531C353F275'}}'''
        
        n = 20
        for x in pleerCorreosEnviados:
            txt1 = ttk.Label(ventana4, text = f'Correo {x}')
            txt1.place(x=10, y=n)
            for key, y in pleerCorreosEnviados[x].items():
                txt1 = ttk.Label(ventana4, text = f'{key}: {y}')
                txt1.place(x=74, y=n)
                n = n+20
            n += 30
     
        view = ttk.Button(ventana4, text = "Regresar", command = partial(mostrar, ventana1, ventana4) )
        view.place(rely=1.0, relx=1.0, x=-15, y=-15, anchor=SE)

        ventana4.mainloop()
    elif opc.get() == "4":
        ventana5 = tk.Tk()
        ventana5.config(width=700, height=1000)
  
        EliminarBandejaEntrada = {0: {'Asunto': 'asdka',
                                    'Body': 'laksjd alskjd asdlkj',
                                    'Destinatario': '0x31d163DB5eF525fcDEE93d3CF9133531C353F275',
                                    'Fecha': '23/11/2022, 00:24:13',
                                    'Remitente': '0x31d163DB5eF525fcDEE93d3CF9133531C353F275'},
        1: {'Asunto': 'osadjk asodj',
            'Body': 'alksd alksjhd aslkdh',
            'Destinatario': '0x31d163DB5eF525fcDEE93d3CF9133531C353F275',
            'Fecha': '23/11/2022, 00:27:38',
            'Remitente': '0x31d163DB5eF525fcDEE93d3CF9133531C353F275'},
        2: {'Asunto': 'osmar',
            'Body': 'jas;dj l;kasjdlkas alskhdasl',
            'Destinatario': '0x31d163DB5eF525fcDEE93d3CF9133531C353F275',
            'Fecha': '23/11/2022, 00:27:49',
            'Remitente': '0x31d163DB5eF525fcDEE93d3CF9133531C353F275'}}
        n = 20

        for x in EliminarBandejaEntrada:
            txt1 = ttk.Label(ventana5, text = f'Correo {x}')
            txt1.place(x=10, y=n)
            for key, y in EliminarBandejaEntrada[x].items():
                txt1 = ttk.Label(ventana5, text = f'{key}: {y}')
                txt1.place(x=74, y=n)
                n = n+20
            n += 30
        view = ttk.Button(ventana5, text = "Regresar", command = partial(mostrar, ventana1, ventana5) )
        view.place(rely=1.0, relx=1.0, x=-15, y=-15, anchor=SE)

     
        ventana5.mainloop()
    else:
        quit()  
    mostrar() 

def show_selection2(opc1):
    esconder(ventana)
    # Obtener la opción seleccionada.
    if opc1.get() == "1":
        global ventana6
        ventana6 = tk.Tk()
        ventana6.config(width=500, height=250)
        # pdeploy = "Hola mundo!"
        pdeploy = deploy(address2, password2)  
        txt1 = ttk.Label(ventana6, text = pdeploy)
        txt1.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        def go_menu():
            esconder(ventana6)
            menu(user2, address2, password2)

        view = ttk.Button(ventana6, text = "Regresar", command =go_menu)

        view.place(rely=1.0, relx=1.0, x=-15, y=-15, anchor=SE)
     
        ventana6.mainloop()
    else:
        quit()

        
def esconder(view):
    view.withdraw()


def mostrar(view, view2):
    view.deiconify()
    esconder(view2)

    
def mostrar2():
    ventana1.deiconify()
    esconder(ventana6)

# menu("quser", "qaddress", "qpassword")


