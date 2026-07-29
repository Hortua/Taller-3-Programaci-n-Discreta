from itertools import product

def a_binario(minterm, n_vars):
    #Se convierte un minitérmino entero a su representación binaria rellena
    return format(minterm, f"0{n_vars}b")


def difieren_en_un_bit(t1, t2):
    #Se identifica si dos términos difieren exactamente en una posición de bit
    if len(t1) != len(t2):
        return False, None
    diferencias = []
    for i, (c1, c2) in enumerate(zip(t1, t2)):
        if c1 == "-" or c2 == "-":
            if c1 != c2:
                return False, None  # los guiones deben coincidir en posicion
            continue
        if c1 != c2:
            diferencias.append(i)
    if len(diferencias) == 1:
        return True, diferencias[0]
    return False, None


def combinar(t1, t2, idx):
    #Se combina dos terminos que difieren en la posicion idx poniendo un guion ahi.
    return t1[:idx] + "-" + t1[idx + 1:]



def simplificar_minterminos(minterminos, n_vars):
    #Algoritmo de Quine-McCluskey para agrupar términos sistemáticamente
    terminos_actuales = [a_binario(m, n_vars) for m in minterminos]
    implicantes_primos = set()

    while True:
        usados = set()
        nuevos = set()

        for i in range(len(terminos_actuales)):
            for j in range(i + 1, len(terminos_actuales)):
                t1, t2 = terminos_actuales[i], terminos_actuales[j]
                ok, idx = difieren_en_un_bit(t1, t2)
                if ok:
                    nuevos.add(combinar(t1, t2, idx))
                    usados.add(t1)
                    usados.add(t2)

        # los terminos que no se combinaron con nadie en esta ronda
        # son implicantes primos definitivos
        for t in terminos_actuales:
            if t not in usados:
                implicantes_primos.add(t)

        if not nuevos:
            break
        terminos_actuales = list(nuevos)

    return sorted(implicantes_primos)



def termino_a_texto(termino, nombres_vars):
    #Se convierte un término binario con guiones a literales de álgebra booleana
    partes = []
    for bit, var in zip(termino, nombres_vars):
        if bit == "1":
            partes.append(var)
        elif bit == "0":
            partes.append(f"(not {var})")
        # si es '-', la variable no aparece
    return " and ".join(partes) if partes else "1"


def expresion_simplificada_texto(implicantes_primos, nombres_vars):
    # Une los implicantes primos mediante conectores OR (Suma de Productos)
    terminos_texto = [termino_a_texto(t, nombres_vars) for t in implicantes_primos]
    return " or ".join(f"({t})" for t in terminos_texto)



def evaluar_por_minterminos(minterminos, n_vars, valores):
    #Seevalua la funcion original: 1 si la combinacion de entrada es un mintermino.
    indice = int("".join(str(v) for v in valores), 2)
    return 1 if indice in minterminos else 0


def evaluar_implicantes(implicantes_primos, valores):
    #Se evalua la expresion simplificada OR de los implicantes primos.
    for termino in implicantes_primos:
        if all(bit == "-" or int(bit) == v for bit, v in zip(termino, valores)):
            return 1
    return 0


def verificar_equivalencia(minterminos, implicantes_primos, n_vars):
    #Se compara la tabla de verdad original vs la simplificada en las 2^n_vars filas.
    for valores in product([0, 1], repeat=n_vars):
        original = evaluar_por_minterminos(minterminos, n_vars, valores)
        simplificada = evaluar_implicantes(implicantes_primos, valores)
        if original != simplificada:
            return False
    return True




    
