import tkinter as tk
from tkinter import messagebox
import random

#Funcion provisional mientras se termina de crear el resto de funciones
def coomingSoon(opcion):
     messagebox.showinfo("⚠️Aviso⚠️","Funcion en construccion: Coming soon 👷")

#Funcion para poder cerrar ventana principal
def salir():
     ventana.destroy()

#Creacion de la ventana principal
ventana = tk.Tk()
ventana.title("Tetris")
ventana.geometry("650x650")

tk.Label(ventana, text="Menu Principal", font=("Arial", 16 , "bold")).pack(pady=10)

opciones = ["1.Continuar juego","2.Nuevo juego","3.Estadisticas de juegos","4.Salir"]

i = 1 

for texto in opciones:
     if  i == 1:
          boton = tk.Button(ventana, text=texto, width=50, height=3, command=lambda i=i: coomingSoon(i))
     elif  i == 2:
          boton = tk.Button(ventana, text=texto, width=50, height=3, command=lambda i=i: coomingSoon(i))
     elif  i == 3:
          boton = tk.Button(ventana, text=texto, width=50, height=3, command=lambda i=i: coomingSoon(i))
     elif  i == 4:
          boton = tk.Button(ventana, text=texto, width=50, height=3, command=salir)

     boton.pack(pady=3)
     i += 1

ventana.mainloop()