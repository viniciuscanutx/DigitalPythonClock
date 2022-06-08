#Bibliotecas Importadas
from operator import iconcat
from tkinter import *
import tkinter 
from datetime import datetime

cor1 = '#3d3d3d' #Cor Preta Fundo
cor2 = '#FFFFFF' #Cor Branca Texto

#Configuração Janela
janela=Tk()
janela.title('Relogio')
janela.geometry("330x150")
janela.iconbitmap('icon.ico')
janela.configure(bg=cor1)
janela.resizable(width=FALSE, height=FALSE)

#Configuração Relógio
def relogio():
    tempo=datetime.now()
    hora= tempo.strftime('%H:%M:%S')
    dia_semana = tempo.strftime("%A")
    dia = tempo.day
    mes = tempo.strftime("%b")
    ano = tempo.strftime("%Y")

    l1.config(text=hora)
    l1.after(200, relogio)
    l2.config(text=dia_semana + " - " + str(dia) + "/" + str(mes) + "/" + str(ano))

#Configuração Janela
l1 = Label(janela, text='', font=('Arial 60'), bg=cor1, fg=cor2)
l1.grid(row=0, column=0, sticky=NW, padx=5)

l2 = Label(janela, text='', font=('Arial 20'), bg=cor1, fg=cor2)
l2.grid(row=1, column=0, sticky=NW, padx=5)

#Janela Mainloop
relogio()
janela.mainloop()
