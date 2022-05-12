from tkinter.tix import INTEGER
from fastapi import FastAPI
import json

app = FastAPI()
captiojson = "captio.json"
Partides = "Partides.json"
Respostes = "Respostes.json"


@app.get("/iniciarpartida")
def partida():
    f = open(Partides)
    data = json.load(f)

    return data
   
@app.get("/accion/{accion_id}")
def accio(accion_id):
    f = open(captiojson)
    data = json.load(f)

    for pregunta in data['Preguntes']:
        if pregunta['id'] == accion_id:
            print(pregunta['pregunta'])
            
            return pregunta

@app.get("/respuestas/{npregunta}")
def respuesta(npregunta):
    f = open(Respostes)
    data = json.load(f)
    resposteslist = []
    for pregunta in data['Captio']:
        if pregunta['pregunta'] == npregunta:
            resposteslist.append(pregunta)
    return resposteslist
    


@app.post("/guardarpartida/{nom}/{npregunta}/{puntuacio}")
def guardar(nom,npregunta,puntuacio):
    formata(nom,npregunta,puntuacio)
    global formatopost 
    with open(Partides, 'r+') as file:
        
        file_data = json.load(file)
        file_data["Partides"].append(formatopost)
        file.seek(0)
        json.dump(file_data,file,indent=4)

    return nom,npregunta

def formata(nom,npregunta,puntuacio):
    global formatopost
    formatopost = {"nom":nom,"npregunta":npregunta,"puntuacio":puntuacio}
    return formatopost
