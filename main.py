class Piso:
    def __init__(self, nombre, filas, columnas,  slip, flip, patrones):
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.flip = flip
        self.slip = slip
        self.siguiente = None
        self.patrones = patrones

class Patrones:
    def __init__(self, codigo, colores):
        self.codigo = codigo
        self.colores = colores
        self.siguiente = None

class Azulejo:
    def __init__(self, color):
        self.color = color
        self.siguiente = None

class ListaEnlazada_Pisos:
    def __init__(self):
        self.primero = None

    def esta_vacia(self):
        return self.primero is None
    
    def add(self, nombre, filas, columnas, slip, flip, patrones):
        nuevo_nodo = Piso(nombre,filas, columnas, slip, flip, patrones)
        nuevo_nodo.siguiente = self.primero
        self.primero = nuevo_nodo

    def get(self):
        if not self.esta_vacia():
            piso_actual = self.primero
            while piso_actual is not None:
                print(piso_actual.patrones.get())
                piso_actual = piso_actual.siguiente
        else:
            print("La lista está vacia")

class ListaEnlazada_Patrones:
    def __init__(self):
        self.primero = None

    def esta_vacia(self):
        return self.primero is None
    
    def add(self, codigo, colores):
        nuevo_nodo = Patrones(codigo, colores)
        nuevo_nodo.siguiente = self.primero
        self.primero = nuevo_nodo
            
    def get(self):
        if not self.esta_vacia():
            patron_actual = self.primero
            while patron_actual is not None:
                print(patron_actual.colores)
                patron_actual = patron_actual.siguiente
        else:
            print("La lista está vacia")


class ListaEnlazada_Azulejos:
    def __init__(self):
        self.primero = None

    def esta_vacia(self):
        return self.primero is None
    
    def add(self, color):
        nuevo_nodo = Azulejo(color)
        nuevo_nodo.siguiente = self.primero
        self.primero = nuevo_nodo
            
    def get(self):
        if not self.esta_vacia():
            azulejo_actual = self.primero
            while azulejo_actual is not None:
                print(azulejo_actual.color)
                azulejo_actual = azulejo_actual.siguiente
        else:
            print("La lista está vacia")


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
        patrones_piso = ListaEnlazada_Patrones()
        azulejos_piso = ListaEnlazada_Azulejos()
        for patron in patrones:
            codigo = patron.get("codigo")
            azulejos = patron.text.strip()
            for azulejo in azulejos:
                nuevo_azulejo = azulejo
                azulejos_piso.add(nuevo_azulejo)
            patrones_piso.add(codigo, azulejos_piso)
            azulejos_piso.get()
        Pisos_disponibles.add(nombre_piso, columnas, Filas, costo_slip, costo_flip, patrones_piso)
        
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