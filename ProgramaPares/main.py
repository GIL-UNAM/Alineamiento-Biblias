import pares 
import procesarTexto



def main():
    print("Procesando texto")
    Libro1, Libro2, path, conLemma = procesarTexto.biblias_procesadas()
    print("Almacenando los pares")
    pares.pares_completos(Libro1, Libro2, path, conLemma)
    
main()
