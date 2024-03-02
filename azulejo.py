import copy
class Azulejo:
    def __init__(self, color):
        self.color = color
        self.siguiente = None

costo_total= None

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

    def modificar(self, indice, nuevo_color):
        actual = self.primero
        contador = 0
        while actual is not None:
            if contador == indice:
                actual.color = nuevo_color
                return
            actual = actual.siguiente
            contador += 1
        return  # No se encontró la posición

    def movement_str(self, patron_objetivo,filas, columnas, costo_flip, costo_swap):
        if not self.esta_vacia():
            num_paso = 0
            aux_patron = copy.deepcopy(self)
            objetivo_azulejo_actual = patron_objetivo.primero
            azulejo_actual = aux_patron.primero
            print("\nPatron inicial:\n")
            aux_patron.imprimir(filas, columnas)
            print("\n")
            indice = 0
            global costo_total
            costo_total = 0
            while azulejo_actual is not None and objetivo_azulejo_actual is not None:
                if azulejo_actual.color == objetivo_azulejo_actual.color:
                    azulejo_actual= azulejo_actual.siguiente
                    objetivo_azulejo_actual = objetivo_azulejo_actual.siguiente
                    indice+=1
                elif azulejo_actual.color != objetivo_azulejo_actual.color:
                    if (indice+1) % (int(columnas)) == 0:
                            if aux_patron.get(indice+int(columnas)) == objetivo_azulejo_actual.color and patron_objetivo.get(indice+int(columnas)) == azulejo_actual.color:
                                num_paso+=1
                                aux_patron.modificar(indice, objetivo_azulejo_actual.color)
                                aux_patron.modificar(indice+int(columnas), patron_objetivo.get(indice+int(columnas)))
                                costo_total+=costo_swap
                                print(f"Paso {num_paso}, Intercambio por la parte inferior, Costo: Q{costo_swap}, COSTO ACUMULADO: {costo_total}" )
                                print(f"Entre el Azulejo {indice+1} y el {indice+int(columnas)+1}")
                                aux_patron.imprimir(filas, columnas)
                                azulejo_actual= azulejo_actual.siguiente
                                objetivo_azulejo_actual = objetivo_azulejo_actual.siguiente
                                indice+=1
                                if indice == int(filas)*int(columnas):
                                    return aux_patron
                            else:
                                num_paso+=1
                                if azulejo_actual.color == "B":
                                    aux_patron.modificar(indice, "N")
                                elif azulejo_actual.color == "N":
                                    aux_patron.modificar(indice, "B")
                                costo_total+=costo_flip
                                print(f"Paso {num_paso}, Volteo, Costo: Q{costo_flip}, , COSTO ACUMULADO: {costo_total}")
                                print(f"Azulejo {indice+1}")
                                aux_patron.imprimir(filas, columnas)
                                azulejo_actual= azulejo_actual.siguiente
                                objetivo_azulejo_actual = objetivo_azulejo_actual.siguiente
                                indice+=1
                                if indice == int(filas)*int(columnas):
                                    return
                    elif azulejo_actual.siguiente.color == objetivo_azulejo_actual.color and azulejo_actual.color == objetivo_azulejo_actual.siguiente.color:
                        num_paso+=1
                        aux_patron.modificar(indice, objetivo_azulejo_actual.color)
                        aux_patron.modificar(indice+1, azulejo_actual.siguiente.color)
                        costo_total+=costo_swap
                        print(f"Paso {num_paso}, Intercambio por la derecha, costo: {costo_swap}, , COSTO ACUMULADO: {costo_total}")
                        print(f"Entre el Azulejo {indice+1} y el {indice+2}")
                        aux_patron.imprimir(filas, columnas)
                        azulejo_actual= azulejo_actual.siguiente
                        objetivo_azulejo_actual = objetivo_azulejo_actual.siguiente
                        indice+=1
                    elif aux_patron.get(indice+int(columnas)) == objetivo_azulejo_actual.color and patron_objetivo.get(indice+int(columnas)) == azulejo_actual.color:
                        num_paso+=1
                        aux_patron.modificar(indice, objetivo_azulejo_actual.color)
                        aux_patron.modificar(indice+int(columnas), patron_objetivo.get(indice+int(columnas)))
                        costo_total+=costo_swap
                        print(f"Paso {num_paso}, Intercambio por la parte inferior, Costo: Q{costo_swap}, , COSTO ACUMULADO: {costo_total}")
                        print(f"Entre el Azulejo {indice+1} y el {indice+int(columnas)+1}")
                        aux_patron.imprimir(filas, columnas)
                        azulejo_actual= azulejo_actual.siguiente
                        
                        objetivo_azulejo_actual = objetivo_azulejo_actual.siguiente
                        indice+=1
                    elif azulejo_actual.color != objetivo_azulejo_actual.color:
                        num_paso+=1
                        if azulejo_actual.color == "B":
                            aux_patron.modificar(indice, "N")
                        elif azulejo_actual.color == "N":
                            aux_patron.modificar(indice, "B")
                        costo_total+=costo_flip
                        print(f"Paso {num_paso}, Volteo, Costo: Q{costo_flip}, , COSTO ACUMULADO: {costo_total}")
                        print(f"Azulejo {indice+1}")
                        aux_patron.imprimir(filas, columnas)
                        azulejo_actual= azulejo_actual.siguiente
                        objetivo_azulejo_actual = objetivo_azulejo_actual.siguiente
                        indice+=1
                    else:
                        azulejo_actual= azulejo_actual.siguiente
                        objetivo_azulejo_actual = objetivo_azulejo_actual.siguiente
                        indice+=1
            return aux_patron
                        

    def imprimir(self, filas, columnas):
        actual = self.primero
        for f in range(filas):
            for c in range(columnas):
                if actual:
                    print(f"[{actual.color}]", end=" ")
                    actual = actual.siguiente
                else:
                    print("[ ]", end=" ")  # Espacio para azulejos
            print()  # Nueva línea después de cada fila
        print("\n")