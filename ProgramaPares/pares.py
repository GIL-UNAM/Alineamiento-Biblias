import WagFish
import lcc
import tabulate as tb

def mostrar_alineacion(alineacion, f):
    """
    Esta función  realiza el txt que contiene a todas las alineaciones entre dos verículos que hay en todo ese libro de
    la Biblia.

    :param alineacion: una alineación obtenida mediante el algoritmo de Wagner Fischer
    :param f: es el escritor para escribir en el archivo txt
    """
    lista_para_mostrar = []
    palabra1 = []
    tag1 = []
    palabra2 = []
    tag2 = []
    for i in alineacion[0]:
        try:
            palabra1.append(i['token'])
        except:
            palabra1.append(i)
    for i in alineacion[0]:
        try:
            tag1.append(i['lemma'])
        except:
            tag1.append(i)
    for i in alineacion[1]:
        try:
            palabra2.append(i['token'])
        except:
            palabra2.append(i)
    for i in alineacion[1]:
        try:
            tag2.append(i['lemma'])
        except:
            tag2.append(i)

    lista_para_mostrar.append(palabra1)
    lista_para_mostrar.append(tag1)
    lista_para_mostrar.append(palabra2)
    lista_para_mostrar.append(tag2)
    lista_para_mostrar.append(alineacion[2])
    lista_para_mostrar.append(lcc.calcular_lcc_completo(alineacion[2]))
    f.write(tb.tabulate(lista_para_mostrar, stralign="right", tablefmt="orgtbl") + '\n\n\n')
    
def candidatos_a_pares(Versiculo1, Versiculo2, g):
    """
    Realiza el algoritmo de Wagner Fisher a dos versículos, hace la función mostrar_alineacion a una copia de la alineación
    para no modificarla. Calcula el lcc de dicha alineacion. Regresa a la alineacion en donde el ultimo elemento es el lcc

    :param Versiculo1: EL primer versículo a alinear. Una lista de json
    :param Versiculo2: EL segundo versículo a alinear. Una lista de json
    :param g: el escritor para la función mostrar_alineaciones
    :returns: Las alineacion derivada del algoritmo de Wagner Fisher junto al lcc 
    """
    alineacion = WagFish.WagnerFisher(Versiculo1, Versiculo2)
    dummy = alineacion.copy()
    mostrar_alineacion(dummy, g)
    alineacion.append(lcc.calcular_lcc_completo(alineacion[2]))

    
    return alineacion

def candidatos_inversion(Versiculo1, Versiculo2, g):
    """
    Realiza el algoritmo de Wagner Fisher considerando las inversiones a dos versículos, hace la función mostrar_alineacion a una copia de la alineación
    para no modificarla. Calcula el lcc de dicha alineacion. Regresa a la alineacion en donde el ultimo elemento es el lcc
    
    :param Versiculo1: EL primer versículo a alinear. Una lista de json
    :param Versiculo2: EL segundo versículo a alinear. Una lista de json
    :param g: el escritor para la función mostrar_alineaciones
    :returns: Las alineacion derivada del algoritmo de Wagner Fisher considerando la inversión junto al lcc 
    """
    rutas_multiples = WagFish.WagFishConj(Versiculo1, Versiculo2)
    numero_de_rutas = len(rutas_multiples)
    
    if numero_de_rutas > 0:
        print("==================================================")
        print("Versículo original 1:")
        print( el['token'] + " " for el in Versiculo1)
        print("Versículo original 2:")
        print( el['token'] + " " for el in Versiculo1)
        print("==================================================")
        print('\n')

    dummy = rutas_multiples.copy()
    for i in range(numero_de_rutas):
        mostrar_alineacion(dummy[i], g)
        rutas_multiples[i].append(lcc.calcular_lcc_completo(rutas_multiples[i][2]))

    return rutas_multiples

