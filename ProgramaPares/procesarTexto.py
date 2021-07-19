"""
Regresa cada versÃ­culo de la biblia como un json
"""
import requests
import sys

puntu = ['â','Â«','â','“','”',"'",',',';',':','.','Â¡','Â¿','!','?','(',')','/','-','_','[',']','{','}','â','â','Â»']
#puntu = ['–','«','“','"','"',"'",',',';',':','.','¡','¿','!','?','(',')','/','-','_','[',']','{','}','”','—','»']

def preguntar_libro_y_codigos():
    """
    Simplemente pregunta quÃ© Libro y quÃ© codigos va a leer.
    Tienen que ser dos traducciones del mismo grupo, del txt 'resumen biblico orednado' o dos biblias alineadas
    
    :returns: CLibro1 y CLibro2 son las carpetas donde se encuentran los archivos .txt
    codigo1 y codigo2 son dos identificadores, las pimeras tres letras indican la traduccion
    y la 4ta a 6ta letra indican que libro de la biblia es
    """
    a = input('¿Quiere procesar Biblias alineadas? 1/0 : ')
    if a == '1':
        CLibro1 = input('¿Qué libro?: ')
        CLibro1 = 'BibliasAlineadas/' + CLibro1
        CLibro2 = CLibro1
        codigo1 = input('Introduzca el código 1: ')
        codigo2 = input('Introduzca el código 2: ')
        conLemma = int(input('¿Desea que se presenten los lemas? 1/0 : '))
        return CLibro1, CLibro2, codigo1, codigo2, a, conLemma
    else:
        CLibro1 = input('¿Cuál es la primera traducción?: ')
        CLibro2 = input('¿Cuál es la segunda traducción?: ')
        codigo1 = input('Introduzca el código 1: ')
        codigo2 = input('Introduzca el código 2: ')
        conLemma = input('¿Desea que se presenten los lemas? 1/0 : ' )

        return CLibro1, CLibro2, codigo1, codigo2, a, conLemma
        
def leer_libros(CLibro1, CLibro2, codigo1, codigo2):
    """
    Lee los libros para que puedan ser procesados despuÃ©s
    
    :param CLibro1: Carpeta de la primera traduccion
    :param CLibro2: Carpeta de la segunda traduccion
    :param codigo1: Codigo de la primera traduccion
    :param codigo2: COdigo de la segunda traduccion
    :returns: Dos strings, cada una es el capitulo de la biblia de su traduccion
    :raises: Eleccion invalida si la direccion no es valida
    """
    try:
        print('./Biblias/'+CLibro1+'/'+codigo1+'.txt')
        print('./Biblias/'+CLibro2+'/'+codigo2+'.txt')
        f1 = open('./Biblias/'+CLibro1+'/'+codigo1+'.txt', 'r',encoding='utf-8')  
        f2 = open('./Biblias/'+CLibro2+'/'+codigo2+'.txt', 'r',encoding='utf-8')
        Libro1 = f1.read()
        Libro2 = f2.read()
        f1.close()
        f2.close()
        return Libro1, Libro2
    except:
        print('Su elección es inválida')
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
    k = 0
    j = len(Libro)
    for vers in Libro:
        k += 1
        print(f" >> {k}/{j} {vers[:10] }")
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
    print("Procesando libro 1")
    Libro1P = procesamiento(Libro1)
    print("Procesando libro 2")
    Libro2P = procesamiento(Libro2)
    return Libro1P, Libro2P

def biblias_procesadas():
    """
    Automatiza el procesamiento del texto
    
    :returns: Los libros como listas de json, donde cada elemento es un versiculo
    """
    CLibro1, CLibro2, codigo1, codigo2, a, conLemma = preguntar_libro_y_codigos()
    if a == '1':
        path = str('ALN' + codigo1[3:]+ '-'+ codigo1[:3]+ '-' + codigo2[:3])
    else:
        path = str(codigo1[3:]+ '-'+ codigo1[:3]+ '-' + codigo2[:3])
    Libro1, Libro2 = leer_libros(CLibro1, CLibro2, codigo1, codigo2)
    print("Libros leídos exitosamente")
    print("Comienza procesamiento NLP de los textos...")
    Libro1, Libro2 = procesamiento_nlp(Libro1, Libro2)
    print('Terminó el procesamiento NLP')
    return Libro1, Libro2, path, conLemma
