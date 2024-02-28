import xml.etree.ElementTree as ET
import os
import reportes as report

class Piso:
    def __init__(self, nombre, filas, columnas,  slip, flip, patrones):
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.flip = flip
        self.slip = slip
        self.patrones = patrones
        self.siguiente = None

class Patrones:
    def __init__(self, codigo, azulejos):
        self.codigo = codigo
        self.azulejos = azulejos
        self.siguiente = None

class Azulejo:
    def __init__(self, color):
        self.color = color
        self.siguiente = None

class ListaEnlazada_Pisos:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def esta_vacia(self):
        return self.primero is None
    
    def add(self, nombre, filas, columnas, slip, flip, patrones):
        nuevo_nodo = Piso(nombre,filas, columnas, slip, flip, patrones)
        if self.esta_vacia():
            self.primero = self.ultimo = nuevo_nodo
        else:
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo
            
    def get(self):
        if not self.esta_vacia():
            piso_actual = self.primero
            while piso_actual is not None:
                print("\nNombre: "+piso_actual.nombre)
                piso_actual.patrones.get()
                piso_actual = piso_actual.siguiente
        else:
            print("La lista está vacia")

    def disponibilidad(self, nombre):
        if not self.esta_vacia():
            piso_actual = self.primero
            while piso_actual is not None:
                if piso_actual.nombre == nombre:
                    return piso_actual
                else:
                    piso_actual = piso_actual.siguiente
        else:
            print("La lista está vacia")


class ListaEnlazada_Patrones:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def esta_vacia(self):
        return self.primero is None
    
    def add(self, codigo, azulejos):
        nuevo_nodo = Patrones(codigo, azulejos)
        if self.esta_vacia():
            self.primero = self.ultimo = nuevo_nodo
        else:
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo
            
    def get(self):
        if not self.esta_vacia():
            patron_actual = self.primero
            while patron_actual is not None:
                print("codigo patron: "+patron_actual.codigo)
                patron_actual = patron_actual.siguiente
        else:
            print("La lista está vacia")

    def disponibilidad(self, codigo):
        if not self.esta_vacia():
            patron_actual = self.primero
            while patron_actual is not None:
                if patron_actual.codigo == codigo:
                    return patron_actual
                else:
                    patron_actual = patron_actual.siguiente
        else:
            print("La lista está vacia")


class ListaEnlazada_Azulejos:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def esta_vacia(self):
        return self.primero is None
    
    def add(self, color):
        nuevo_nodo = Azulejo(color)
        if self.esta_vacia():
            self.primero = self.ultimo = nuevo_nodo
        else:
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo
            
    def get(self, indice):
        if not self.esta_vacia():
            azulejo_actual = self.primero
            conteo = 0
            while azulejo_actual is not None:
                if indice == conteo:
                    return azulejo_actual.color
                conteo+=1
                azulejo_actual=azulejo_actual.siguiente
        else:
            print("La lista está vacia")

    def movement(self, patron_objetivo,filas, columnas):
        if not self.esta_vacia():
            objetivo_azulejo_actual = patron_objetivo.primero
            azulejo_actual = self.primero
            indice = 0
            while azulejo_actual is not None and objetivo_azulejo_actual is not None:
                if azulejo_actual.color == objetivo_azulejo_actual.color:
                    azulejo_actual= azulejo_actual.siguiente
                    objetivo_azulejo_actual = objetivo_azulejo_actual.siguiente
                    indice+=1
                elif azulejo_actual.color != objetivo_azulejo_actual.color:
                    if (indice+1) % (int(columnas)) == 0:
                        if azulejo_actual.color != objetivo_azulejo_actual.color:
                            print("Volteo")
                            azulejo_actual= azulejo_actual.siguiente
                            objetivo_azulejo_actual = objetivo_azulejo_actual.siguiente
                            indice+=1
                            if indice == int(filas)*int(columnas):
                                return
                        else:
                            azulejo_actual= azulejo_actual.siguiente
                            objetivo_azulejo_actual = objetivo_azulejo_actual.siguiente
                            indice+=1
                            if indice == int(filas)*int(columnas):
                                return
                    if azulejo_actual.siguiente.color == objetivo_azulejo_actual.color:
                        print("Intercambio por la derecha")
                        azulejo_actual= azulejo_actual.siguiente
                        objetivo_azulejo_actual = objetivo_azulejo_actual.siguiente
                        indice+=1
                    elif self.get(indice+int(columnas)) == objetivo_azulejo_actual.color:
                        print("Intercambio por la parte inferior")
                        azulejo_actual= azulejo_actual.siguiente
                        objetivo_azulejo_actual = objetivo_azulejo_actual.siguiente
                        indice+=1
                    elif self.get(indice-int(columnas)) == objetivo_azulejo_actual.color:
                        print("Intercambio por la parte superior")
                        azulejo_actual= azulejo_actual.siguiente
                        objetivo_azulejo_actual = objetivo_azulejo_actual.siguiente
                        indice+=1
                    else:
                        print("Volteo")
                        azulejo_actual= azulejo_actual.siguiente
                        objetivo_azulejo_actual = objetivo_azulejo_actual.siguiente
                        indice+=1


