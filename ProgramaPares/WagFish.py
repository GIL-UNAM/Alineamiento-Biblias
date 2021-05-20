"""
Las funciones de este script nos sirven para hacer las agrupaciones
"""
import Levishtein
import copy

def WagnerFisher(oracion1, oracion2):
    """
    Sacado de "Design of a concept-oriented tool for terminology", G. Sierra 1999 
    Es un algoritmo que nos da las agrupaciones de mínima edición. Una vez con la matriz de edición mínima,
    dependiendo de su naturaleza, se hacen las agrupaciones
    
    :param seq1: Es una lista de diccionarios que representa a la primera oración. Cada diccionario contiene el token, lemma y tag. 
    :param seq2: Es una lista de diccionarios que representa a la segunda oración. Cada diccionario contiene el token, lemma y tag.
    :returns: Una lista cuyos elementos son 3 listas. La primer lista (posición 0) es el agrupamiento de la primera oración
    La segunda lista (posicion 1) es el agrupamiento de la segunda oración.
    La tercera lista (posicion 2) representa al tipo de par en la posición i. Los pares pueden ser nulos, representados 
    por una 'N', pares iguales, representados por una 'I', o pares correspondientes, representados por una 'C'.
    """
    cost = Levishtein.levishtein(oracion1, oracion2) 
    i = len(oracion1) 
    j = len(oracion2) 
    lista_auxiliar = []
    lista1 = []
    lista2 = []
    while (i>0) and (j>0):
        if (cost[i][j] == cost[i-1][j]+1):
            lista1.insert(0, oracion1[i-1])
            lista2.insert(0, {'token': ' ', 'lemma': ' ', 'tag': ' '})
            lista_auxiliar.insert(0, 'N')
            i -= 1
        elif (cost[i][j] == cost[i][j-1]+1):
            lista1.insert(0, {'token': ' ', 'lemma': ' ', 'tag': ' '})
            lista2.insert(0, oracion2[j-1])
            lista_auxiliar.insert(0, 'N')
            j -= 1
        else:
            lista1.insert(0, oracion1[i-1])
            lista2.insert(0, oracion2[j-1])
            if Levishtein.palabras_equivalentes(oracion1[i-1], oracion2[j-1]):
                lista_auxiliar.insert(0, 'I')
            else:
                lista_auxiliar.insert(0, 'C')
            i = i-1
            j = j-1
    resultado = []
    resultado.append(lista1)
    resultado.append(lista2)
    resultado.append(lista_auxiliar)
    return resultado

