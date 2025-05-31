import tkinter as tk
from tkinter import messagebox
import random

#===========================
# Funciones de apoyo
#===========================

def largolista(lista):
    if not lista:
        return 0
    contador = 0
    for _ in lista:
        contador += 1
    return contador

def esta_en_lista(elemento, lista):
    for item in lista:
        if item == elemento:
            return True
    return False

#=========================
# Tablero personalizable por el usuario
#=========================

MATRIZ_PERSONALIZABLE = [
    ['+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+'],
    ['+', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '+'],  
    ['+', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '+'],  
    ['+', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '+'],  
    ['+', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '+'], 
    ['+', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '+'],  
    ['+', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '+'],  
    ['+', 0, 0, 0, "X", 0, 0, 0, 0, 0, 0, '+'],  
    ['+', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '+'],  
    ['+', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '+'],  
    ['+', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '+'],  
    ['+', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '+'],
    ['+', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '+'],  
    ['+', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '+'],  
    ['+', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '+'],  
    ['+', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '+'],  
    ['+', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '+'],  
    ['+', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '+'],  
    ['+', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '+'],  
    ['+', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '+'],  
    ['+', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '+'],  
    ['+', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '+'],  
    ['+', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '+'],  
    ['+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+']
]

def crear_tablero():
    matriz = []
    for fila in MATRIZ_PERSONALIZABLE:
        nueva_fila = []
        for valor in fila:
            nueva_fila = nueva_fila + [valor]
        matriz = matriz + [nueva_fila]
    return matriz

