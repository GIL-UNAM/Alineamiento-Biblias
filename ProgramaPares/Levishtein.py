##Sacado de "Design of a concept-oriented tool for terminology", G. Sierra 1999

import numpy as np
import unidecode

def levishtein (seq1, seq2):
    """
    De "Design of a concept-oriented tool for terminology", G. Sierra 1999
    Calcula la distancia de edición entre dos oraciones
    
    :param seq1: La primera oracion que vamos a comparar
    :param seq2: La segunda oracion que vamos a comparar
    :returns: La matriz de edición
    """
    n = len(seq1)
    m = len(seq2)
    matriz = np.zeros((n+1, m+1))
    for i in range(n+1):
        matriz [i, 0] = i
    for j in range(m+1):
        matriz [0, j] = j
    for i in range(1, n+1):
        for j in range(1, m+1):
            if palabras_equivalentes(seq1[i-1], seq2[j-1]):
                matriz[i][j] = min(matriz[i-1][j]+1, matriz[i][j-1] + 1, matriz[i-1][j-1])
            else:
                matriz[i][j] = min(matriz[i-1][j] + 1, matriz[i][j-1] + 1, matriz[i-1][j-1]+1)
    return matriz



def palabras_equivalentes(palabra1, palabra2):
    """
    Consideramos dos palabras como equivalentes si tienen el mismo lemma. Como el
    lemmatizador puede fallar, también consideramos el token
    
    :param palabra1: Es un diccionario que conseguimos gracias al tagger 'freeling'.
    contiene el token, el lemma y el tag.
    :param palabra2: Es un diccionario que conseguimos gracias al tagger 'freeling'.
    contiene el token, el lemma y el tag.
    :returns: True si son palabras equivalentes, False en caso contrario
    """
    if unidecode.unidecode(palabra1['lemma'].lower()) == unidecode.unidecode(palabra2['lemma'].lower()):
        return True
    elif unidecode.unidecode(palabra1['token'].lower()) == unidecode.unidecode(palabra2['token'].lower()):
        return True
    else:
        return False

#####################

def intercambio_consecutivo(seq1, seq2, i, j):
    """
    Sacado de "ALGORITMO REVISADO PARA LA EXTRACCIÓN AUTOMÁTICA DE AGRUPAMIENTOS SEMÁNTICOS' G. Castillo 2002
    En ocasiones hay dos palabras que aparecen en orden contrario. Cuando esto ocurre, podríamos considerar esto al momento de hacer el agrupamiento.
    Esta funcion determina si existe esta inversión y ayuda a su agrupamiento. Ejemplo: "comida rica" "rica comida" 
    
    :param seq1: La primer oración a comparar. Es una lista donde el i-ésimo elemento es un diccionario que representa a la i-ésima palabra, con su token, lemma y tag
    :param seq1: La segunda oración a comparar. Es una lista donde el i-ésimo elemento es un diccionario que representa a la i-ésima palabra, con su token, lemma y tag
    :param i: representa una posición en la oración 1.
    :param j: representa una posición en la oración 2.
    :returns: 1 si hay un intercambio consecutivo, 100 si no.
    """
    if palabras_equivalentes(seq1[i], seq2[j-1]) and palabras_equivalentes(seq1[i-1], seq2[j]):
        return 1
    else:
        return 100
    
def intercambio_conjuntivo(seq1, seq2, i, j):
    """
    Sacado de "ALGORITMO REVISADO PARA LA EXTRACCIÓN AUTOMÁTICA DE AGRUPAMIENTOS SEMÁNTICOS' G. Castillo 2002
    En ocasiones hay dos palabras que aparecen en orden contrario después de la palabra "y". Cuando esto ocurre, podríamos considerar esto al momento de hacer el agrupamiento.
    Esta funcion determina si existe esta inversión y ayuda a su agrupamiento. Ejemplo: "blanco y negro" "negro y blanco"
    
    :param seq1: La primer oración a comparar. Es una lista donde el i-ésimo elemento es un diccionario que representa a la i-ésima palabra, con su token, lemma y tag
    :param seq1: La segunda oración a comparar. Es una lista donde el i-ésimo elemento es un diccionario que representa a la i-ésima palabra, con su token, lemma y tag
    :param i: representa una posición en la oración 1.
    :param j: representa una posición en la oración 2.
    :returns: 1 si hay un intercambio conjuntivo, 100 si no.    
    """
    if palabras_equivalentes(seq1[i-1], seq2[j-1]) and seq1[i-1]['token']== 'y':  
        if palabras_equivalentes(seq1[i-2], seq2[j]) and palabras_equivalentes(seq1[i], seq2[j-2]):
            return 1
        else:
            return 100
    else: 
        return 100

