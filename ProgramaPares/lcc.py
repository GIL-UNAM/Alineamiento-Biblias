def Condicion_de_frontera(tipo_par,i):
    """
    Es la condicion de frontera para considerar a un par correspondiente como meritorio de calcular su lcc
    
    :param tipo_par: Es la lista que contiene los tipos de pares en el alineamiento, puede ser Correspondiente, Nulo o Igual
    :param i: Indica una posición
    """
    if (tipo_par[i-1] == 'I') and (tipo_par[i+1] == 'I'):
        return True
    else:
        return False


def calcular_lcc_pos_i(tipo_par, i):
    """
    Calcula el lcc del par correspondiente a la posición i
    
    :param tipo_par: Es la lista que contiene los tipos de pares en el alineamiento, puede ser Correspondiente, Nulo o Igual
    :param i: Indica una posición
    """
    lcc = 0
    if tipo_par[i] != 'C':
        return int(0)
    if Condicion_de_frontera(tipo_par, i):
        n = 0
        lcc += 1
        while (n+i < len(tipo_par)-1) and tipo_par[i+n+1] == 'I':
            lcc += 1
            n += 1
        n = i
        while n >= 1 and tipo_par[n-1] == 'I':
            n -= 1
            lcc += 1
        return lcc
    else:
        return 0

def lcc_ultimo(tipo_par):
    """
    Calcular el lcc del ultimo elemento, ya que no puede cumplir con la condición de frontera
    """
    lcc = 0
    if tipo_par[-1] != 'C':
        return int (0)
    else:
        lcc += 1
        n = 2
        while  n < len(tipo_par) and tipo_par[-n] == 'I':
            n += 1
            lcc += 1
        return lcc
    


def calcular_lcc_completo(tipo_par):
    """
    Calcula el lcc de cada elemento de las alineaciones
    """
    lista_de_lcc = []
    for i in range (1, len(tipo_par)-1):
        lista_de_lcc.append(calcular_lcc_pos_i(tipo_par, i))
    lista_de_lcc.insert(0, 0)
    a = lcc_ultimo(tipo_par)
    lista_de_lcc.append(a)
    return lista_de_lcc

def distancia_de_edicion(lista_de_pares):
    """
    Calcula la distancia de edicion en la alineación
    """
    a = 0
    lista_dde = []
    for i in lista_de_pares:
        if i == 'I':
            lista_dde.append(a)
        else:
            a += 1
            lista_dde.append(a)
    return lista_dde