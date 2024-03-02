class Piso:
    def __init__(self, nombre, filas, columnas,flip, swap, patrones):
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.flip = flip
        self.swap = swap
        self.patrones = patrones
        self.siguiente = None

class ListaEnlazada_Pisos:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def esta_vacia(self):
        return self.primero is None
    
    def add(self, nombre, filas, columnas, swap, flip, patrones):
        nuevo_nodo = Piso(nombre,filas, columnas, swap, flip, patrones)
        if self.esta_vacia() or nombre.lower()< self.primero.nombre.lower():
            nuevo_nodo.siguiente = self.primero
            self.primero = self.ultimo = nuevo_nodo
        else:
            actual = self.primero
            while actual.siguiente is not None and actual.siguiente.nombre.lower()< nombre.lower():
                actual = actual.siguiente
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo
            
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