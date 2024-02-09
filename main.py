def save_data(raiz):
    for hoja in raiz:
        print(hoja.get("nombres"))
        Columnas = hoja.find("R")
        print(Columnas.tag.strip())
        print(Columnas.text.strip())
        Filas = hoja.find("C")
        print(Filas.tag.strip())
        print(Filas.text.strip())
        Costo_change = hoja.find("F")
        print(Costo_change.tag.strip())
        print(Costo_change.text.strip())
        Costo_flip = hoja.find("S")
        print(Costo_flip.tag.strip())
        print(Costo_flip.text.strip())
        patrones = hoja.find("patrones")
        for patron in patrones:
            print(patron.get("codigo"))
            print(str(patron.text).strip())

import xml.etree.ElementTree as ET
import os
print("-----------Bienvenido-----------")
print("Por favor seleccione una opción")
respuesta = 0
while respuesta != str(2):
    print("1. Cargar archivo XML")
    print("2. Salir")
    respuesta = input("Opción: ")
    if respuesta == str(1):
        nombre_archivo = input("Ingrese el nombre del archivo XML en el escritorio: ")
        ruta_escritorio = os.path.join(os.path.expanduser("~"), "Desktop")
        ruta_xml = os.path.join(ruta_escritorio, nombre_archivo)
        if os.path.exists(ruta_xml):
            tree = ET.parse(ruta_xml)
            raiz = tree.getroot()
            save_data(raiz)
        else:
            print(f"El archivo {nombre_archivo} no existe en el escritorio.")
print("Gracias por usar nuestra aplicación")
print("Saliendo...")