def alinearConj(oracion1, r, oracion2, c, Z, C, rutas, maxAlineaciones=300):
    """
    Algoritmo recursivo de rutas múltiples
    """

    # Evaluación del número de alineaciones máximas
    if(maxAlineaciones > len(rutas)):

        # Palabra vacía
        palabra_vacia = {'token': ' ', 'lemma': ' ', 'tag': ' '}
        
        if r != 0:
            if c != 0:
                # Costos básicos
                w_a_b = 0 if Levishtein.palabras_equivalentes(oracion1[r-1], oracion2[c-1]) else 1
                w_e = 1
                
                if r >= 3 and c >= 3:
                    w_c = Levishtein.intercambio_conjuntivo(oracion1, oracion2, r-1, c-1)
                    if C[r][c] == C[r-3][c-3] + w_c:
                        cZ = copy.deepcopy(Z)
                        
                        cZ[0].insert(0, oracion1[r-3])
                        cZ[0].insert(0, oracion1[r-2])
                        cZ[0].insert(0, oracion1[r-1])
                        
                        cZ[1].insert(0, oracion2[c-1])
                        cZ[1].insert(0, oracion2[c-2])
                        cZ[1].insert(0, oracion2[c-3])
                        
                        cZ[2].insert(0, 'G')
                        cZ[2].insert(0, 'G')
                        cZ[2].insert(0, 'G')
                        
                        alinearConj(oracion1, r-3, oracion2, c-3, cZ, C, rutas, maxAlineaciones)
                
                if r >= 2 and c >= 2:
                    w_s = Levishtein.intercambio_consecutivo(oracion1, oracion2, r-1, c-1)
                    if C[r][c] == C[r-2][c-2] + w_s:
                        cZ = copy.deepcopy(Z)
                        
                        cZ[0].insert(0, oracion1[r-2])
                        cZ[0].insert(0, oracion1[r-1])
                        
                        cZ[1].insert(0, oracion2[c-1])
                        cZ[1].insert(0, oracion2[c-2])
                        
                        cZ[2].insert(0, 'J')
                        cZ[2].insert(0, 'J')
                        
                        alinearConj(oracion1, r-2, oracion2, c-2, cZ, C, rutas, maxAlineaciones)

                if C[r][c] == C[r-1][c-1] + w_a_b:
                    cZ = copy.deepcopy(Z)
                    
                    cZ[0].insert(0, oracion1[r-1])
                    cZ[1].insert(0, oracion2[c-1])
                    cZ[2].insert(0, 'I' if w_a_b == 0 else 'C') #
                    
                    alinearConj(oracion1, r-1, oracion2, c-1, cZ, C, rutas, maxAlineaciones)
                    
                if C[r][c] == C[r-1][c] + w_e:
                    cZ = copy.deepcopy(Z)
                    
                    cZ[0].insert(0, oracion1[r-1])
                    cZ[1].insert(0, palabra_vacia)
                    cZ[2].insert(0, 'N')
                    
                    alinearConj(oracion1, r-1, oracion2, c, cZ, C, rutas, maxAlineaciones)
                    
                if C[r][c] == C[r][c-1] + w_e:
                    cZ = copy.deepcopy(Z)
                    
                    cZ[0].insert(0, palabra_vacia)
                    cZ[1].insert(0, oracion2[c-1])
                    cZ[2].insert(0, 'N')
                    
                    alinearConj(oracion1, r, oracion2, c-1, cZ, C, rutas, maxAlineaciones)

            else:
                cZ = copy.deepcopy(Z)
                
                cZ[0].insert(0, oracion1[r-1])
                cZ[1].insert(0, palabra_vacia)
                cZ[2].insert(0, 'N')
                
                alinearConj(oracion1, r-1, oracion2, 0, cZ, C, rutas, maxAlineaciones)
        
        else:
            if c != 0:
                cZ = copy.deepcopy(Z)
                
                cZ[0].insert(0, palabra_vacia)
                cZ[1].insert(0, oracion2[c-1])
                cZ[2].insert(0, 'N')
                
                alinearConj(oracion1, 0, oracion2, c-1, cZ, C, rutas, maxAlineaciones)
                
            else:
                # Agregar alineamiento
                rutas.append(Z)
            

def WagFishConj(oracion1, oracion2):
    """
    Algoritmo de Wagner Fisher aplicado a la matriz de costos que considera a los
    intercambios consecutivo y conjuntivo
    
    :param oracion1: Es una lista de diccionarios que representa a la primera oración. Cada diccionario contiene el token, lemma y tag. 
    :param oracion2: Es una lista de diccionarios que representa a la segunda oración. Cada diccionario contiene el token, lemma y tag.
    :returns: Una lista cuyos elementos son 3 listas. La primer lista (posición 0) es el agrupamiento de la primera oración
    La segunda lista (posicion 1) es el agrupamiento de la segunda oración.
    La tercera lista (posicion 2) representa al tipo de par en la posición i. Los pares pueden ser nulos, representados 
    por una 'N', pares iguales, representados por una 'I', o pares correspondientes, representados por una 'C'.
    """
    
    r = len(oracion1)
    c = len(oracion2)
    Z = [ [], [], [] ]
    C = Levishtein.levi(oracion1, oracion2)
    rutas_multiples = []    
    alinearConj(oracion1, r, oracion2, c, Z, C, rutas_multiples, 16)
    
    return rutas_multiples
    

