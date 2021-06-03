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
        porcentaje = 0 # Porcentaje de la ruta
        nPares = len(rutas_multiples[r][0]) # Número de pares de la ruta
        nSustantivos = 0 # Número de sustantivos máximo de la ruta
        nParesSustantivos = 0 # Número de pares de sustantivos de la ruta
        
        seq1 = rutas_multiples[r][0]
        seq2 = rutas_multiples[r][1]
        
        sust1Aux = 0
        sust2Aux = 0
        
        for p in range(nPares):
            if seq1[p]['tag'][0] == 'N':
                sust1Aux += 1
                
            if seq2[p]['tag'][0] == 'N':
                sust2Aux += 1
            
            if seq1[p]['tag'][0] == seq2[p]['tag'][0] and seq1[p]['tag'][0] == 'N':
                nParesSustantivos += 1
                
        nSustantivos = sust1Aux if sust1Aux > sust2Aux else sust2Aux
        
        porcentaje = 0 if nSustantivos == 0 else nParesSustantivos / nSustantivos
        
        if porcentaje < min_perc:
            rutasAIgnorar.append(r)
            
    # Invertimos los índices
    nRutasAIgnorar = len(rutasAIgnorar)
    rutasAIgnorar.reverse()
    
    # Removemos las rutas con un porcentaje bajo de sustantivos alineados
    for r in range(nRutasAIgnorar):
        rutas_multiples.pop(rutasAIgnorar[r])
        
    return