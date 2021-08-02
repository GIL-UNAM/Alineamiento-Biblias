'''
Por: Abigail Ríos Guzmán
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

Diccionario de relación con palabras compuestas

Si se detecta la primera palabra, se comparan las siguientes palabras del
versículo para ver si hay coincidencia con las palabras compuestas registradas.

NOTA: Es importante modificar en conjunto los diccionarios
detectComposedWordDict y composedWordsDict, ya que su funcionalidad está
relacionada.
'''
detectComposedWordDict = {
    'buena': ['buena nueva'],
    'cristo': ['cristo jesús'],
    'jesús': ['jesús cristo']
    }

'''
Autor: Abigail Ríos Guzmán

Diccionario de palabras compuestas

Se almacenan las posibles palabras compuestas así como su equivalencia en
objeto para no perder la notación usada por Freeling.

NOTA: Es importante modificar en conjunto los diccionarios
detectComposedWordDict y composedWordsDict, ya que su funcionalidad está
relacionada.
'''
composedWordsDict = {
    # Cristo Jesús
    'buena nueva': {"token": 'buena nueva', 'lemma': 'nuevo', 'tag': 'K'},
    'cristo jesús': {"token": 'cristo jesús', 'lemma': 'jesucristo', 'tag': 'K'},
    'jesús cristo': {"token": 'jesús cristo', 'lemma': 'jesucristo', 'tag': 'K'}
    }

