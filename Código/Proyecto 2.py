import tkinter as tk
from tkinter import messagebox
import random
import os
import time

#===========================
# Funciones de apoyo
#===========================
#Esta funcion reemplaza lo que haria la funcion de len
def largolista(lista):
    if not lista:
        return 0
    contador = 0
    for _ in lista:
        contador += 1
    return contador

#vVerfica si un elemento se encuentra en una lista
def esta_en_lista(elemento, lista):
    for item in lista:
        if item == elemento:
            return True
    return False

#=======================================
# Tablero personalizable por el usuario
#=======================================

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
    ['+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+']
]

#Crear el tablero que se utiliza en el juego
#E:La matriz personalizable que define el tablero del juego
#S:Retorna una matriz que representa el tablero del juego

def crear_tablero():
    matriz = []
    for fila in MATRIZ_PERSONALIZABLE:
        nueva_fila = []
        for valor in fila:
            nueva_fila = nueva_fila + [valor]
        matriz = matriz + [nueva_fila]
    return matriz

#En este diccionario se definen las piezas del juego
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

# Función para obtener el color de una celda según su valor
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

#====================
# Variables globales
#====================

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

#====================
# Funciones de juego
#====================

# Esta función muestra el tablero en la interfaz gráfica
#E:Se necesitan la matriz y los frame del tablero
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

# Esta función actualiza el color de las celdas del tablero según la matriz
#E:Se necesita la matriz y las celdas del tablero
def actualizar_tablero(celdas):
    for fila in range(largolista(matriz)):
        for col in range(largolista(matriz[0])):
            valor = matriz[fila][col]
            color = obtener_color(valor)
            celdas[fila][col].configure(bg=color)

#En esta funcion se llama a las piezas de manera aleatoria
def nuevaPieza():
    global piezaActiva, rotacion, tipoPieza, posicionX, posicionY
    
    indice = random.randint(0, largolista(TIPOS_PIEZAS) - 1)
    tipoPieza = TIPOS_PIEZAS[indice]
    piezaActiva = piezas[tipoPieza][0]
    rotacion = 0
    posicionX = 5
    posicionY = 1

#Esta función verifica si la pieza activa puede moverse a una nueva posición
#E:Recibe las nuevas coordenadas y una pieza opcional
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

# Esta función inserta la pieza activa en la matriz del tablero
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

# Esta función borra la pieza activa del tablero
def borrarPieza():
    for fila in range(5):
        for col in range(5):
            if piezaActiva[fila][col] != 0:
                y = posicionY + fila
                x = posicionX + col
                if (0 <= y and y < largolista(matriz) and 
                    0 <= x and x < largolista(matriz[0])):
                    # Solo se borra la celda contiene una pieza (número), NO obstáculos ni bordes
                    if (isinstance(matriz[y][x], int) and matriz[y][x] > 0 and 
                        matriz[y][x] != '+' and matriz[y][x] != 'X'):
                        matriz[y][x] = 0

# Esta función rota la pieza activa si es posible
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

#=====================================
# Funciones de Estadísticas
#=====================================

# Esta función carga las estadísticas desde un archivo
def cargar_estadisticas():
    """Carga las estadísticas desde el archivo, si existe"""
    ruta_stats = os.path.join(os.path.dirname(__file__), "estadisticas.txt")
    estadisticas = {
        "partidas_jugadas": 0,
        "puntuacion_maxima": 0,
        "mejor_jugador": "N/A",
        "nivel_maximo": 0,
        "tiempo_total": 0,
        "filas_eliminadas": 0
    }
    
    try:
        with open(ruta_stats, "r") as archivo:
            for linea in archivo:
                if ":" in linea:
                    clave, valor = linea.strip().split(":", 1)
                    if clave in estadisticas:
                        if clave in ["mejor_jugador"]:
                            estadisticas[clave] = valor.strip()
                        else:
                            estadisticas[clave] = int(valor.strip())
    except FileNotFoundError:
        pass
    
    return estadisticas

# Esta función guarda las estadísticas en un archivo
#E:Recibe un diccionario con las estadísticas a guardar 
def guardar_estadisticas(stats):
    """Guarda las estadísticas en el archivo"""
    ruta_stats = os.path.join(os.path.dirname(__file__), "estadisticas.txt")
    
    try:
        with open(ruta_stats, "w") as archivo:
            archivo.write(f"partidas_jugadas:{stats['partidas_jugadas']}\n")
            archivo.write(f"puntuacion_maxima:{stats['puntuacion_maxima']}\n")
            archivo.write(f"mejor_jugador:{stats['mejor_jugador']}\n")
            archivo.write(f"nivel_maximo:{stats['nivel_maximo']}\n")
            archivo.write(f"tiempo_total:{stats['tiempo_total']}\n")
            archivo.write(f"filas_eliminadas:{stats['filas_eliminadas']}\n")
    except Exception as e:
        print(f"Error guardando estadísticas: {e}")