def candidatos_seminull(Versiculo1, Versiculo2, g):
    """
    Realiza el algoritmo de Wagner Fisher considerando a los pares semi iguales y semi nulos de dos versículos, hace la función mostrar_alineacion a una copia de la alineación
    para no modificarla. Calcula el lcc de dicha alineacion. Regresa a la alineacion en donde el ultimo elemento es el lcc

    :param Versiculo1: EL primer versículo a alinear. Una lista de json
    :param Versiculo2: EL segundo versículo a alinear. Una lista de json
    :param g: el escritor para la función mostrar_alineaciones
    :returns: Las alineacion derivada del algoritmo de Wagner Fisher considerando pares semi nulos y pares semi iguales junto al lcc 
    """

    alineacion = WagFish.semi(WagFish.WagnerFisher(Versiculo1, Versiculo2))
    dummy = alineacion.copy()
    mostrar_alineacion(dummy, g)
    alineacion.append(lcc.calcular_lcc_completo(alineacion[2]))
    
    return alineacion

def candidatos_POS(Versiculo1, Versiculo2, g):
    """
    Realiza el algoritmo de Wagner Fisher considerando la etiqueta POS de dos versículos, hace la función mostrar_alineacion a una copia de la alineación
    para no modificarla. Calcula el lcc de dicha alineacion. Regresa a la alineacion en donde el ultimo elemento es el lcc

    :param Versiculo1: EL primer versículo a alinear. Una lista de json
    :param Versiculo2: EL segundo versículo a alinear. Una lista de json
    :param g: el escritor para la función mostrar_alineaciones
    :returns: Las alineacion derivada del algoritmo de Wagner Fisher considerando POS junto al lcc 
    """

    alineacion = WagFish.POSWagnerFisher(Versiculo1, Versiculo2)
    dummy = alineacion.copy()
    mostrar_alineacion(dummy, g)
    alineacion.append(lcc.calcular_lcc_completo(alineacion[2]))
    
    return alineacion

def candidatos_POSsemi(Versiculo1, Versiculo2, g):
    """
    Realiza el algoritmo de Wagner Fisher considerando las etiquetas POS y pares semi nulos e iguales a dos versículos, hace la función mostrar_alineacion a una copia de la alineación
    para no modificarla. Calcula el lcc de dicha alineacion. Regresa a la alineacion en donde el ultimo elemento es el lcc
    :param Versiculo1: EL primer versículo a alinear. Una lista de json
    :param Versiculo2: EL segundo versículo a alinear. Una lista de json
    :param g: el escritor para la función mostrar_alineaciones
    :returns: Las alineacion derivada del algoritmo de Wagner Fisher considerando POS y pares semi nulos e iguales junto al lcc
    """

    alineacion = WagFish.semi(WagFish.POSWagnerFisher(Versiculo1, Versiculo2))
    dummy = alineacion.copy()
    mostrar_alineacion(dummy, g)
    alineacion.append(lcc.calcular_lcc_completo(alineacion[2]))
    
    return alineacion

    
def son_pares_sem(alineaciones, f, conLemma):
    """
    Función que calcula a las alineaciones cuyo lcc es mayor a 4, despues verifica que esas dos palabras sean pares lexicos cuyo etiquetado POS indique que no son palabras funcionales. A los pares lexicos que superen el filtro se les escribe en un txt para validar los resultados.

    :param alineaciones: Una alineacion obtenida mediante el algoritmo de WagnerFisher que ademas tiene calculado el lcc
    :param f: el escritor para hacer el txt
    """
    for i in range(len(alineaciones[3])):
        lcc = alineaciones[3][i]
        if lcc >= 4:
            if nos_interesa(alineaciones[0][i],alineaciones[1][i]):
               if conLemma == 1:
                   a = str(alineaciones[0][i]['token']) + ' / ' + str(alineaciones[0][i]['lemma'])+ ' - '+ str(alineaciones[1][i]['token']) + ' / ' + str(alineaciones[1][i]['lemma']) + ' -- ' +str(lcc)+ ' ' + str(alineaciones[0][0]['token'])+ '\n'
               else : 
                   a = str(alineaciones[0][i]['token']) + ' - '+ str(alineaciones[1][i]['token']) + ' -- ' +str(lcc)+ ' ' + str(alineaciones[0][0]['token'])+ '\n'
               f.write(a)


