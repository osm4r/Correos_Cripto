import re
import os
import time
import tkinter as tk
from tkinter import *
from tkinter import messagebox,ttk
from idlelib.tooltip import Hovertip

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
        txt5.place(x=20, y=60)

        captur2 = ttk.Entry()
        captur2.place (x=40, y=60)

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