# Esta función actualiza las estadísticas al finalizar una partida
#E:Recibe el nombre del jugador, puntuación final, nivel final, tiempo jugado y filas eliminadas
def actualizar_estadisticas_partida(nombre_jugador, puntuacion_final, nivel_final, tiempo_jugado, filas_total):
    """Actualiza las estadísticas con los datos de la partida terminada"""
    stats = cargar_estadisticas()
    
    stats["partidas_jugadas"] += 1
    
    if puntuacion_final > stats["puntuacion_maxima"]:
        stats["puntuacion_maxima"] = puntuacion_final
        stats["mejor_jugador"] = nombre_jugador
    
    if nivel_final > stats["nivel_maximo"]:
        stats["nivel_maximo"] = nivel_final
    
    stats["tiempo_total"] += tiempo_jugado
    stats["filas_eliminadas"] += filas_total
    
    guardar_estadisticas(stats)

# Esta función muestra una ventana con las estadísticas del juego
def mostrar_estadisticas():
    """Muestra la ventana de estadísticas"""
    stats = cargar_estadisticas()
    
    ventana_stats = tk.Toplevel()
    ventana_stats.title("📊 Estadísticas del Juego")
    ventana_stats.geometry("700x800")  # Aumentado de 500x600 a 700x800
    ventana_stats.configure(bg="navy")
    ventana_stats.resizable(False, False)
    
    # Título
    tk.Label(ventana_stats, text="📊 ESTADÍSTICAS DEL JUEGO", 
             font=("Arial", 20, "bold"), bg="navy", fg="gold").pack(pady=30)  # Aumentado padding
    
    # Marco principal para las estadísticas
    marco_stats = tk.Frame(ventana_stats, bg="lightblue", bd=3, relief="raised")
    marco_stats.pack(pady=30, padx=30, fill="both", expand=True)  # Aumentado padding
    
    # Estadísticas generales
    tk.Label(marco_stats, text="🎮 ESTADÍSTICAS GENERALES", 
             font=("Arial", 16, "bold"), bg="lightblue", fg="darkblue").pack(pady=15)  # Aumentado fuente y padding
    
    # Crear las estadísticas
    estadisticas_mostrar = [
        ("🎯 Partidas Jugadas:", stats["partidas_jugadas"]),
        ("🏆 Puntuación Máxima:", f"{stats['puntuacion_maxima']:,}"),
        ("👑 Mejor Jugador:", stats["mejor_jugador"]),
        ("📈 Nivel Máximo Alcanzado:", stats["nivel_maximo"]),
        ("⏱️ Tiempo Total Jugado:", f"{stats['tiempo_total']//60}m {stats['tiempo_total']%60}s"),
        ("🧱 Filas Eliminadas Totales:", stats["filas_eliminadas"])
    ]
    
    for etiqueta, valor in estadisticas_mostrar:
        frame_stat = tk.Frame(marco_stats, bg="lightblue")
        frame_stat.pack(fill="x", padx=25, pady=8)  # Aumentado padding
        
        tk.Label(frame_stat, text=etiqueta, 
                font=("Arial", 13, "bold"), bg="lightblue", fg="darkred").pack(side="left")  # Aumentado fuente
        tk.Label(frame_stat, text=str(valor), 
                font=("Arial", 13), bg="lightblue", fg="black").pack(side="right")  # Aumentado fuente
    
    # Separador
    tk.Label(marco_stats, text="", bg="lightblue").pack(pady=15)  # Aumentado padding
    
    # Estadísticas calculadas
    tk.Label(marco_stats, text="📊 ESTADÍSTICAS CALCULADAS", 
             font=("Arial", 16, "bold"), bg="lightblue", fg="darkblue").pack(pady=10)  # Aumentado fuente
    
    # Calcular promedios si hay partidas
    if stats["partidas_jugadas"] > 0:
        promedio_puntos = stats["puntuacion_maxima"] // stats["partidas_jugadas"]
        promedio_tiempo = stats["tiempo_total"] // stats["partidas_jugadas"]
        promedio_filas = stats["filas_eliminadas"] // stats["partidas_jugadas"]
    else:
        promedio_puntos = 0
        promedio_tiempo = 0
        promedio_filas = 0
    
    estadisticas_calculadas = [
        ("💯 Puntuación Promedio:", f"{promedio_puntos:,}"),
        ("⏰ Tiempo Promedio por Partida:", f"{promedio_tiempo//60}m {promedio_tiempo%60}s"),
        ("📦 Filas Promedio por Partida:", promedio_filas)
    ]
    
    for etiqueta, valor in estadisticas_calculadas:
        frame_calc = tk.Frame(marco_stats, bg="lightblue")
        frame_calc.pack(fill="x", padx=25, pady=8)  # Aumentado padding
        
        tk.Label(frame_calc, text=etiqueta, 
                font=("Arial", 13, "bold"), bg="lightblue", fg="darkgreen").pack(side="left")  # Aumentado fuente
        tk.Label(frame_calc, text=str(valor), 
                font=("Arial", 13), bg="lightblue", fg="black").pack(side="right")  # Aumentado fuente
    
    # Botones
    frame_botones = tk.Frame(ventana_stats, bg="navy")
    frame_botones.pack(pady=30)  # Aumentado padding
    
    tk.Button(frame_botones, text="🔄 Actualizar", 
             font=("Arial", 14, "bold"), bg="green", fg="white",  # Aumentado fuente
             width=14, height=2,  # Aumentado tamaño de botones
             command=lambda: [ventana_stats.destroy(), mostrar_estadisticas()]).pack(side="left", padx=15)
    
    tk.Button(frame_botones, text="🗑️ Resetear", 
             font=("Arial", 14, "bold"), bg="red", fg="white",  # Aumentado fuente
             width=14, height=2,  # Aumentado tamaño de botones
             command=lambda: resetear_estadisticas(ventana_stats)).pack(side="left", padx=15)
    
    tk.Button(frame_botones, text="❌ Cerrar", 
             font=("Arial", 14, "bold"), bg="gray", fg="white",  # Aumentado fuente
             width=14, height=2,  # Aumentado tamaño de botones
             command=ventana_stats.destroy).pack(side="left", padx=15)