def save_data(raiz):
    global Pisos_cargados
    Pisos_cargados = ListaEnlazada_Pisos()
    for hoja in raiz:  
        nombre_piso = hoja.get("nombres")
        tag_columnas = hoja.find("C")
        columnas = tag_columnas.text.strip()
        tag_Filas = hoja.find("R")
        Filas = tag_Filas.text.strip()
        Costo_change = hoja.find("F")
        costo_flip = Costo_change.text.strip()
        tag_Costo_flip = hoja.find("S")
        costo_slip = tag_Costo_flip.text.strip()
        patrones = hoja.find("patrones")
        patrones_piso = ListaEnlazada_Patrones()
        for patron in patrones:
            azulejos_piso = ListaEnlazada_Azulejos()
            codigo = patron.get("codigo")
            azulejos = patron.text.strip()
            for azulejo in azulejos:
                nuevo_azulejo = azulejo
                azulejos_piso.add(nuevo_azulejo)
            patrones_piso.add(codigo, azulejos_piso)
        Pisos_cargados.add(nombre_piso, Filas, columnas, costo_slip, costo_flip, patrones_piso)
    print("\nArchivo Cargado Con exito.\n")
        

print("-----------Bienvenido-----------")
print("Por favor seleccione una opción")
Pisos_cargados = None
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
            while respuesta != str(3):
                print("\nPor favor seleccione una opción")
                print("1. Seleccionar Piso")
                print("2. Mostrar Todos los pisos")
                print("3. Salir")
                respuesta = input("Opción: ")
                if respuesta == str(1):
                    piso_deseado = input("\nSeleccione un piso por medio del nombre: ")
                    piso_disponible = Pisos_cargados.disponibilidad(piso_deseado)
                    if piso_disponible is not None:
                        print("\n¡Piso Encontrado con exito!")
                        patron_deseado = input("\nSeleccione un patron por medio de su codigo: ")
                        patron_disponible = piso_disponible.patrones.disponibilidad(patron_deseado)
                        if patron_disponible is not None:
                            print("\n¡Patron Encontrado con exito!")
                            while respuesta != str(4):
                                print("\nSeleccione una opción para el patron:")
                                print("1. Mostrar graficamente")
                                print("2. Convertir patron a uno nuevo")
                                print("4. Salir")
                                respuesta = input("Opción: ")
                                if respuesta == str(1):
                                    report.crear_piso(piso_disponible, patron_disponible)
                                if respuesta == str(2):
                                    patron_deseado_convertir = input("\nSeleccione el otro patron por medio de su codigo: ")
                                    if patron_deseado != patron_deseado_convertir:
                                        patron_a_convertir = piso_disponible.patrones.disponibilidad(patron_deseado_convertir)
                                        if patron_a_convertir is not None:
                                            patron_disponible.azulejos.movement(patron_a_convertir.azulejos,piso_disponible.filas, piso_disponible.columnas )
                                        else:
                                            print("\nPatron no encontrado, intentelo nuevamente.")
                                    else:
                                        print("\nEl patron a convertir no puede ser el mismo. Intente con otro codigo.")
                                if respuesta == str(4):
                                    pass
                        else:
                            print("patron no encontrado, intentelo de nuevo.")
                    else:
                        print("No fue posible encontrar el piso, Intentelo de nuevo.\n")
            #break
                if respuesta == str(2):
                    Pisos_cargados.get()
        else:
            print(f"\nEl archivo {nombre_archivo} no existe en el escritorio.\n")
print("Gracias por usar nuestra aplicación")
print("Saliendo...")