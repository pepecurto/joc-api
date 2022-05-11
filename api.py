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
    


@app.post("/guardarpartida/{nom}/{npregunta}")
def guardar(nom,npregunta):
    formata(nom,npregunta)
    global formatopost 
    with open(Partides, 'r+') as file:
        
        file_data = json.load(file)
        file_data["Partides"].append(formatopost)
        file.seek(0)
        json.dump(file_data,file,indent=4)

    return nom,npregunta

def formata(nom,npregunta):
    global formatopost
    formatopost = {"nom":nom,"npregunta":npregunta}
    return formatopost




"""
python -m uvicorn api:app --reload
https://www.youtube.com/watch?v=9N6a-VLBa2I
"""