# Esta función resetea todas las estadísticas después de confirmación
#E:Recibe una ventana padre opcional para cerrar después del reset
def resetear_estadisticas(ventana_padre=None):
    """Resetea todas las estadísticas después de confirmación"""
    respuesta = messagebox.askyesno("Confirmar Reset", 
                                   "¿Estás seguro de que quieres resetear todas las estadísticas?\n\n" +
                                   "Esta acción no se puede deshacer.")
    
    if respuesta:
        estadisticas_vacias = {
            "partidas_jugadas": 0,
            "puntuacion_maxima": 0,
            "mejor_jugador": "N/A",
            "nivel_maximo": 0,
            "tiempo_total": 0,
            "filas_eliminadas": 0
        }
        
        guardar_estadisticas(estadisticas_vacias)
        messagebox.showinfo("Estadísticas Reseteadas", "Todas las estadísticas han sido reseteadas.")
        
        if ventana_padre:
            ventana_padre.destroy()
            mostrar_estadisticas()

# Variables globales para el seguimiento de estadísticas
tiempo_inicio_partida = 0
filas_eliminadas_partida = 0

# Esta función verifica si hay filas completas y las elimina
def verificarFilasCompletas():
    global puntuacion, nivel, velocidad, filas_eliminadas_partida
    
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
        filas_eliminadas_partida += filas_eliminadas  # Actualizar contador
        puntos = filas_eliminadas * 100 * nivel
        puntuacion = puntuacion + puntos  
        
        nuevo_nivel = (puntuacion // 1000) + 1
        if nuevo_nivel > nivel:
            nivel = nuevo_nivel
            velocidad = max(100, 500 - (nivel - 1) * 50)
    
    return filas_eliminadas

# Esta función mueve la pieza activa en la dirección indicada
#E:Recibe la dirección de movimiento y las celdas del tablero
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

# Esta función hace caer la pieza activa en el tablero
#E:Recibe el frame del tablero, las celdas y el label de puntuación
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
            
            # Actualizar estadísticas al finalizar el juego
            tiempo_jugado = int(time.time()) - tiempo_inicio_partida
            actualizar_estadisticas_partida(nombre_jugador, puntuacion, nivel, tiempo_jugado, filas_eliminadas_partida)
            
            messagebox.showinfo("Fin del juego", 
                               f"¡Juego terminado, {nombre_jugador}!\n\nPuntaje final: {puntuacion}\nTiempo jugado: {tiempo_jugado//60}m {tiempo_jugado%60}s\nFilas eliminadas: {filas_eliminadas_partida}\n\n¡Gracias por jugar!")
            return
        
        insertarPieza()
        actualizar_tablero(celdas)
        
        frameTablero.after(velocidad, lambda: caerPieza(frameTablero, celdas, labelPuntuacion, nombre_jugador))

# Esta función alterna el estado de pausa del juego
def togglePausa():
    global pausado
    pausado = not pausado
    return pausado

# Esta función solicita el nombre del jugador antes de iniciar el juego
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
    
    # Función para iniciar el juego con el nombre ingresado
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
    
    # Bind para iniciar el juego al presionar Enter
    #E:Se necesita un event
    def al_presionar_enter(event):
        iniciar_con_nombre()
    
    entrada_nombre.bind("<Return>", al_presionar_enter)

# Esta función inicia el juego y configura la ventana principal
#E:Recibe el nombre del jugador opcionalmente
def iniciarJuego(nombre_jugador="Jugador"):
    global matriz, puntuacion, nivel, velocidad, pausado, juego_terminado, movimiento_activo, tiempo_inicio_partida, filas_eliminadas_partida
    
    # Inicializar seguimiento de estadísticas
    import time
    tiempo_inicio_partida = int(time.time())
    filas_eliminadas_partida = 0
    
    if matriz == [] or not isinstance(matriz[0], list):
        matriz = crear_tablero()
        puntuacion = 0
        nivel = 1
        velocidad = 500
    puntuacion = 0
    nivel = 1
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
    
    # Instrucciones de control
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
    
    botonesLateral = tk.Frame(panelControles, bg="black")
    botonesLateral.pack(pady=10)

    tk.Button(botonesLateral, text="Guardar", font=("Arial", 10, "bold"),
          bg="blue", fg="white", width=12,
          command=lambda: guardar_partida(nombre_jugador)).pack(pady=5)

        
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

directorio_actual = os.path.dirname(__file__)
ruta_partida = os.path.join(directorio_actual, "partida_guardada.txt")

# Esta función guarda la partida actual en un archivo
#E:Recibe el nombre del jugador opcionalmente
def guardar_partida(nombre_jugador="Jugador"):
    carpeta = os.path.dirname(__file__)
    i = 1

    while i <= 99:
        numero = str(i)
        if i < 10:
            numero = "0" + numero
        nombre_archivo = "partida_" + numero + ".txt"
        ruta = carpeta + "/" + nombre_archivo

        try:
            archivo = open(ruta, "r")
            archivo.close()
            i = i + 1
        except:
            break

    if i > 99:
        messagebox.showwarning("Límite alcanzado", "Ya existen 99 partidas guardadas.")
        return

    archivo = open(ruta, "w")

    fila_i = 0
    while fila_i < largolista(matriz):
        fila = matriz[fila_i]
        k = 0
        linea = ""
        while k < largolista(fila):
            linea = linea + str(fila[k]) + ","
            k = k + 1
        archivo.write(linea[:-1] + "\n")
        fila_i = fila_i + 1

    archivo.write("---\n")
    archivo.write(str(posicionX) + "\n")
    archivo.write(str(posicionY) + "\n")
    archivo.write(str(puntuacion) + "\n")
    archivo.write(str(velocidad) + "\n")
    archivo.write(tipoPieza + "\n")
    archivo.write(str(rotacion) + "\n")
    archivo.write(nombre_jugador + "\n")  

    archivo.close()
    messagebox.showinfo("Partida guardada", f"Se guardó como {nombre_archivo}")

# Esta función carga una partida guardada desde un archivo
def cargar_partida():
    global ventana
    carpeta = os.path.dirname(__file__)
    archivos = []

    # Buscar solo archivos que existan (más eficiente)
    for i in range(1, 100):
        numero = str(i).zfill(2)
        ruta = os.path.join(carpeta, f"partida_{numero}.txt")
        if os.path.exists(ruta):
            archivos = archivos + [ruta]  # Usar concatenación en lugar de append

    if archivos == []:  # Comparar con lista vacía en lugar de not
        messagebox.showwarning("Sin partidas", "No se encontraron partidas guardadas.")
        return

    ventana_selector = tk.Toplevel()
    ventana_selector.title("Partidas Disponibles")
    ventana_selector.geometry("350x450")
    ventana_selector.configure(bg="white")

    tk.Label(ventana_selector, text="Selecciona una partida", font=("Arial", 14, "bold"), bg="white").pack(pady=10)
    contenedor = tk.Frame(ventana_selector, bg="white")
    contenedor.pack(fill="both", expand=True)
    # Función para cargar una partida desde un archivo
    #E:Recibe la ruta del archivo y el nombre del jugador
    def cargar_desde(ruta_archivo, nombre_jugador):
        global matriz, posicionX, posicionY, puntuacion, velocidad, tipoPieza, rotacion, piezaActiva, nivel, pausado, juego_terminado, movimiento_activo
        
        try:
            with open(ruta_archivo, "r") as archivo:
                lineas = archivo.readlines()

            # Reconstruir matriz
            matriz = []
            i = 0
            while i < largolista(lineas) and lineas[i].strip() != "---":  # Usar largolista en lugar de len
                fila = lineas[i].strip().split(",")
                fila_convertida = []
                for valor in fila:
                    v = valor.strip()
                    if v == '+' or v == 'X':
                        fila_convertida = fila_convertida + [v]  # Concatenación
                    elif v.isdigit():
                        fila_convertida = fila_convertida + [int(v)]  # Concatenación
                    else:
                        fila_convertida = fila_convertida + [0]  # Concatenación
                matriz = matriz + [fila_convertida]  # Concatenación
                i = i + 1

            # Leer datos del juego
            if i + 6 < largolista(lineas):  # Usar largolista en lugar de len
                i = i + 1  # Saltar la línea "---"
                posicionX = int(lineas[i].strip())
                posicionY = int(lineas[i+1].strip())
                puntuacion = int(lineas[i+2].strip())
                velocidad = int(lineas[i+3].strip())
                tipoPieza = lineas[i+4].strip()
                rotacion = int(lineas[i+5].strip())
                
                # Validar que la pieza existe
                if esta_en_lista(tipoPieza, TIPOS_PIEZAS) and rotacion < largolista(piezas[tipoPieza]):  # Usar funciones auxiliares
                    piezaActiva = piezas[tipoPieza][rotacion]
                else:
                    # Pieza por defecto si hay error
                    tipoPieza = "O"
                    rotacion = 0
                    piezaActiva = piezas["O"][0]

                # Recalcular nivel basado en puntuación
                nivel = (puntuacion // 1000) + 1
                
                # Reinicializar estado del juego
                pausado = False
                juego_terminado = False
                movimiento_activo = True

                ventana_selector.destroy()
                iniciarJuego(nombre_jugador)
            else:
                messagebox.showerror("Error", "Archivo de partida corrupto")
                
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar la partida: {str(e)}")

    # Mostrar partidas disponibles de manera más eficiente
    partidas_encontradas = 0
    for j in range(largolista(archivos)):  # Usar largolista y range
        archivo = archivos[j]
        try:
            with open(archivo, "r") as f:
                lineas = f.readlines()

            # Buscar el separador ---
            separador_index = -1
            for i in range(largolista(lineas)):  # Usar largolista
                if lineas[i].strip() == "---":
                    separador_index = i
                    break

            if separador_index == -1 or separador_index + 7 >= largolista(lineas):  # Usar largolista
                continue

            puntos = int(lineas[separador_index + 3].strip())
            nombre = "Jugador"
            if separador_index + 7 < largolista(lineas):  # Usar largolista
                nombre = lineas[separador_index + 7].strip()

            partida = tk.Frame(contenedor, bg="lightgray", bd=2, relief="raised")
            partida.pack(pady=5, padx=10, fill="x")

            lbl1 = tk.Label(partida, text=f"Partida {str(j+1).zfill(2)}", font=("Arial", 10, "bold"), bg="lightgray")
            lbl2 = tk.Label(partida, text=f"Jugador: {nombre}", font=("Arial", 10), bg="lightgray")
            lbl3 = tk.Label(partida, text=f"Puntaje: {puntos}", font=("Arial", 10), bg="lightgray")
            
            lbl1.pack(anchor="w", padx=10)
            lbl2.pack(anchor="w", padx=10)
            lbl3.pack(anchor="w", padx=10)

            # Eventos de clic
            for widget in [partida, lbl1, lbl2, lbl3]:
                widget.bind("<Button-1>", lambda e, r=archivo, n=nombre: cargar_desde(r, n))
                
            partidas_encontradas = partidas_encontradas + 1  # Incremento manual
            
        except Exception as ex:
            print(f"Error leyendo {archivo}: {ex}")
            continue

    if partidas_encontradas == 0:
        tk.Label(contenedor, text="No hay partidas válidas para mostrar.", bg="white", fg="red").pack(pady=20)

#=====================================
# Función para salir de la aplicación
def salir():
    ventana.destroy()

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
    ("📊 Estadísticas", "gold", mostrar_estadisticas),
    ("💾 Cargar Partida", "green", cargar_partida),  
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