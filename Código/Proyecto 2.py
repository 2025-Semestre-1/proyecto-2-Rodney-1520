import tkinter as tk
from tkinter import messagebox
import random

#==============
#Funciones de apoyo
#==============

#Largo lista (Realiza lo que haria len)
#E:Una lista
#S:Retorna el largo de esa lista
def largolista(lista):
     contador = 0
     if lista == []:
          return 0
     for x in lista:
          contador += 1
     return contador

#===================
#Tablero y piezas
#===================

#Matriz para crear el tablero de juego
matriz = [
    ['+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+'],
    ['+',  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, '+'],
    ['+',  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, '+'],
    ['+',  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, '+'],
    ['+',  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, '+'],
    ['+',  0,  0,  0,  0, '+',  0,  0,  0,  0,  0, '+'],
    ['+',  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, '+'],
    ['+',  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, '+'],
    ['+',  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, '+'],
    ['+',  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, '+'],
    ['+',  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, '+'],
    ['+',  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, '+'],
    ['+',  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, '+'],
    ['+',  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, '+'],
    ['+',  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, '+'],
    ['+',  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, '+'],
    ['+',  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, '+'],
    ['+',  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, '+'],
    ['+',  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, '+'],
    ['+',  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, '+'],
    ['+',  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, '+'],
    ['+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+']
]

#Los siguientes comentarios son para ubicarse mejor en cual sentido esta rotada la pieza 
#se van usar 12 3 6 9 como las manesillas del reloj para las ubicaciones

#=====================
#=====================

piezas = {
    "O": [[
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,1,1,0,0],  # Caso especial no tiene sentido rotar esta pieza
        [0,1,1,0,0],
        [0,0,0,0,0]
    ]],

#===================
#===================

    "I": [
        [[0,0,0,0,0],
         [0,0,2,0,0],
         [0,0,2,0,0],  # 12
         [0,0,2,0,0],
         [0,0,2,0,0]],
        [[0,0,0,0,0],
         [0,0,0,0,0],
         [0,2,2,2,2],  # 3
         [0,0,0,0,0],
         [0,0,0,0,0]],
        [[0,0,0,0,0],
         [0,2,0,0,0],
         [0,2,0,0,0],  # 6
         [0,2,0,0,0],
         [0,2,0,0,0]],
        [[0,0,0,0,0],
         [0,0,0,0,0],
         [2,2,2,2,0],  # 9
         [0,0,0,0,0],
         [0,0,0,0,0]]
    ],

#===================
#===================

    "L": [
        [[0,0,3,0,0],
         [0,0,3,0,0],
         [0,0,3,3,0],  # 12
         [0,0,0,0,0],
         [0,0,0,0,0]],
        [[0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,3,3,3],  # 3
         [0,0,3,0,0],
         [0,0,0,0,0]],
        [[0,0,0,0,0],
         [0,0,0,0,0],
         [0,3,3,0,0],  # 6
         [0,0,3,0,0],
         [0,0,3,0,0]],
        [[0,0,0,0,0],
         [0,0,3,0,0],
         [3,3,3,0,0],  # 9
         [0,0,0,0,0],
         [0,0,0,0,0]]
    ],

#===================
#===================

    "J": [
        [[0,0,4,0,0],
         [0,0,4,0,0],
         [0,4,4,0,0],  # 12
         [0,0,0,0,0],
         [0,0,0,0,0]],
        [[0,0,0,0,0],
         [0,0,4,0,0],
         [0,0,4,4,4],  # 3
         [0,0,0,0,0],
         [0,0,0,0,0]],
        [[0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,4,4,0],  # 6
         [0,0,4,0,0],
         [0,0,4,0,0]],
        [[0,0,0,0,0],
         [0,0,0,0,0],
         [4,4,4,0,0],  # 9
         [0,0,4,0,0],
         [0,0,0,0,0]]
    ],

#=====================
#=====================

    "T": [
        [[0,0,0,0,0],
         [0,0,0,0,0],
         [0,5,5,5,0],  # 12
         [0,0,5,0,0],
         [0,0,0,0,0]],
        [[0,0,0,0,0],
         [0,0,5,0,0],
         [0,5,5,0,0],  # 3
         [0,0,5,0,0],
         [0,0,0,0,0]],
        [[0,0,0,0,0],
         [0,0,5,0,0],
         [0,5,5,5,0],  # 6
         [0,0,0,0,0],
         [0,0,0,0,0]],
        [[0,0,0,0,0],
         [0,0,5,0,0],
         [0,0,5,5,0],  # 9
         [0,0,5,0,0],
         [0,0,0,0,0]]
    ],

#====================
#====================

    "Z": [
        [[0,0,0,0,0],
         [0,0,0,0,0],
         [0,6,6,0,0],  # 12
         [0,0,6,6,0],
         [0,0,0,0,0]],
        [[0,0,0,0,0],
         [0,0,0,6,0],
         [0,0,6,6,0],  # 3
         [0,0,6,0,0],
         [0,0,0,0,0]]
    ],

