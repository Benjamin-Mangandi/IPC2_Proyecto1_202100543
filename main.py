class Piso:
    def __init__(self, nombre, filas, columnas,  slip, flip):
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.flip = flip
        self.slip = slip
        self.siguiente = None

class ListaEnlazada_Pisos:
    def __init__(self):
        self.primero = None

    def esta_vacia(self):
        return self.primero is None
    
    def add(self, nombre, filas, columnas, slip, flip):
        nuevo_nodo = Piso(nombre,filas, columnas, slip, flip)
        if self.esta_vacia():
            self.primero = nuevo_nodo
        else:
            self.primero.siguiente = nuevo_nodo

    def get(self):
        if not self.esta_vacia():
            return self.primero.filas
        else:
            print("la cola está vacia")


def save_data(raiz):
    for hoja in raiz:
        nombre_piso = hoja.get("nombres")
        tag_columnas = hoja.find("R")
        columnas = tag_columnas.text.strip()
        tag_Filas = hoja.find("C")
        Filas = tag_Filas.text.strip()
        Costo_change = hoja.find("F")
        costo_flip = Costo_change.text.strip()
        tag_Costo_flip = hoja.find("S")
        costo_slip = tag_Costo_flip.text.strip()
        patrones = hoja.find("patrones")
        Pisos_disponibles = ListaEnlazada_Pisos()
        Pisos_disponibles.add(nombre_piso, columnas, Filas, costo_slip, costo_flip)
        for patron in patrones:
            pass
    print(Pisos_disponibles.get())
import xml.etree.ElementTree as ET
import os
print("-----------Bienvenido-----------")
print("Por favor seleccione una opción")
Pisos_disponibles = None
respuesta = 0
while respuesta != str(2):
    print("1. Cargar archivo XML")
    print("2. Salir")
    respuesta = input("Opción: ")
    if respuesta == str(1):
        lista = ListaEnlazada_Pisos()
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