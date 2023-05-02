import tkinter as tk
from tkinter import *
import os
import getpass
from time import strftime

colorbg = '#242038'
colorfont = '#F7ECE1'

root = tk.Tk()
root.title('Relógio')
root.geometry('600x320')
root.maxsize(600, 320)
root.minsize(600, 320)
root.configure(background=colorbg)

def get_saudacao():
 nome_usuario = getpass.getuser()
 saudacao.config( text='Olá, ' + nome_usuario)
def get_data():
 data_atual = strftime(' %a, %d %b %Y ')
 data.config(text= data_atual)
def get_horas():
 hora_atual = strftime('%H:%M:%S')
 horas.config(text=hora_atual)
 horas.after(1000, get_horas)
 
tela = tk.Canvas(root, width=600, height=30, bg=colorbg, highlightthickness=0, relief='ridge')
tela.pack()
saudacao = Label(root, bg=colorbg, fg=colorfont, font=('Montserrat', 16))
saudacao.pack()
data = Label(root, bg=colorbg, fg=colorfont, font=('Montserrat', 16))
data.pack(pady=2)
tela2 = tk.Canvas(root, width=600, height=40, bg=colorbg, highlightthickness=0, relief='ridge')
tela2.pack()
horas = Label(root, bg=colorbg, fg=colorfont, font=('Montserrat', 64, 'bold'))
horas.pack(pady=2)

get_saudacao()
get_data()
get_horas()

root.mainloop()