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

def composedWordObject(token, lemma, tag):
    """
    Constructs a composed word object

    Parameters
    ----------
    token : String
        The word itself.
    lemma : String
        Word's lemma.
    tag : String
        Word's tag.

    Returns
    -------
    dict
        Constructed object with Freeling syntax using given parameters.
        The dictionary contains token, lemma and tag of the composed word.

    """
    return {"token": token, "lemma": lemma, "tag": tag}

'''
Autor: Abigail Ríos Guzmán

Diccionario de palabras compuestas

Se almacenan las posibles palabras compuestas así como su equivalencia en
objeto para no perder la notación usada por Freeling.

IMPORTANTE: Todos los valores deberán estar en minúsculas a excepción del tag.
'''
composedWordsDict = {
    'buena nueva': composedWordObject('buena nueva', 'nuevo', 'K'),
    'cristo jesús': composedWordObject('cristo jesús', 'jesucristo', 'K'),
    'jesús cristo': composedWordObject('jesús cristo', 'jesucristo', 'K'),
    'jesús mesías': composedWordObject("Jesús Mesías", "jesús mesías", "NCMS000"),
    'maestros de la ley': composedWordObject("Maestros de la ley", "maestro de la ley", "NCMS000"),
    'espíritu malo': composedWordObject("Espíritu Malo", "espíritu malo", "NCMS000"),
    'consagrado por dios': composedWordObject("Consagrado por Dios","consagrado por dios", "K"),
    'santo de dios': composedWordObject("Santo de Dios", "santo de dios", "NCMS000"),
    'jesús de nazaret': composedWordObject("Jesús de Nazaret", "jesús de nazaret", "NCMS000"),
    'jusús nazareno': composedWordObject("Jesús Nazareno", "jusús nazareno", "NCMS000"),
    'juan bautista': composedWordObject("Juan Bautista", "juan bautista", "RG"),
    'juan el bautista': composedWordObject("Juan el Bautista", "juan bautista", "RG"),
    'espíritu santo': composedWordObject("Espíritu Santo", "espíritu santo", "NCMS000"),
    'bueno noticia': composedWordObject("buena noticia", "bueno noticia", "NCFS000"),
    'reinado de dios': composedWordObject("reinado de Dios", "reinado de dios", "NCMS000"),
    'reino de dios': composedWordObject("Reino de Dios", "reino de dios", "NCMS000")
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