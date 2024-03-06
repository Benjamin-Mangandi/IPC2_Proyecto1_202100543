class Patrones:
    def __init__(self, codigo, azulejos):
        self.codigo = codigo
        self.azulejos = azulejos
        self.siguiente = None

class ListaEnlazada_Patrones:
    def __init__(self):
        self.primero = None

    def esta_vacia(self):
        return self.primero is None
    
    def add(self, codigo, azulejos):
        nuevo_nodo = Patrones(codigo, azulejos)
        if self.esta_vacia() or codigo.lower()< self.primero.codigo.lower():
            nuevo_nodo.siguiente = self.primero
            self.primero = nuevo_nodo
        else:
            actual = self.primero
            while actual.siguiente is not None and actual.siguiente.codigo.lower()< codigo.lower():
                actual = actual.siguiente
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo
            
    def get(self):
        if not self.esta_vacia():
            patron_actual = self.primero
            while patron_actual is not None:
                print("Codigo Patrón: "+patron_actual.codigo)
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