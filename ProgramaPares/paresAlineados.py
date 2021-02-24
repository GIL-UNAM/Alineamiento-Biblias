import pares
import procesarTexto
import sys

trad1 = input('Libro1 : ')
trad2 = input('Libro2 : ')
path = str(trad1[3:7]+'-'+ trad1+ '-' + trad2)

def leer_libros(Libro, traduccion1, traduccion2):
    """
    Lee los libros para que puedan ser procesados despuÃ©s
    
    :param Libro: Libro bÃ­blico
    :param tradducion1: Primera traduccion
    :param traduccion2: Segunda traduccion
    :returns: Dos strings, cada una es el capitulo de la biblia de su traduccion
    :raises: Eleccion invalida si la direccion no es valida
    """
    try:
        f1 = open('./Biblias/'+Libro+'/'+traduccion1+'.txt', 'r')  
        f2 = open('./Biblias/'+Libro+'/'+traduccion2+'.txt', 'r')
        Libro1 = f1.read()
        Libro2 = f2.read()
        f1.close()
        f2.close()
        return Libro1, Libro2
    except:
        print('Tu elecciÃ³n es invÃ¡lida')
        sys.exit(1)

Libro1, Libro2 = leer_libros('Alineadas', trad1, trad2)
Libro1, Libro2 = procesarTexto.procesamiento_nlp(Libro1, Libro2)

pares_lex = pares.pares_completos(Libro1, Libro2, path)