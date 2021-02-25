import pares 
import procesarTexto



def main():
    Libro1, Libro2, path = procesarTexto.biblias_procesadas()
    pares.pares_completos(Libro1, Libro2, path)
    
main()