piezas = {
    # Pieza O (Cuadrado) - No rota
    "O": [[
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,1,1,0,0],
        [0,1,1,0,0],
        [0,0,0,0,0]
    ]],

    # Pieza I (Línea) - 2 rotaciones
    "I": [
        # Vertical
        [[0,0,0,0,0], [0,0,2,0,0], [0,0,2,0,0], [0,0,2,0,0], [0,0,2,0,0]],
        # Horizontal
        [[0,0,0,0,0], [0,0,0,0,0], [2,2,2,2,0], [0,0,0,0,0], [0,0,0,0,0]]
    ],

    # Pieza L - 4 rotaciones
    "L": [
        # Rotación 0
        [[0,0,0,0,0], [0,0,3,0,0], [0,0,3,0,0], [0,0,3,3,0], [0,0,0,0,0]],
        # Rotación 1
        [[0,0,0,0,0], [0,0,0,0,0], [0,3,3,3,0], [0,3,0,0,0], [0,0,0,0,0]],
        # Rotación 2
        [[0,0,0,0,0], [0,3,3,0,0], [0,0,3,0,0], [0,0,3,0,0], [0,0,0,0,0]],
        # Rotación 3
        [[0,0,0,0,0], [0,0,0,3,0], [0,3,3,3,0], [0,0,0,0,0], [0,0,0,0,0]]
    ],

    # Pieza J - 4 rotaciones
    "J": [
        # Rotación 0
        [[0,0,0,0,0], [0,0,4,0,0], [0,0,4,0,0], [0,4,4,0,0], [0,0,0,0,0]],
        # Rotación 1
        [[0,0,0,0,0], [0,4,0,0,0], [0,4,4,4,0], [0,0,0,0,0], [0,0,0,0,0]],
        # Rotación 2
        [[0,0,0,0,0], [0,0,4,4,0], [0,0,4,0,0], [0,0,4,0,0], [0,0,0,0,0]],
        # Rotación 3
        [[0,0,0,0,0], [0,0,0,0,0], [4,4,4,0,0], [0,0,4,0,0], [0,0,0,0,0]]
    ],

    # Pieza T - 4 rotaciones
    "T": [
        # Rotación 0
        [[0,0,0,0,0], [0,0,0,0,0], [5,5,5,0,0], [0,5,0,0,0], [0,0,0,0,0]],
        # Rotación 1
        [[0,0,0,0,0], [0,5,0,0,0], [5,5,0,0,0], [0,5,0,0,0], [0,0,0,0,0]],
        # Rotación 2
        [[0,0,0,0,0], [0,5,0,0,0], [5,5,5,0,0], [0,0,0,0,0], [0,0,0,0,0]],
        # Rotación 3
        [[0,0,0,0,0], [0,5,0,0,0], [0,5,5,0,0], [0,5,0,0,0], [0,0,0,0,0]]
    ],

    # Pieza Z - 2 rotaciones
    "Z": [
        # Rotación 0
        [[0,0,0,0,0], [0,0,0,0,0], [6,6,0,0,0], [0,6,6,0,0], [0,0,0,0,0]],
        # Rotación 1
        [[0,0,0,0,0], [0,0,6,0,0], [0,6,6,0,0], [0,6,0,0,0], [0,0,0,0,0]]
    ],

    # Pieza S - 2 rotaciones
    "S": [
        # Rotación 0
        [[0,0,0,0,0], [0,0,0,0,0], [0,7,7,0,0], [7,7,0,0,0], [0,0,0,0,0]],
        # Rotación 1
        [[0,0,0,0,0], [0,7,0,0,0], [0,7,7,0,0], [0,0,7,0,0], [0,0,0,0,0]]
    ],

    # Pieza + (Cruz) - 4 rotaciones
    "Mas": [
        # Rotación 0
        [[0,0,0,0,0], [0,0,8,0,0], [0,8,8,8,0], [0,0,8,0,0], [0,0,0,0,0]],
        # Rotación 1 (igual que 0, es simétrica)
        [[0,0,0,0,0], [0,0,8,0,0], [0,8,8,8,0], [0,0,8,0,0], [0,0,0,0,0]],
        # Rotación 2 (igual que 0, es simétrica)
        [[0,0,0,0,0], [0,0,8,0,0], [0,8,8,8,0], [0,0,8,0,0], [0,0,0,0,0]],
        # Rotación 3 (igual que 0, es simétrica)
        [[0,0,0,0,0], [0,0,8,0,0], [0,8,8,8,0], [0,0,8,0,0], [0,0,0,0,0]]
    ],

    # Pieza U - 4 rotaciones
    "U": [
        # Rotación 0
        [[0,0,0,0,0], [0,0,0,0,0], [9,0,9,0,0], [9,9,9,0,0], [0,0,0,0,0]],
        # Rotación 1
        [[0,0,0,0,0], [0,9,9,0,0], [0,9,0,0,0], [0,9,9,0,0], [0,0,0,0,0]],
        # Rotación 2
        [[0,0,0,0,0], [0,0,0,0,0], [9,9,9,0,0], [9,0,9,0,0], [0,0,0,0,0]],
        # Rotación 3
        [[0,0,0,0,0], [0,9,9,0,0], [0,0,9,0,0], [0,9,9,0,0], [0,0,0,0,0]]
    ]
}

# Listas de los tipos de piezas y colores
TIPOS_PIEZAS = ["O", "I", "L", "J", "T", "Z", "S", "Mas", "U"]
COLORES_LISTA = ["yellow", "cyan", "orange", "blue", "purple", "red", "green", "magenta", "pink"]

def obtener_color(valor):
    if valor == '+':
        return "gray"
    elif valor == 'X':  # Obstáculos definidos por el usuario
        return "darkred"
    elif valor == 0:
        return "black"
    elif valor >= 1 and valor <= largolista(COLORES_LISTA):
        return COLORES_LISTA[valor - 1]
    else:
        return "white"

#==================
# Variables globales
#==================

matriz = crear_tablero()
piezaActiva = None
posicionX = 5
posicionY = 1
rotacion = 0
tipoPieza = ""
puntuacion = 0
nivel = 1
velocidad = 500
pausado = False
juego_terminado = False
movimiento_activo = False

#==================
# Funciones de juego
#==================

def mostrarTablero(matriz, frameTablero):
    for widget in frameTablero.winfo_children():
        widget.destroy()
    
    celdas = []
    
    for fila in range(largolista(matriz)):
        fila_celdas = []
        for col in range(largolista(matriz[0])):
            valor = matriz[fila][col]
            color = obtener_color(valor)
            
            celda = tk.Label(
                frameTablero, 
                width=3, 
                height=1, 
                borderwidth=1, 
                relief="solid",
                bg=color
            )
            celda.grid(row=fila, column=col, padx=0, pady=0)
            fila_celdas = fila_celdas + [celda]  
        celdas = celdas + [fila_celdas]  
    
    return celdas

