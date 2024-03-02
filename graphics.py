from graphviz import Graph

def crear_piso(piso_deseado, patron_deseado, num_patron):
    piso = Graph('G', filename='piso_'+piso_deseado.nombre+'_patron_'+num_patron+'.gv', engine='neato')
    
    piso.attr(overlap='false', splines='false', bgcolor='beige')

    piso.attr(label="Pisos de Guatemala, S.A.\n"+'Piso '+piso_deseado.nombre+ ', Patron: '+num_patron, fontsize='17', labelloc='t')
    
    piso.attr('node', shape='square', width='0.35', height='0.35', fixedsize='true', fontsize='0')

    indice =0
    
    for i in range(int(piso_deseado.filas)):
        for j in range(int(piso_deseado.columnas)):
            color_azulejo = patron_deseado.azulejos.get(indice)
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

def crear_piso_convertido(piso_deseado, patron_deseado, num_patron1, num_patron2, costo):
    piso = Graph('G', filename='piso_'+piso_deseado.nombre+'_patron_convertido_a_'+num_patron1+'.gv', engine='neato')
    
    piso.attr(overlap='false', splines='false', bgcolor='beige')

    piso.attr(label="Pisos de Guatemala, S.A.\n"+'Piso '+piso_deseado.nombre+ ', Patron: '+num_patron1+" Convertido a Patron: "+num_patron2+ "\nCOSTO: Q"+str(costo), fontsize='12', labelloc='t')
    
    piso.attr('node', shape='square', width='0.35', height='0.35', fixedsize='true', fontsize='0')

    indice =0
    
    for i in range(int(piso_deseado.filas)):
        for j in range(int(piso_deseado.columnas)):
            color_azulejo = patron_deseado.azulejos.get(indice)
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