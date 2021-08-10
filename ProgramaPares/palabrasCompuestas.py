from copy import deepcopy

'''
Autor: Abigail Ríos Guzmán
Construcción de tags para palabras compuestas

----------------------------------------------------------------------
POS        Atributo        Valor            Código
----------------------------------------------------------------------
1          Categoría       Determinante     K
----------------------------------------------------------------------
Añadir más atributos si son necesarios
'''


'''
Autor: Abigail Ríos Guzmán

Diccionario de palabras compuestas

Se almacenan las posibles palabras compuestas así como su equivalencia en
objeto para no perder la notación usada por Freeling.

IMPORTANTE: Todos los valores deberán estar en minúsculas a excepción del tag.
'''
composedWordsDict = {
    'buena nueva': {"token": 'buena nueva', 'lemma': 'nuevo', 'tag': 'K'},
    'cristo jesús': {"token": 'cristo jesús', 'lemma': 'jesucristo', 'tag': 'K'},
    'jesús cristo': {"token": 'jesús cristo', 'lemma': 'jesucristo', 'tag': 'K'}
}


'''
Autor: Abigail Ríos Guzmán

Diccionario de relación con palabras compuestas

Calculado por código
'''
composedWordsLengthsDict = { }


def buildComposedWordsLenghtsDict():
    
    # Add global variables
    # global composedWordsDict, composedWordsLengthsDict
    
    for key in composedWordsDict:
        words = key.split(" ") # List of words in the key
        
        fWord = words[0] # First word
        nWords = len(words)
        # Validate if there's a key in the composed words lenghts dict which
        # name is our first word
        if composedWordsLengthsDict.get(fWord) is not None:
            # Add the number of words to the current key if it doesn't exist
            if nWords not in composedWordsLengthsDict[fWord]:
                composedWordsLengthsDict[fWord].append(nWords)
        else:
            # Add the key and the number of words
            composedWordsLengthsDict[fWord] = [nWords]


'''
Autor: Abigail Ríos Guzmán

Función que concatena n posiciones dentro del versículo en una frasse y
regresa el string concatenado.
'''
def concatWordsInVersicle(versicle, start, positions):
    resultStr = ""
    for i in range(positions):
        resultStr = resultStr + versicle[start + i]['token'].lower() + " "
        
    return resultStr[:-1]

'''
Autor: Abigail Ríos Guzmán

Función que transforma las frases contenidas en un versículo en su equivalente
de palabras compuestas si es que existe dicha eqivalencia.
'''
def treatComposedWords(versicle):
    # Add global variables
    #global composedWordsDict, composedWordsLengthsDict

    nWords = len(versicle) # Words in versicle
    w = 0
    
    # Iterate over every word
    while w < nWords:
        
        currentWord = versicle[w]['token'].lower() # w-th word
        # Validate if we detect a possible composed word
        if composedWordsLengthsDict.get(currentWord) is not None:
            
            # Get posible composed words lengths
            compWordsLengthOptions = composedWordsLengthsDict[currentWord]
            
            # Verify every length option verify if our text exists as composed
            # word
            for length in compWordsLengthOptions:
                
                if nWords > (w + length):      
                    composedWord = concatWordsInVersicle(versicle, w, length)
                    
                    # Check if the composed word exists
                    if composedWordsDict.get(composedWord) is not None:
                        
                        # Removed equivalent words
                        for i in range(length):
                            versicle.pop(w)
                        
                        # Push composed word
                        versicle.insert(w, composedWordsDict[composedWord])
                        
                        # Recalculate versicle limits
                        nWords = len(versicle)
                        
        w += 1

    # Return the updated versicle
    return versicle