#====================
#====================

    "U": [
        [[0,0,0,0,0],
         [0,7,0,7,0],
         [0,7,7,7,0],  # 12
         [0,0,0,0,0],
         [0,0,0,0,0]],
        [[0,0,0,0,0],
         [0,0,7,7,0],
         [0,0,7,0,0],  # 3
         [0,0,7,7,0],
         [0,0,0,0,0]],
        [[0,0,0,0,0],
         [0,0,0,0,0],
         [0,7,7,7,0],  # 6
         [0,7,0,7,0],
         [0,0,0,0,0]],
        [[0,0,0,0,0],
         [0,7,7,0,0],
         [0,0,7,0,0],  # 9
         [0,7,7,0,0],
         [0,0,0,0,0]]
    ],

#=====================
#=====================

    "Mas": [[
        [0,0,0,0,0],
        [0,0,8,0,0],
        [0,8,8,8,0],  # Caso especial no tiene sentido rotarlo debido a que eso no representa un
        [0,0,8,0,0],  # cambio significativo a la figura
        [0,0,0,0,0]
    ]],

#===================
#===================

    "Piezas": ["O","I","L","J","T","Z","U","Mas"],

    "Colores": ["Yellow","Lightblue","Orange","Pink","Violet","Green","Brown","Red"]

}

#Mostrar Tablero de con Tkinter
#E:Matriz piezas y frames
#S:El tablero de juego
def mostrarTablero(matriz, frameTablero, piezas):
    colores = {"+": "gainsboro", 0: "black"}
    listaColores = piezas["Colores"]

    for i in range(1, largolista(listaColores)+1):
        colores[i] = listaColores[i-1]

    for fila in range(largolista(matriz)):
        for col in range(largolista(matriz[0])):
            valor = matriz[fila][col]
            color = colores.get(valor, "white")
            celda = tk.Label(frameTablero, bg=color, width=2, height=1, borderwidth=1, relief="solid")
            celda.grid(row=fila, column=col, padx=1, pady=1)

#=================
#=================

#=====================
#Ejecucion del juego
#=====================

#Nuevo Juego
#E:La funcion de mostrar tablero
#S:Muestra la ventana con el tablero juego impreso
def nuevoJuego():
    ventanaJuego = tk.Toplevel(ventana)
    ventanaJuego.title("Tetris - Nuevo Juego")
    ventanaJuego.configure(bg="black")

    #Nombre del jugador y puntaje
    encabezado = tk.Frame(ventanaJuego, bg="black")
    encabezado.pack(pady=10)

    tk.Label(encabezado, text="Puntaje: (Coming soon)", font=("Arial", 12), fg="white", bg="black").pack(side="left", padx=30)
    tk.Label(encabezado, text="Jugador: (Coming soon)", font=("Arial", 12), fg="white", bg="black").pack(side="left", padx=30)

    #Botones del lado derecho (Pausa,Guardar y Salir)
    seccionCentral = tk.Frame(ventanaJuego, bg="black")
    seccionCentral.pack(pady=10)

    frameTablero = tk.Frame(seccionCentral, bg="black")
    frameTablero.pack(side="left", padx=20)
    mostrarTablero(matriz, frameTablero, piezas)

    botonesLateral = tk.Frame(seccionCentral, bg="black")
    botonesLateral.pack(side="left", padx=20)

    tk.Button(botonesLateral, text="Pausa", font=("Arial", 10, "bold"),
              bg="orange", fg="black", width=12,
              command=lambda: messagebox.showinfo("Pausa", "Función en construcción")).pack(pady=10)

    tk.Button(botonesLateral, text="Guardar", font=("Arial", 10, "bold"),
              bg="blue", fg="white", width=12,
              command=lambda: messagebox.showinfo("Guardar", "Función en construcción")).pack(pady=10)

    tk.Button(botonesLateral, text="Salir", font=("Arial", 10, "bold"),
              bg="red", fg="white", width=12,
              command=ventanaJuego.destroy).pack(pady=10)

#===========================
#Ventana del Menu Principal
#===========================

#Funcion provisional mientras se termina de crear el resto de funciones
def coomingSoon(opcion):
     messagebox.showinfo("⚠️Aviso⚠️","Funcion en construccion: Coming soon 👷")

#Funcion para poder cerrar ventana principal
def salir():
     ventana.destroy()

#Creacion de la ventana principal
ventana = tk.Tk()
ventana.title("Tetris")
ventana.geometry("650x575")

#Personalizacion de la ventana
ventana.configure(bg="darkblue")

tk.Label(ventana, text="Menu Principal", font=("Arial", 16 , "bold"),bg="darkblue",fg="orange").pack(pady=10)

opciones = ["1.Continuar juego","2.Nuevo juego","3.Estadisticas de juegos","4.Salir"]

#Asignacion de funciones a cada boton

i = 1 

for texto in opciones:
     if  i == 1:
          boton = tk.Button(ventana, text=texto, font=("Arial", 12 , "bold"),bg="green",fg="white", width=40, height=2, command=lambda i=i: coomingSoon(i))
     elif  i == 2:
          boton = tk.Button(ventana, text=texto, font=("Arial", 12 , "bold" ),bg="red",fg="white", width=40, height=2, command=nuevoJuego)
     elif  i == 3:
          boton = tk.Button(ventana, text=texto, font=("Arial", 12 ,"bold" ),bg="gold",fg="white",  width=40, height=2, command=lambda i=i: coomingSoon(i))
     elif  i == 4:
          boton = tk.Button(ventana, text=texto, font=("Arial", 12 ,"bold" ),bg="violet",fg="white", width=40, height=2, command=salir)

     boton.pack(pady=3)
     i += 1

#Para poder ejecutar el programa
ventana.mainloop()