import re
import os
import time
import tkinter as tk
from tkinter import *
from tkinter import messagebox,ttk
from idlelib.tooltip import Hovertip
from functools import partial

def menu():
    global ventana1
    global opc
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
    enviar = ttk.Button(ventana1, text="Enviar", command = partial( show_selection, opc))
    enviar.place(x= 20, y=148)

    ventana1. mainloop()


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

def show_selection(opc):
    # Obtener la opción seleccionada.
    
    if opc.get() == "1":
        ventana2 = Toplevel(ventana1)
        ventana2.config(width=800, height=500)

        with open('usernames.txt', 'r') as file:
            file_data = file.read()
            usernames = file_data.split('\n')
            usernames.pop()
        txt1 = ttk.Label(ventana2, text = "Correo: ")
        txt1.place(x=20, y=20)
        opc = ttk.Combobox(ventana2,
        state="readonly",
        values= usernames
        )
        opc.place (x=80, y=20)
        y = 20

        txt3 = ttk.Label(ventana2, text = "Asunto: ")
        txt3.place(x=20, y=50)

        captura = ttk.Entry(ventana2)
        captura.place(x=80, y=50, width= 600)

        txt4 = ttk.Label(ventana2, text = "Cuerpo: ")
        txt4.place(x=20, y=80)

        captur2 = ttk.Entry(ventana2)
        captur2.place (x=80, y=80, width = 600, height=400)

        enviar = ttk.Button(ventana2, text="Enviar")
        enviar.place(x=700,y= 260)

        ventana2.mainloop()
    elif opc.get() == "2":
        ventana3 = tk.Tk()
        ventana3.config(width=500, height=250)
  
        txt1 = ttk.Label(ventana3, text = " Ingrese el codigo aqui(BORRAR ESTE CODIGO)")
        txt1.place(x=20, y=20)
     
        ventana3.mainloop()
    elif opc.get() == "3":
        ventana4 = tk.Tk()
        ventana4.config(width=500, height=250)
  
        txt1 = ttk.Label(ventana4, text = " Ingrese el codigo aqui(BORRAR ESTE CODIGO)")
        txt1.place(x=20, y=20)
     
        ventana4.mainloop()
    elif opc.get() == "4":
        ventana5 = tk.Tk()
        ventana5.config(width=500, height=250)
  
        txt1 = ttk.Label(ventana5, text = " Ingrese el codigo aqui(BORRAR ESTE CODIGO)")
        txt1.place(x=20, y=20)
     
        ventana5.mainloop()
    else:
        quit()   

def show_selection2(opc):
    # Obtener la opción seleccionada.
    if opc.get() == "2":
        selection = opc.get()
        messagebox.showinfo(
        message=f"La opción seleccionada es: {selection}",
        title="Selección")
    else:
        quit()

menu()