def actualizar_tablero(celdas):
    for fila in range(largolista(matriz)):
        for col in range(largolista(matriz[0])):
            valor = matriz[fila][col]
            color = obtener_color(valor)
            celdas[fila][col].configure(bg=color)

def nuevaPieza():
    global piezaActiva, rotacion, tipoPieza, posicionX, posicionY
    
    indice = random.randint(0, largolista(TIPOS_PIEZAS) - 1)
    tipoPieza = TIPOS_PIEZAS[indice]
    piezaActiva = piezas[tipoPieza][0]
    rotacion = 0
    posicionX = 5
    posicionY = 1

def puedeMover(nuevaX, nuevaY, pieza=None):
    if pieza is None:
        pieza = piezaActiva
    
    for fila in range(5):
        for col in range(5):
            if pieza[fila][col] != 0:
                y = nuevaY + fila
                x = nuevaX + col
                
                # Se verfican los limites
                if (y < 0 or y >= largolista(matriz) or 
                    x < 0 or x >= largolista(matriz[0])):
                    return False
                
                # Se verfican las colisiones incluido el obstaculo
                if matriz[y][x] != 0:
                    return False
    return True

def insertarPieza():
    for fila in range(5):
        for col in range(5):
            if piezaActiva[fila][col] != 0:
                y = posicionY + fila
                x = posicionX + col
                if (0 <= y and y < largolista(matriz) and 
                    0 <= x and x < largolista(matriz[0])):
                    if matriz[y][x] == 0:
                        matriz[y][x] = piezaActiva[fila][col]

def borrarPieza():
    for fila in range(5):
        for col in range(5):
            if piezaActiva[fila][col] != 0:
                y = posicionY + fila
                x = posicionX + col
                if (0 <= y and y < largolista(matriz) and 
                    0 <= x and x < largolista(matriz[0])):
                    # Solo borrar si la celda contiene una pieza (número), NO obstáculos ni bordes
                    if (isinstance(matriz[y][x], int) and matriz[y][x] > 0 and 
                        matriz[y][x] != '+' and matriz[y][x] != 'X'):
                        matriz[y][x] = 0

def rotarPieza():
    global piezaActiva, rotacion
    
    if tipoPieza == "O":  # El cuadrado no posee rotacion
        return False
    
    # Guardar el estado actual
    pieza_anterior = piezaActiva
    rotacion_anterior = rotacion
    
    # Calcular la nueva rotación
    num_rotaciones = largolista(piezas[tipoPieza])
    nueva_rotacion = (rotacion + 1) % num_rotaciones
    nueva_pieza = piezas[tipoPieza][nueva_rotacion]
    
    # Verificar si es posible rotar
    if puedeMover(posicionX, posicionY, nueva_pieza):
        rotacion = nueva_rotacion
        piezaActiva = nueva_pieza
        return True
    
    return False

