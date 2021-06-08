def validar_alineacion(tipos_pares):
    outerChars = ["I", "J", "G"]
    bridgeChars = { 'N': False, 'C': False}
    n = len(tipos_pares) # Longitud del arreglo
    lastChar = "" # Variable temporal del último caracter
    
    # Buscamos que se cumpla la condición O, ..., B, ..., O
    # O = Outer char
    # B = Bridge char
    while n:
        currentChar = tipos_pares[n-1]
        # Si se detecta un cambio tal que: ..., B, O, ....
        if(currentChar in bridgeChars and lastChar in outerChars):
            tempBridgeChars = bridgeChars.copy()
            
            # Retrocedemos mientas haya caracteres y sean el mismo que
            # encontramos en el cambio
            while n and tipos_pares[n-1] in bridgeChars:
                tempBridgeChars[tipos_pares[n-1]] = True
                n -= 1
            
            # Flag para identificar si se encontraron todas los bridge chars
            found = True
            
            # Verificamos si se encontraron todos los bridge chars
            for key, value in tempBridgeChars.items():
                found &= value
            
            # Verificamos si el nuevo cambio es del tipo: ..., O, B, ...
            # También se revisa si se encontraron todos 
            if tipos_pares[n-1] in outerChars and found:
                return True
        lastChar = currentChar
        n -= 1
    
    return False

def filtrar_alineaciones_sustantivos(rutas_multiples):
    min_perc = .2 # Porcentaje mínimo aceptable
    nRutas = len(rutas_multiples) # Número de rutas
    rutasAIgnorar = []
    
    for r in range(nRutas):
        porcentajes = {'s': 0, 'v': 0} # Porcentaje de la ruta
        nPares = len(rutas_multiples[r][0]) # Número de pares de la ruta
        # Lista que almacena el número de sustantivos y verbos
        totales = {'s': 0, 'v': 0}
        # Número de pares de sustantivos y verbos en la ruta
        paresRuta = {'s': 0, 'v': 0}
        
        seq1 = rutas_multiples[r][0]
        seq2 = rutas_multiples[r][1]
        
        # Contadores auxiliares {'s': sustantivos, 'v': verbos}
        cont1Aux = {'s': 0, 'v': 0} # Contadores de la sequencia 1
        cont2Aux = {'s': 0, 'v': 0} # Contadores de la sequencia 2
        
        for p in range(nPares):
            if seq1[p]['tag'][0] == 'N':
                cont1Aux['s'] += 1
            elif seq1[p]['tag'][0] == 'V':
                cont1Aux['v'] += 1
                
            if seq2[p]['tag'][0] == 'N':
                cont2Aux['s'] += 1
            elif seq2[p]['tag'][0] == 'V':
                cont2Aux['v'] += 1
            
            if seq1[p]['tag'][0] == seq2[p]['tag'][0]:
                if seq1[p]['tag'][0] == 'N':
                    paresRuta['s'] += 1
                elif seq1[p]['tag'][0] == 'V':
                    paresRuta['v'] += 1
        
        totales['s'] = cont1Aux['s'] if cont1Aux['s'] > cont2Aux['s'] else cont2Aux['s']
        totales['v'] = cont1Aux['v'] if cont1Aux['v'] > cont2Aux['v'] else cont2Aux['v']
        
        porcentajes['s'] = 0 if totales['s'] == 0 else paresRuta['s'] / totales['s']
        
        if porcentajes['s'] < min_perc or porcentajes['v'] < min_perc:
            rutasAIgnorar.append(r)
            
    # Invertimos los índices
    nRutasAIgnorar = len(rutasAIgnorar)
    rutasAIgnorar.reverse()
    
    # Removemos las rutas con un porcentaje bajo de sustantivos alineados
    for r in range(nRutasAIgnorar):
        rutas_multiples.pop(rutasAIgnorar[r])
        
    return