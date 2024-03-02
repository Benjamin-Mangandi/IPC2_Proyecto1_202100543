import xml.etree.ElementTree as ET
import os
import graphics as graph
from piso import ListaEnlazada_Pisos
from patron import ListaEnlazada_Patrones
from azulejo import ListaEnlazada_Azulejos


def save_data(raiz):
    global Pisos_cargados
    Pisos_cargados = ListaEnlazada_Pisos()
    for hoja in raiz:  
        nombre_piso = hoja.get("nombres")
        tag_columnas = hoja.find("C")
        columnas = tag_columnas.text.strip()
        tag_Filas = hoja.find("R")
        filas = tag_Filas.text.strip()
        tag_Costo_flip = hoja.find("F")
        costo_flip = tag_Costo_flip.text.strip()
        tag_Costo_swap = hoja.find("S")
        costo_swap = tag_Costo_swap.text.strip()
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
        Pisos_cargados.add(nombre_piso, int(filas), int(columnas), 
                           int(costo_flip),int(costo_swap), patrones_piso)
    print("\nArchivo Cargado Con exito.\n")
        

print("-"*30+"Bienvenido"+"-"*30)
print("Por favor seleccione una opción")
Pisos_cargados = None
costo_total = None
respuesta_usuario = 0
while respuesta_usuario != str(2):
    print("1. Cargar archivo XML")
    print("2. Salir")
    respuesta_usuario = input("Opción: ")
    if respuesta_usuario == str(1):
        lista = ListaEnlazada_Pisos()
        nombre_archivo = input("Ingrese el nombre del archivo XML en el escritorio: ")
        ruta_escritorio = os.path.join(os.path.expanduser("~"), "Desktop")
        ruta_xml = os.path.join(ruta_escritorio, nombre_archivo)
        if os.path.exists(ruta_xml):
            tree = ET.parse(ruta_xml)
            raiz = tree.getroot()
            save_data(raiz)
            while respuesta_usuario != str(3):
                print("\nPor favor seleccione una opción")
                print("1. Seleccionar Piso")
                print("2. Mostrar Todos los pisos")
                print("3. Salir")
                respuesta_usuario = input("Opción: ")
                if respuesta_usuario == str(1):
                    piso_deseado = input("\nSeleccione un piso por medio del nombre: ")
                    piso_disponible = Pisos_cargados.disponibilidad(piso_deseado)
                    if piso_disponible is not None:
                        print("\n¡Piso Encontrado con exito!")
                        patron_deseado = input("\nSeleccione un patron por medio de su codigo: ")
                        patron_disponible = piso_disponible.patrones.disponibilidad(patron_deseado)
                        if patron_disponible is not None:
                            print("\n¡Patron Encontrado con exito!")
                            while respuesta_usuario != str(4):
                                print("\nSeleccione una opción para el patron:")
                                print("1. Mostrar graficamente")
                                print("2. Convertir patron a uno nuevo")
                                print("4. Salir")
                                respuesta_usuario = input("Opción: ")
                                if respuesta_usuario == str(1):
                                    graph.crear_piso(piso_disponible, patron_disponible, patron_deseado)
                                if respuesta_usuario == str(2):
                                    patron_deseado_convertir = input("\nSeleccione el otro patron por medio de su codigo: ")
                                    if patron_deseado != patron_deseado_convertir:
                                        patron_a_convertir = piso_disponible.patrones.disponibilidad(patron_deseado_convertir)
                                        if patron_a_convertir is not None:
                                            patron_disponible.azulejos.movement_str(patron_a_convertir.azulejos, piso_disponible.filas, 
                                                                                    piso_disponible.columnas, piso_disponible.flip, piso_disponible.swap)
                                            from azulejo import costo_total
                                            print(f"EL COSTO TOTAL ES: Q{costo_total}")
                                            graph.crear_piso_convertido(piso_disponible, patron_a_convertir, patron_deseado, 
                                                                        patron_deseado_convertir, costo_total)
                                        else:
                                            print("\nPatron no encontrado, intentelo nuevamente.")
                                    else:
                                        print("\nEl patron a convertir no puede ser el mismo. Intente con otro codigo.")
                                if respuesta_usuario == str(4):
                                    pass
                        else:
                            print("\nPatron no encontrado, intentelo de nuevo.")
                    else:
                        print("\nNo fue posible encontrar el piso, Intentelo de nuevo.\n")
                if respuesta_usuario == str(2):
                    Pisos_cargados.get()
        else:
            print(f"\nEl archivo {nombre_archivo} no existe en el escritorio.\n")
print("-"*20+"Gracias por usar nuestra aplicación"+"-"*20)
print("-"*32+"Saliendo...")