def pares_seminulos(alineacion):
    """
    A veces una palabra funcional resulta ser miembro de un par nulo 'N'. Esto puede afectar la condición de frontera o el cálculo de lcc de pares correspondientes que resultan ser
    pares léxicos, por ello conviene hacer que esas dos palabra funcional emparejada con el cáracter vacío se considere 
    un par igual.   
    Consideramos pares semi nulos a los que son Nulos y en donde la palabra no vacía está en nuestra stoplist
    o en donde su etiquetado POS indica que es una palabra funcional. Considerar esto incrementa el recall
    """
    stoplist = ['y', 'el', 'la', 'de', 'un'] 
    for i in range(len(alineacion[0])):
        if alineacion[2][i] == 'N':
            if alineacion[0][i]['lemma'] in stoplist:
                alineacion[2][i] = 'I'
            elif alineacion[0][i]['token'] in stoplist:
                alineacion[2][i] = 'I'
            elif alineacion[1][i]['lemma'] in stoplist:
                alineacion[2][i] = 'I'     
            elif alineacion[1][i]['token'] in stoplist:
                alineacion[2][i] = 'I'
            elif alineacion[1][i]['tag'] == 'SP':
                alineacion[2][i] = 'I'
            elif alineacion[0][i]['tag'] == 'SP': 
                alineacion[2][i] = 'I'
            elif alineacion[0][i]['tag'] == 'DA0MP0': 
                alineacion[2][i] = 'I'
            elif alineacion[1][i]['tag'] == 'DA0MP0': 
                alineacion[2][i] = 'I'



    return alineacion


def pares_semiguales(alineacion):
    """
    A veces dos palabras funcionales distintas resultan emparejadas, como son distintas entonces son un par
    correspondiente 'C'. Esto puede afectar la condición de frontera o el cálculo de lcc de pares correspondientes que resultan ser
    pares léxicos, por ello conviene hacer que esas dos palabras funcionales diferentes se consideren un par igual.
    Consideramos pares semi igual a los que contienen a dos palabras distintas cuyo etiquetado POS es 'SP'.
    
    :param alineacionacion: Es la alineación de dos versículos procesados
    :returns: La misma alineación cansiderando los pares siemi iguales 
    """

    for i in range(len(alineacion[0])):
        if (alineacion[0][i]['tag'] == alineacion[1][i]['tag']) and (alineacion[0][i]['tag'] == 'SP') : 
            alineacion[2][i] == 'I'
    return alineacion



def seminulos(alineacion):
    """
    Es la función pares_seminulos aplicada a la copia de una alineación para no alterar a la lista original
    """
    dummy = alineacion.copy()
    pares_seminull = pares_seminulos(dummy)
    dummy = pares_seminull.copy()
    resultado = pares_semiguales(dummy)
    return resultado

def semigual(alineacion):
    """
    Es la función pares_seminulos aplicada a la copia de una alineación para no alterara la lista original
    """
    dummy = alineacion.copy()
    pares_semigual = pares_semiguales(dummy)
    return pares_semigual

def semi(alineacion):
    """
    Considera los pares seminulos y los pares semiiguales, realiza las funciones 
    """
    dummy = alineacion.copy()
    pares_semi = pares_seminulos(dummy)
    pares_semi = pares_semiguales(pares_semi)
    return pares_semi


def POSWagnerFisher(oracion1, oracion2):
    """
    Hace el alineamiento utilizando las etiqueta parte de la oración. Es el mismo algoritmo pero aplicado a la matriz de costos que utiliza el etiquetado de 
    Partes de la oración   
    """
    cost = Levishtein.POSlevi(oracion1, oracion2) 
    i = len(oracion1)
    j = len(oracion2) 
    lista_auxiliar = []
    lista1 = []
    lista2 = []
    while (i>0) and (j>0):
        if (cost[i][j] == cost[i-1][j]+1):
            lista1.insert(0, oracion1[i-1])
            lista2.insert(0, {'token': ' ', 'lemma': ' ', 'tag': ' '})
            lista_auxiliar.insert(0, 'N')
            i -= 1
        elif (cost[i][j] == cost[i][j-1]+1):
            lista1.insert(0, {'token': ' ', 'lemma': ' ', 'tag': ' '})
            lista2.insert(0, oracion2[j-1])
            lista_auxiliar.insert(0, 'N')
            j -= 1
        else:
            lista1.insert(0, oracion1[i-1])
            lista2.insert(0, oracion2[j-1])
            if Levishtein.palabras_equivalentes(oracion1[i-1], oracion2[j-1]):
                lista_auxiliar.insert(0, 'I')
            else:
                lista_auxiliar.insert(0, 'C')
            i = i-1
            j = j-1
    resultado = []
    resultado.append(lista1)
    resultado.append(lista2)
    resultado.append(lista_auxiliar)
    return resultado
