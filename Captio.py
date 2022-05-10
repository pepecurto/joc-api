from tkinter import *
import requests
import json
from tkinter import ttk

i = 0
npregunta = 1
x = 4
puntuacio = 0

def preguntascaptio(ventana):
    # Create an instance of tkinter frame
    ventana.destroy()
    win = Tk()
    win.geometry("700x350")
    win.title("Trivial")

    # Create a text box to display the response body
    text = Text(win, height=3, width=25, wrap="word")
    text.config(font="Arial, 12")

    label = Label(win, text="Pregunta:")
    label.config(font="Calibri, 14")
    pregunta1(text,label,win,)


def pregunta1(text,label,win):
   api_url = "http://127.0.0.1:8000/accion/1"
   api_url2 = "http://127.0.0.1:8000/respuestas/1"

   response = requests.get(api_url).text
   response_info = json.loads(response)

   response2= requests.get(api_url2).text
   response_info2 = json.loads(response2)

   Fact = response_info["pregunta"]
   resposta1 = Button(win, text= response_info2[0]["text"],command=lambda:comprobar(response_info2[0]["correta"],text,resposta1,resposta2,resposta3,resposta4))
   resposta2 = Button(win, text= response_info2[1]["text"],command=lambda:comprobar(response_info2[1]["correta"],text,resposta1,resposta2,resposta3,resposta4))
   resposta3 = Button(win, text= response_info2[2]["text"],command=lambda:comprobar(response_info2[2]["correta"],text,resposta1,resposta2,resposta3,resposta4))
   resposta4 = Button(win, text= response_info2[3]["text"],command=lambda:comprobar(response_info2[3]["correta"],text,resposta1,resposta2,resposta3,resposta4))

   resposta1.place(y=180,x=150)
   resposta2.place(y=180,x=370)
   resposta3.place(y=250,x=150)
   resposta4.place(y=250,x=370)


   text.delete('1.0', END)
   text.insert(END, Fact)

    # Create Next and Exit Button

   label.pack()
   text.pack()
   win.mainloop()

def next(text,resposta1,resposta2,resposta3,resposta4,puntuacio):
    text.delete('1.0',END)
    global npregunta
    global x 
    x +=1
    npregunta += 1
    if npregunta != 11:    
        api_url = "http://127.0.0.1:8000/accion/" + str(npregunta)
        api_url2 = "http://127.0.0.1:8000/respuestas/" + str(npregunta)
        response = requests.get(api_url).text
        response2 = requests.get(api_url2).text
        response_info2 = json.loads(response2)
        resposta1 ['text'] = response_info2[0]["text"]
        resposta1 ['command'] = lambda: comprobar(response_info2[0]["correta"],text,resposta1,resposta2,resposta3,resposta4)
        resposta2 ['text'] = response_info2[1]["text"]
        resposta2 ['command'] = lambda: comprobar(response_info2[1]["correta"],text,resposta1,resposta2,resposta3,resposta4)
        resposta3 ['text'] = response_info2[2]["text"]
        resposta3 ['command'] = lambda: comprobar(response_info2[2]["correta"],text,resposta1,resposta2,resposta3,resposta4)
        resposta4 ['text'] = response_info2[3]["text"]
        resposta4 ['command'] = lambda: comprobar(response_info2[3]["correta"],text,resposta1,resposta2,resposta3,resposta4)

        response_info = json.loads(response)
        responsta=response_info["pregunta"]
        text.insert(END,responsta)
        
        return npregunta

    else:
        resultadofinal(puntuacio,text,resposta1,resposta2,resposta3,resposta4)

def resultadofinal(puntuacio,text,resposta1,resposta2,resposta3,resposta4):
    if puntuacio == 10:
        resposta1.destroy()
        resposta2.destroy()
        resposta3.destroy()
        resposta4.destroy()
        text.insert(END,"tu puntuacio ha sido " + str(puntuacio) + "/10 pasaste el test :D ")

    else:
        resposta1.destroy()
        resposta2.destroy()
        resposta3.destroy()
        resposta4.destroy()
        text.insert(END,"tu puntuacio ha sido " + str(puntuacio) + "/10 NO pasaste el test D: ")



def comprobar(resposta,text,resposta1,resposta2,resposta3,resposta4):
    global puntuacio
    if resposta == "Si":
        puntuacio +=1
        next(text,resposta1,resposta2,resposta3,resposta4,puntuacio)
    else:
        next(text,resposta1,resposta2,resposta3,resposta4,puntuacio)
