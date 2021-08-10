import pares 
import procesarTexto
from palabrasCompuestas import buildComposedWordsLenghtsDict


def main():
    print("Procesando texto")
    Libro1, Libro2, path, conLemma = procesarTexto.biblias_procesadas()
    
    print("Calculando diccionario de longitudes en palabras compuestas")
    buildComposedWordsLenghtsDict()
    
    print("Almacenando los pares")
    pares.pares_completos(Libro1, Libro2, path, conLemma)
    
main()
