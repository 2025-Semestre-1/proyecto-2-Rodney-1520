import tkinter as tk
from tkinter import messagebox
import random

#===========================
#Funciones de apoyo (Inicio)
#===========================

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

#========================
#Funciones de apoyo (Fin)
#========================

#=========================
#Tablero y piezas (Inicio)
#=========================

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

piezas = {
    "O": [[
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,1,1,0,0],  # Caso especial no tiene sentido rotar esta pieza
        [0,1,1,0,0],
        [0,0,0,0,0]
    ]],

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

#=====================

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

#======================

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

#=======================


    "Mas": [[
        [0,0,0,0,0],
        [0,0,8,0,0],
        [0,8,8,8,0],  # Caso especial no tiene sentido rotarlo debido a que eso no representa un
        [0,0,8,0,0],  # cambio significativo a la figura
        [0,0,0,0,0]
    ]],

#===================

    "Piezas": ["O","I","L","J","T","Z","U","Mas"],

    "Colores": ["Yellow","Blue","Orange","Pink","Violet","Green","Brown","Red"]

}

#===================
#Variables globales para las piezas del tablero
piezaActiva = None
posicionX = 3
posicionY = 0
rotacion = 0
nombrePieza = ""

#==================

#Mostrar Tablero de con Tkinter
#E:Matriz piezas y frames
#S:El tablero de juego
def mostrarTablero(matriz, frameTablero, piezas):
    colores = {"+": "gray", 0: "black"}
    listaColores = piezas["Colores"]

    for i in range(1, largolista(listaColores) + 1):
        colores[i] = listaColores[i - 1]

    for fila in range(largolista(matriz)):
        for col in range(largolista(matriz[0])):
            valor = matriz[fila][col]
            color = colores.get(valor, "white")
            celda = tk.Label(frameTablero, bg=color, width=2, height=1, borderwidth=1, relief="solid")
            celda.grid(row=fila, column=col, padx=1, pady=1)

#======================
#Tablero y Piezas (Fin)
#======================

#============================
#Ejecucion del juego (Inicio)
#============================

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

    #Botones del lado derecho(pausa,guardar,salir) 
    seccionCentral = tk.Frame(ventanaJuego, bg="black")
    seccionCentral.pack(pady=10)

    frameTablero = tk.Frame(seccionCentral, bg="black")
    frameTablero.pack(side="left", padx=20)
    nuevaPieza()               
    insertarPiezaEnMatriz()
    mostrarTablero(matriz, frameTablero, piezas)

    botonesLateral = tk.Frame(seccionCentral, bg="black")
    botonesLateral.pack(side="left", padx=20)
    tk.Button(botonesLateral, text="Pausa", font=("Arial", 10, "bold"), bg="orange", fg="black", width=12, command=lambda: messagebox.showinfo("Pausa", "Función en construcción")).pack(pady=10)
    tk.Button(botonesLateral, text="Guardar", font=("Arial", 10, "bold"), bg="blue", fg="white", width=12, command=lambda: messagebox.showinfo("Guardar", "Función en construcción")).pack(pady=10)
    tk.Button(botonesLateral, text="Salir", font=("Arial", 10, "bold"), bg="red", fg="white", width=12, command=ventanaJuego.destroy).pack(pady=10)

    ventanaJuego.bind("<KeyPress-Left>", lambda e: moverPiezaDireccion("izquierda", frameTablero))
    ventanaJuego.bind("<KeyPress-Right>", lambda e: moverPiezaDireccion("derecha", frameTablero))
    ventanaJuego.bind("<KeyPress-Down>", lambda e: moverPiezaDireccion("abajo", frameTablero))
    ventanaJuego.focus_set()

#=================================

#Nueva pieza
#E:Variables globales de las piezas para el juego
#S:Una de las piezas aletorias 
def nuevaPieza():
    global piezaActiva, rotacion, nombrePieza ,posicionX, posicionY
    nombrePieza =  random.choice(piezas["Piezas"])
    piezaActiva = piezas[nombrePieza][0]
    rotacion = 0
    posicionX = 4
    posicionY = 0

#=================================

