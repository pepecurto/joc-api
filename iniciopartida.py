from tkinter import * 
import tkinter as tk
import requests
import json

from Captio import preguntascaptio


api_url = "http://127.0.0.1:8000/iniciarpartida"
variable = 1
def iniciarpartida():
    root = Tk()
    root.title("Juego Python")
    root.geometry("750x350")

    """root.iconbitmap("C:\driver_chrome\classes\logo2.ico")"""

    response = requests.get(api_url).text
    data = json.loads(response)
    for nom in data["Partides"]:
        Button(root, text= str(nom['nom'])).pack()
        
    newgame =  Button(root, text = 'New Game',command=lambda:opciones(root))
    newgame.place(x=50,y=25)

    root.mainloop()


def opciones(root):
    root.destroy()

    ventana = Tk()
    ventana.title("Opciones")
    ventana.geometry("750x350")
    opcion1 =  Button(ventana, text = 'Captio',command=lambda:preguntascaptio(ventana))
    opcion1.place(x=350, y=150)


    ventana.mainloop()

iniciarpartida()
