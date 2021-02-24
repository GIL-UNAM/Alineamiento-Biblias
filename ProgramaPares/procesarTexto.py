"""
Regresa cada versículo de la biblia como un json
"""
import requests
import sys

puntu = ['–','«','“','"',"'",',',';',':','.','¡','¿','!','?','(',')','/','-','_','[',']','{','}','”','—','»']

def preguntar_libro_y_trad():
    """
    Simplemente pregunta qué Libro y qué traducciones va a leer.
    Tienen que ser dos traducciones del mismo grupo, del txt 'resumen biblico orednado'
    
    :returns: Strings del libro, y las traducciones
    """
    Libro = input('¿Qué libro quieres utilizar?: ')
    Traduccion1 = input('Traducción 1: ')
    Traduccion2 = input('Traducción 2: ')
    return Libro, Traduccion1, Traduccion2

def leer_libros(Libro, traduccion1, traduccion2):
    """
    Lee los libros para que puedan ser procesados después
    
    :param Libro: Libro bíblico
    :param tradducion1: Primera traduccion
    :param traduccion2: Segunda traduccion
    :returns: Dos strings, cada una es el capitulo de la biblia de su traduccion
    :raises: Eleccion invalida si la direccion no es valida
    """
    try:
        f1 = open('./Biblias/'+traduccion1+'/'+Libro+'.txt', 'r')  
        f2 = open('./Biblias/'+traduccion2+'/'+Libro+'.txt', 'r')
        Libro1 = f1.read()
        Libro2 = f2.read()
        f1.close()
        f2.close()
        return Libro1, Libro2
    except:
        print('Tu elección es inválida')
        sys.exit(1)

def procesamiento_previo(Libro):
    """
    Algunas biblias tienen doble espaciado o problemas de ese estilo
    Saca una lista donde cada elemento es un versiculo
    
    :param Libro: Un string que contiene un libro de la Biblia
    :returns: Una lista donde cada elemento es un versiculo del Libro
    """
    Libro = Libro.split('\n')
    Libro_preprocesado = []
    for i in Libro:
        if i not in ['',' ']:
            Libro_preprocesado.append(i)
    return Libro_preprocesado

def procesamiento(Libro):
    """
    Funcion que contacta a freeling para procesar el texto con el servicio de el
    GIL
        
    :param Libro: Una lista donde cada elemento es un string que es un versiculo en la biblia
    :returns: Una lista donde cada elemento es versiculo en un json con tres categorias, token, lemma y tag
    """
    Libro = procesamiento_previo(Libro)
    versiculoLing = []
    for vers in Libro:
        files = {'file': bytearray(vers, "utf8")}
        params = {'outf': 'tagged', 'format': 'json'}
        url = "http://www.corpus.unam.mx/servicio-freeling/analyze.php"
        r = requests.post(url, files=files, params=params)
        obj = r.json()
        versiculo = []
        for oracion in obj:
            for palabra in oracion:
                if palabra['token'] not in puntu:
                    versiculo.append(palabra)
        versiculoLing.append(versiculo)
    return versiculoLing

def procesamiento_nlp(Libro1, Libro2):
    """
    Realiza la funcion procesamiento a dos Libros
    """
    Libro1P = procesamiento(Libro1)
    Libro2P = procesamiento(Libro2)
    return Libro1P, Libro2P

def biblias_procesadas():
    """
    Automatiza el procesamiento del texto
    
    :returns: Los libros como listas de json, donde cada elemento es un versiculo
    """
    Libro, Traduccion1, Traduccion2 = preguntar_libro_y_trad()
    path = str(Libro+ '-'+ Traduccion1+ '-' + Traduccion2)
    Libro1, Libro2 = leer_libros(Libro, Traduccion1, Traduccion2)
    Libro1, Libro2 = procesamiento_nlp(Libro1, Libro2)
    return Libro1, Libro2, path