#Insertar piezas en la matriz(Tablero)
#E:piezas matriz
#S:la pieza dentro de la matriz
def insertarPiezaEnMatriz():
    for fila in range(5):
        for col in range(5):
            valor = piezaActiva[fila][col]
            if valor != 0:
                y = posicionY + fila
                x = posicionX + col
                if 0 <= y < largolista(matriz) and 0 <= x < largolista(matriz[0]) and matriz[y][x] == 0:
                    matriz[y][x] = valor

#===================================

#Borrar pieza de la matriz
#E:la pieza dentro de la matriz de base (molde que se uso una matriz 5x5)
#S:la pieza sola 
def borrarPiezaDeMatriz():
    for fila in range(5):
        for col in range(5):
            valor = piezaActiva[fila][col]
            if valor != 0:
                y = posicionY + fila
                x = posicionX + col
                if 0 <= y < largolista(matriz) and 0 <= x < largolista(matriz[0]) and isinstance(matriz[y][x], int):
                    matriz[y][x] = 0

#=====================================

#Puede mover abajo
#E:Verifica si la pieza seleccionada puede bajar mas
#S:retorna true o false si o no
def puedeMoverAbajo():
    for fila in range(5):
        for col in range(5):
            if piezaActiva[fila][col] != 0:
                nuevaFila = posicionY + fila + 1
                nuevaCol = posicionX + col
                if matriz[nuevaFila][nuevaCol] != 0:
                    return False
    return True

#=====================================

#Mover pieza
#E: Frame del tablero
#S: Mueve la pieza hacia abajo o genera nueva si ya no puede bajar
def moverPieza(frameTablero):
    global posicionY

    borrarPiezaDeMatriz()

    if puedeMoverAbajo():
        posicionY += 1
        insertarPiezaEnMatriz()
        mostrarTablero(matriz, frameTablero, piezas)
    else:
        insertarPiezaEnMatriz()
        mostrarTablero(matriz, frameTablero, piezas)

        
        nuevaPieza()
        insertarPiezaEnMatriz()
        mostrarTablero(matriz, frameTablero, piezas)

#=====================================

#Puede Mover teclas
#E:Una de las distintas piezas del juego
#S:Verfica si la pieza se puede mover retorna True si se puede y False si no
#R:Depende de la piezas del juego para funcionar
def puedeMover(nuevaX,nuevaY):
    for fila in range(5):
        for col in range(5):
            if piezaActiva[fila][col] != 0:
                y = nuevaY + fila
                x = nuevaX + col
                if y >= largolista(matriz) or x < 0 or x >= largolista(matriz[0]) or matriz[y][x] != 0:
                    return False
    return True

#=====================================

#Mover Pieza direccion 
#E:Una pieza culaquiera del juego
#S:se realiza la trsalcion de la pieza ya sea para abajo izquierda o derecha
#R:Depende de tener piezas y solo si se pueden mover
def moverPiezaDireccion(direccion,frameTablero):
    global posicionX, posicionY
    
    borrarPiezaDeMatriz()
    
    if direccion == "izquierda":
        if puedeMover(posicionX - 1,posicionY):
            posicionX -=1
    elif direccion == "derecha":
            if puedeMover(posicionX + 1,posicionY):
                posicionX += 1
    elif direccion == "abajo":
            if puedeMover(posicionX, posicionY + 1):
                posicionY +=1
        
    insertarPiezaEnMatriz()
    mostrarTablero(matriz,frameTablero,piezas)

#==========================
#Ejecucion del Juego (Fin)
#===========================

#===================================
#Ventana del Menu Principal (Inicio)
#===================================

#Funcion provisional mientras se termina de crear el resto de funciones
def coomingSoon(opcion):
     messagebox.showinfo("⚠️Aviso⚠️","Funcion en construccion: Coming soon 👷")

#======================================

#Funcion para poder cerrar ventana principal
def salir():
     ventana.destroy()

#======================================

#Creacion de la ventana principal
ventana = tk.Tk()
ventana.title("Tetris")
ventana.geometry("650x575")

#=======================================

#Personalizacion de la ventana
ventana.configure(bg="darkblue")

tk.Label(ventana, text="Menu Principal", font=("Arial", 16 , "bold"),bg="darkblue",fg="orange").pack(pady=10)

opciones = ["1.Continuar juego","2.Nuevo juego","3.Estadisticas de juegos","4.Salir"]

#======================================

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

#========================================

#Para poder ejecutar el programa
ventana.mainloop()

#=====================================
#Ventana del Menu Principal (Fin)
#=====================================