def verificarFilasCompletas():
    global puntuacion, nivel, velocidad
    
    filas_eliminadas = 0
    fila = largolista(matriz) - 2  
    
    while fila > 0:
        completa = True
        
        for col in range(1, largolista(matriz[0]) - 1):
            if matriz[fila][col] == 0 or matriz[fila][col] == 'X':
                completa = False
                break
        
        if completa:
            filas_eliminadas = filas_eliminadas + 1  
            
            for y in range(fila, 1, -1):
                for x in range(1, largolista(matriz[0]) - 1):
                    if MATRIZ_PERSONALIZABLE[y][x] == 'X':
                        matriz[y][x] = 'X'  
                    elif MATRIZ_PERSONALIZABLE[y-1][x] == 'X':
                        matriz[y][x] = 0    
                    else:
                        matriz[y][x] = matriz[y-1][x]  
            
            for x in range(1, largolista(matriz[0]) - 1):
                if MATRIZ_PERSONALIZABLE[1][x] == 'X':
                    matriz[1][x] = 'X'
                else:
                    matriz[1][x] = 0
                
        else:
            fila = fila - 1  
    
    if filas_eliminadas > 0:
        puntos = filas_eliminadas * 100 * nivel
        puntuacion = puntuacion + puntos  
        
        nuevo_nivel = (puntuacion // 1000) + 1
        if nuevo_nivel > nivel:
            nivel = nuevo_nivel
            velocidad = max(100, 500 - (nivel - 1) * 50)
    
    return filas_eliminadas

def moverPieza(direccion, celdas):
    global posicionX, posicionY
    
    if pausado or juego_terminado:
        return
    
    borrarPieza()
    
    if direccion == "izquierda" and puedeMover(posicionX - 1, posicionY):
        posicionX = posicionX - 1  
    elif direccion == "derecha" and puedeMover(posicionX + 1, posicionY):
        posicionX = posicionX + 1  
    elif direccion == "abajo" and puedeMover(posicionX, posicionY + 1):
        posicionY = posicionY + 1  
    elif direccion == "rotar":
        rotarPieza()
    
    insertarPieza()
    actualizar_tablero(celdas)

def caerPieza(frameTablero, celdas, labelPuntuacion, nombre_jugador="Jugador"):
    global posicionY, juego_terminado, movimiento_activo
    
    if juego_terminado or not movimiento_activo:
        return
    
    if pausado:
        frameTablero.after(100, lambda: caerPieza(frameTablero, celdas, labelPuntuacion, nombre_jugador))
        return
    
    borrarPieza()
    
    if puedeMover(posicionX, posicionY + 1):
        posicionY = posicionY + 1  
        insertarPieza()
        actualizar_tablero(celdas)
        frameTablero.after(velocidad, lambda: caerPieza(frameTablero, celdas, labelPuntuacion, nombre_jugador))
    else:
        insertarPieza()
        
        filas_eliminadas = verificarFilasCompletas()
        
        labelPuntuacion.config(text=f"Puntaje: {puntuacion}")
        actualizar_tablero(celdas)
        
        nuevaPieza()
        
        if not puedeMover(posicionX, posicionY):
            juego_terminado = True
            movimiento_activo = False
            messagebox.showinfo("Fin del juego", 
                               f"¡Juego terminado, {nombre_jugador}!\n\nPuntaje final: {puntuacion}\n\n¡Gracias por jugar!")
            return
        
        insertarPieza()
        actualizar_tablero(celdas)
        
        frameTablero.after(velocidad, lambda: caerPieza(frameTablero, celdas, labelPuntuacion, nombre_jugador))

def togglePausa():
    global pausado
    pausado = not pausado
    return pausado

def solicitar_nombre():
    ventana_nombre = tk.Toplevel(ventana)
    ventana_nombre.title("Ingresa tu nombre")
    ventana_nombre.geometry("400x300")
    ventana_nombre.configure(bg="darkblue")
    ventana_nombre.resizable(False, False)
    
    tk.Label(ventana_nombre, text="🎮 TETRIS EXTENDIDO 🎮", 
             font=("Arial", 16, "bold"), bg="darkblue", fg="yellow").pack(pady=20)
    
    tk.Label(ventana_nombre, text="Ingresa tu nombre:", 
             font=("Arial", 12), bg="darkblue", fg="white").pack(pady=10)
    
    nombre_jugador = tk.StringVar()
    entrada_nombre = tk.Entry(ventana_nombre, textvariable=nombre_jugador,
                             font=("Arial", 12), width=20, justify="center")
    entrada_nombre.pack(pady=10)
    entrada_nombre.focus()
    
    def iniciar_con_nombre():
        nombre = nombre_jugador.get().strip()
        if nombre:
            ventana_nombre.destroy()
            iniciarJuego(nombre)
        else:
            tk.Label(ventana_nombre, text="⚠️ Por favor ingresa tu nombre", 
                    font=("Arial", 10), bg="darkblue", fg="red").pack()
    
    tk.Button(ventana_nombre, text="🎮 ¡COMENZAR!", 
             font=("Arial", 12, "bold"), bg="green", fg="white",
             width=15, command=iniciar_con_nombre).pack(pady=20)
    
    def al_presionar_enter(event):
        iniciar_con_nombre()
    
    entrada_nombre.bind("<Return>", al_presionar_enter)

def iniciarJuego(nombre_jugador="Jugador"):
    global matriz, puntuacion, nivel, velocidad, pausado, juego_terminado, movimiento_activo
    
    matriz = crear_tablero()
    puntuacion = 0
    nivel = 1
    velocidad = 500
    pausado = False
    juego_terminado = False
    movimiento_activo = True
    
    ventanaJuego = tk.Toplevel(ventana)
    ventanaJuego.title(f"Tetris Extendido - {nombre_jugador}")
    ventanaJuego.configure(bg="black")
    ventanaJuego.resizable(False, False)
    
    panelInfo = tk.Frame(ventanaJuego, bg="black")
    panelInfo.pack(pady=10)
    
    tk.Label(panelInfo, text=f"🎮 Jugador: {nombre_jugador}", 
             font=("Arial", 12, "bold"), fg="cyan", bg="black").pack()
    
    labelPuntuacion = tk.Label(panelInfo, text=f"Puntaje: {puntuacion}", 
                              font=("Arial", 14, "bold"), fg="white", bg="black")
    labelPuntuacion.pack()
    
    panelPrincipal = tk.Frame(ventanaJuego, bg="black")
    panelPrincipal.pack(pady=10)
    
    frameTablero = tk.Frame(panelPrincipal, bg="black")
    frameTablero.pack(side="left", padx=20)
    
    panelControles = tk.Frame(panelPrincipal, bg="black")
    panelControles.pack(side="left", padx=20, fill="y")
    
    labelEstado = tk.Label(panelControles, text="", 
                          font=("Arial", 12, "bold"), fg="red", bg="black")
    labelEstado.pack(pady=5)
    
    tk.Label(panelControles, text="CONTROLES:", font=("Arial", 10, "bold"), 
             fg="yellow", bg="black").pack(pady=(10,5))
    
    instrucciones = [
        "← → : Mover lateralmente",
        "↓ : Caída rápida", 
        "Espacio: Rotar pieza",
        "P: Pausar/Reanudar"
    ]
    
    for inst in instrucciones:
        tk.Label(panelControles, text=inst, font=("Arial", 8), 
                fg="white", bg="black").pack(anchor="w")
    
    tk.Label(panelControles, text="", bg="black").pack(pady=10)  
    
    # Información de las piezas
    tk.Label(panelControles, text="PIEZAS:", font=("Arial", 10, "bold"), 
             fg="cyan", bg="black").pack()
    
    piezas_info = [
        "O: Cuadrado", "I: Línea", "L: Ele", "J: Jota", 
        "T: Te", "Z: Zeta", "S: Ese", "+: Cruz", "U: U"
    ]
    for info in piezas_info:
        tk.Label(panelControles, text=info, font=("Arial", 7), 
                fg="lightgray", bg="black").pack(anchor="w")
    
    tk.Label(panelControles, text="", bg="black").pack(pady=5)
    
    # Información de los obstáculos
    tk.Label(panelControles, text="OBSTÁCULOS:", font=("Arial", 9, "bold"), 
             fg="red", bg="black").pack()
    tk.Label(panelControles, text="Bloques rojos indestructibles", font=("Arial", 7), 
             fg="lightcoral", bg="black").pack()
    tk.Label(panelControles, text="Editables en el código", font=("Arial", 7), 
             fg="lightcoral", bg="black").pack()
    
    tk.Label(panelControles, text="", bg="black").pack(pady=10)  
    
    # Función para manejar la pausa
    def manejarPausa():
        pausado_actual = togglePausa()
        if pausado_actual:
            botonPausa.config(text="▶ Reanudar", bg="green")
            labelEstado.config(text="⏸ PAUSADO", fg="yellow")
        else:
            botonPausa.config(text="⏸ Pausa", bg="orange")
            labelEstado.config(text="▶ JUGANDO", fg="green")
    
    # Botones
    botonPausa = tk.Button(panelControles, text="⏸ Pausa", 
                          font=("Arial", 10, "bold"), bg="orange", fg="black",
                          width=12, command=manejarPausa)
    botonPausa.pack(pady=5)
    
    tk.Button(panelControles, text="🔄 Nuevo Juego", 
             font=("Arial", 10, "bold"), bg="green", fg="white",
             width=12, command=lambda: [ventanaJuego.destroy(), solicitar_nombre()]).pack(pady=5)
    
    tk.Button(panelControles, text="❌ Salir", 
             font=("Arial", 10, "bold"), bg="red", fg="white",
             width=12, command=ventanaJuego.destroy).pack(pady=5)
    
    # Inicializar estado
    labelEstado.config(text="▶ JUGANDO", fg="green")
    
    # Inicializar juego
    nuevaPieza()
    insertarPieza()
    celdas = mostrarTablero(matriz, frameTablero)
    
    # Configurar controles mejorados
    def manejar_tecla(event):
        # Se pausar incluso durante el juego 
        if event.keysym.lower() == "p":
            manejarPausa()
            return
        
        # Solo permitir otros controles si no está pausado
        if not pausado and not juego_terminado:
            if event.keysym == "Left":
                moverPieza("izquierda", celdas)
            elif event.keysym == "Right":
                moverPieza("derecha", celdas)
            elif event.keysym == "Down":
                moverPieza("abajo", celdas)
            elif event.keysym == "space":
                moverPieza("rotar", celdas)
    
    ventanaJuego.bind("<Key>", manejar_tecla)
    ventanaJuego.focus_set()
    
    # Cerrar juego al cerrar ventana
    def al_cerrar():
        global movimiento_activo
        movimiento_activo = False
        ventanaJuego.destroy()
    
    ventanaJuego.protocol("WM_DELETE_WINDOW", al_cerrar)
    
    # Iniciar caída automática
    caerPieza(frameTablero, celdas, labelPuntuacion, nombre_jugador)

def comingSoon():
    messagebox.showinfo("Próximamente", "Esta función estará disponible pronto")

def salir():
    ventana.quit()

#=====================================
# Ventana Principal
#=====================================

ventana = tk.Tk()
ventana.title("🎮 TETRIS EXTENDIDO 🎮")
ventana.geometry("600x500")
ventana.configure(bg="darkblue")
ventana.resizable(False, False)

# Título principal
tk.Label(ventana, text="🎮 TETRIS EXTENDIDO 🎮", 
         font=("Arial", 24, "bold"), bg="darkblue", fg="yellow").pack(pady=30)

tk.Label(ventana, text="¡Con obstáculos personalizables y piezas + y U!", 
         font=("Arial", 12, "bold"), bg="darkblue", fg="orange").pack(pady=5)

tk.Label(ventana, text="Menú Principal", 
         font=("Arial", 16, "bold"), bg="darkblue", fg="orange").pack(pady=10)

# Botones del menú
opciones = [
    ("🎯 Nuevo Juego", "red", solicitar_nombre),
    ("📊 Estadísticas", "gold", comingSoon),
    ("💾 Cargar Partida", "green", comingSoon),
    ("❌ Salir", "violet", salir)
]

for texto, color, comando in opciones:
    boton = tk.Button(ventana, text=texto, 
                     font=("Arial", 14, "bold"), bg=color, fg="white",
                     width=25, height=2, command=comando,
                     relief="raised", bd=3)
    boton.pack(pady=10)

# Información de controles y edición
tk.Label(ventana, text="Controles: ← → (mover) | ↓ (bajar) | ESPACIO (rotar) | P (pausa)", 
         font=("Arial", 10), bg="darkblue", fg="lightblue").pack(side="bottom", pady=10)

tk.Label(ventana, text="Para agregar obstáculos: Edita MATRIZ_PERSONALIZABLE en el código (cambia 0 por 'X')", 
         font=("Arial", 9), bg="darkblue", fg="lightcyan").pack(side="bottom", pady=5)

ventana.mainloop()