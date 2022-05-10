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
    
"""
python -m uvicorn api:app --reload
https://www.youtube.com/watch?v=9N6a-VLBa2I
"""