def omega(matriz, seq1, seq2, i, j):
    """
    Sacado de "ALGORITMO REVISADO PARA LA EXTRACCIÓN AUTOMÁTICA DE AGRUPAMIENTOS SEMÁNTICOS' G. Castillo 2002
    Es el cálculo de la distancia de edición considerando las inversiones consecutivas y conjuntivas
    
    :param matriz: La matriz de distancia de edición que vamos a llenar
    :param seq1: La primera oracion que vamos a comparar
    :param seq2: La segunda oracion que vamos a comparar
    :param i: posición de la seq1
    :param j: posición de la seq2
    :returns: La distancia de edición de la seq1 a la posición i con la seq2 en la posición j
    """
    w_e = 1
    if palabras_equivalentes(seq1[i], seq2[j]):
        w_i = 0
    else: 
        w_i = 1

    if i>=3 and j >=3:
        int_cons = intercambio_consecutivo(seq1, seq2, i, j)
        int_conj = intercambio_conjuntivo(seq1, seq2, i, j)
        
        C_i_j = min(matriz[i][j+1]+w_e, matriz[i+1][j] + w_e, matriz[i][j] + w_i,
                matriz[i-1][j-1]+ int_cons, matriz[i-2][j-2] + int_conj)
        return C_i_j
    elif i>=2 and j>=2:
        int_cons = intercambio_consecutivo(seq1, seq2, i, j)
        
        C_i_j = min(matriz[i][j+1]+w_e, matriz[i+1][j] + w_e, matriz[i][j] + w_i,
                matriz[i-1][j-1]+ int_cons)
        return C_i_j
    else:
        C_i_j = min(matriz[i][j+1]+w_e, matriz[i+1][j] + w_e, matriz[i][j] + w_i)
        return C_i_j    

def levi (seq1, seq2):
    """
    Calcula la matriz de edición entre dos secuencias considerando el intercambio conjuntivo y consecutivo
    
    :param seq1: Es una lista de diccionarios que representa a la primera oración. Cada diccionario contiene el token, lemma y tag
    :param seq2: Es una lista de diccionarios que representa a la segunda oración. Cada diccionario contiene el token, lemma y tag
    :returns: La matriz de edición considerando el interccambio consecutivo y conjuntivo
    """
    n = len(seq1)
    m = len(seq2)
    matriz = np.zeros((n+1, m+1))
    
    for j in range(1, m+1):
        matriz [0, j] = matriz[0, j-1] + 1
    
    for i in range(1, n+1):
        matriz [i, 0] = matriz[i-1, 0] + 1
        
        for j in range(1, m+1):
            matriz[i][j] = omega(matriz, seq1, seq2, i-1, j-1)
            
    return matriz

def POSpalabras_equivalentes(palabra1, palabra2):
    """
    Funcion booleana que ve si dos palabras son equivalentes, es decir si tienen el mismo token o lema, o si tienen el mismo etiquetado POS 
    """
    if unidecode.unidecode(palabra1['lemma'].lower()) == unidecode.unidecode(palabra2['lemma'].lower()):
        return True
    elif unidecode.unidecode(palabra1['token'].lower()) == unidecode.unidecode(palabra2['token'].lower()):
        return True
    elif palabra1['tag'] == palabra2['tag']:
        return True
    else:
        return False

    

def POSlevi (seq1, seq2):
    """
    Cálculo de la matriz de edición entre dos oraciones, considerando el etiquetado POS de las oraciones en lugar de las palabras
    
    :param seq1: Es una lista de diccionarios que representa a la primera oración. Cada diccionario contiene el token, lemma y tag. Utilizamos el lemma
    :param seq2: Es una lista de diccionarios que representa a la segunda oración. Cada diccionario contiene el token, lemma y tag. Utilizamos el lemma
    :returns: La matriz de edición considerando el etiqeutado POS en lugar de las palabras    
    """
    n = len(seq1)
    m = len(seq2)
    matriz = np.zeros((n+1, m+1))
    for i in range(n+1):
        matriz [i, 0] = i
    for j in range(m+1):
        matriz [0, j] = j
    for i in range(1, n+1):
        for j in range(1, m+1):
            if POSpalabras_equivalentes(seq1[i-1], seq2[j-1]):
                matriz[i][j] = min(matriz[i-1][j]+1, matriz[i][j-1] + 1, matriz[i-1][j-1])
            else:
                matriz[i][j] = min(matriz[i-1][j] + 1, matriz[i][j-1] + 1, matriz[i-1][j-1]+1)
    return matriz