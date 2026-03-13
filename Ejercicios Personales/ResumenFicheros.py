# -*- coding: utf-8 -*-
"""
Resumen de manejo de ficheros en Python
Formatos: .txt, .csv, .pickle
Incluye lectura, explicación, conversión y guardado
"""

import csv
import pickle

# -------------------------------
# 1. Funciones para leer archivos
# -------------------------------

def leer_txt(ruta):
    """
    Lee un archivo de texto plano (.txt)
    Cada línea se guarda como un elemento en una lista
    """
    with open(ruta, 'r', encoding='utf-8') as f:
        lineas = [linea.strip() for linea in f.readlines()]
    print(f"Archivo .txt leído: {lineas}")
    return lineas

def leer_csv(ruta):
    """
    Lee un archivo CSV (.csv)
    Devuelve una lista de listas (filas con columnas)
    """
    with open(ruta, newline='', encoding='utf-8') as f:
        lector = csv.reader(f)
        datos = [fila for fila in lector]
    print(f"Archivo .csv leído: {datos}")
    return datos

def leer_pickle(ruta):
    """
    Lee un archivo binario pickle (.pickle)
    Puede contener cualquier objeto de Python
    """
    with open(ruta, 'rb') as f:
        datos = pickle.load(f)
    print(f"Archivo .pickle leído: {datos}")
    return datos

# -------------------------------
# 2. Funciones para guardar archivos
# -------------------------------

def guardar_txt(datos, ruta):
    """
    Guarda una lista de datos en un archivo de texto
    Cada elemento será una línea
    """
    with open(ruta, 'w', encoding='utf-8') as f:
        for item in datos:
            f.write(str(item) + '\n')
    print(f"Datos guardados en {ruta}")

def guardar_csv(datos, ruta):
    """
    Guarda datos en formato CSV
    datos debe ser lista de listas
    """
    with open(ruta, 'w', newline='', encoding='utf-8') as f:
        escritor = csv.writer(f)
        escritor.writerows(datos)
    print(f"Datos guardados en {ruta}")

def guardar_pickle(datos, ruta):
    """
    Guarda cualquier objeto de Python en formato pickle
    """
    with open(ruta, 'wb') as f:
        pickle.dump(datos, f)
    print(f"Datos guardados en {ruta}")

# -------------------------------
# 3. Funciones de conversión
# -------------------------------

def txt_a_csv(ruta_txt, ruta_csv):
    """
    Convierte un .txt a .csv
    Cada línea del txt será una fila en el csv
    """
    lineas = leer_txt(ruta_txt)
    datos = [[linea] for linea in lineas]  # Cada línea en lista para CSV
    guardar_csv(datos, ruta_csv)

def csv_a_txt(ruta_csv, ruta_txt):
    """
    Convierte un .csv a .txt
    Cada fila del csv será una línea
    """
    datos = leer_csv(ruta_csv)
    lineas = [', '.join(fila) for fila in datos]  # Convertimos lista a string
    guardar_txt(lineas, ruta_txt)

def cualquier_a_pickle(datos, ruta_pickle):
    """
    Guarda cualquier dato en formato pickle
    """
    guardar_pickle(datos, ruta_pickle)

def pickle_a_txt(ruta_pickle, ruta_txt):
    """
    Convierte un pickle a un archivo de texto
    """
    datos = leer_pickle(ruta_pickle)
    # Si es lista o diccionario, convertir a string por línea
    if isinstance(datos, list):
        lineas = [str(d) for d in datos]
    elif isinstance(datos, dict):
        lineas = [f"{k}: {v}" for k,v in datos.items()]
    else:
        lineas = [str(datos)]
    guardar_txt(lineas, ruta_txt)

# -------------------------------
# 4. Explicación rápida
# -------------------------------
explicacion = """
.txt -> Archivo de texto plano, cada línea es texto. Fácil de leer, ligero, pero sin estructura.
.csv -> Archivo separado por comas, ideal para tablas y datos estructurados.
.pickle -> Archivo binario de Python. Guarda cualquier objeto, incluso listas, diccionarios, clases.
Para pasar de un formato a otro, primero leemos el archivo original, luego lo procesamos y lo guardamos
en el nuevo formato usando las funciones correspondientes.
"""

print(explicacion)

# -------------------------------
# 5. Ejemplos de uso
# -------------------------------

# Supongamos que tenemos "datos.txt" con líneas de texto
# txt_a_csv("datos.txt", "datos.csv")
# csv_a_txt("datos.csv", "datos2.txt")
# datos = leer_csv("datos.csv")
# cualquier_a_pickle(datos, "datos.pickle")
# pickle_a_txt("datos.pickle", "datos_desde_pickle.txt")