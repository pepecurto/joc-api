from tkinter import * 
import tkinter as tk
import requests

api_post = "http://127.0.0.1:8000/guardarpartida"

def guardarpartida(nom,npregunta,nompartida,puntuacio):
    global api_post
    response = requests.post(api_post + "/" + nom + "/" + str(npregunta) + "/" + str(puntuacio)).text
    nompartida.delete("1.0",END)
    nompartida.insert(END,"Partida Guardada")
    print (response)