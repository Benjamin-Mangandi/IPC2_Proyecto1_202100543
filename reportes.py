from graphviz import Graph

def crear_piso(piso_deseado, patron_deseado):
    piso = Graph('G', filename='piso'+piso_deseado.nombre+'.gv', engine='neato')
    
    piso.attr(overlap='false', splines='false', bgcolor='beige')

    piso.attr(label="Pisos de Guatemala, S.A.\n"+'Piso'+piso_deseado.nombre, fontsize='20', labelloc='t')
    
    piso.attr('node', shape='square', width='0.35', height='0.35', fixedsize='true', fontsize='0')

    indice =0
    
    for i in range(int(piso_deseado.filas)):
        for j in range(int(piso_deseado.columnas)):
            color_azulejo = patron_deseado.azulejos.get(indice)
            print(color_azulejo)
            indice+=1
            if str(color_azulejo) == "B":
                color = 'white'
            elif str(color_azulejo) == "N":
                color = 'black'
            piso.node(f'{i}{j}', style='filled', fillcolor=color)
    
    espaciado = 0.4
    for i in range(int(piso_deseado.filas)):  # Filas
        for j in range(int(piso_deseado.columnas)):  # Columnas
            pos_x = j * espaciado
            pos_y = -i * espaciado
            piso.node(f'{i}{j}', pos=f'{pos_x},{pos_y}!')
    
    piso.view()