def nos_interesa(palabra1, palabra2):
    """
    Función booleana que nos dice si dos palabras que cumplen con el criterio de lcc nos interesan, eso quiere decir que nos dice si es un Verbo, un adjetivo, un Sustantivo o un adveribio, ya que dos palabras funcionales que son pares lexicos no nos interesan
    """
    try:
        if str(palabra1['tag'][0]) in ['V', 'N', 'A', 'R']:
            if str(palabra2['tag'][0]) in ['V', 'N', 'A', 'R']:
                return True
            else:
                return False
        else:
            return False
    except:
        return False 

def pares_completos(Libro1, Libro2, path, conLemma):
    """
    Función que nos sirve para automatizar la obtencion de resultados utilizando los diferentes metodos para obtener las alineaciones, escribiendo dos archivos txt, uno con las alineaciones y otro con los pares, conteniendo todos los resultados correspondientes a dos traducciones del mismo libro.

    :param Libro1: una lista de listas, donde cada lista contiene un versículo procesado mediante freeling, por lo que cada versiculo es una lista de json.Obtenido mediante la funcion procesar texto
    :param Libro2: una lista de listas, donde cada lista contiene un versículo procesado mediante freeling, por lo que cada versiculo es una lista de json. Obtenido mediante la funcion procesar texto
    :param path: es lo que nos ayuda con el título de los resultados
    """
    g = open('./Resultados/Alineaciones/Normal/alineaciones-' + path+ '.txt', 'w',encoding='utf-8')
    f = open('./Resultados/Pares/Normal/'+path+'.txt', 'w',encoding='utf-8')
    
    l = open('./Resultados/Alineaciones/Intercambio/alineaciones-Intercambio' + path+ '.txt', 'w',encoding='utf-8')
    h = open('./Resultados/Pares/Intercambio/Intercambio_'+ path +'.txt', 'w',encoding='utf-8')

    r = open('./Resultados/Alineaciones/Semi/alineacionesSeminiull-'+ path + '.txt', 'w',encoding='utf-8')    
    m = open('./Resultados/Pares/Semi/Seminull-'+path+'.txt', 'w',encoding='utf-8')
    
    b = open('./Resultados/Alineaciones/POS/POS'+path+'.txt', 'w',encoding='utf-8')
    a = open('./Resultados/Pares/POS/POS'+path+'.txt', 'w',encoding='utf-8')
    
    c = open('./Resultados/Alineaciones/POSsemi/POSsemi'+path+'.txt', 'w',encoding='utf-8')
    d = open('./Resultados/Pares/POSsemi/POSsemi'+path+'.txt', 'w',encoding='utf-8')
    
    j = len(Libro1)
    if j != len(Libro2):
        print('Las biblias seleccionadas no están alineadas.')
        exit(1) 
    for i in range(j):
        print(f'alineando {i+1}/{j}')
        
        alineacion_versiculo_i = candidatos_a_pares(Libro1[i], Libro2[i], g)
        son_pares_sem(alineacion_versiculo_i,f, conLemma)
        
        alineaciones_inversion_i = candidatos_inversion(Libro1[i], Libro2[i], l)
        for alineacion in alineaciones_inversion_i:
            son_pares_sem(alineacion, h, conLemma)
        
        alineacion_seminull_i = candidatos_seminull(Libro1[i], Libro2[i], r)
        son_pares_sem(alineacion_seminull_i, m, conLemma)
        
        alineacion_pos_i = candidatos_POS(Libro1[i], Libro2[i], b)
        son_pares_sem(alineacion_pos_i, a, conLemma)
        
        alineacion_POSsemi_i = candidatos_POSsemi(Libro1[i], Libro2[i], c)
        son_pares_sem(alineacion_POSsemi_i, d, conLemma)
    
    f.close()
    g.close()
    h.close()
    l.close()
    m.close()
    a.close()
    b.close()
    c.close()
    d.close()
