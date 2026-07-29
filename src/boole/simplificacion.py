from itertools import product

def a_binario(minterm, n_vars):
    return format(minterm, f"0{n_vars}b")


def difieren_en_un_bit(t1, t2):
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
    """Combina dos terminos que difieren en la posicion idx, poniendo un guion ahi."""
    return t1[:idx] + "-" + t1[idx + 1:]



def simplificar_minterminos(minterminos, n_vars):
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
    partes = []
    for bit, var in zip(termino, nombres_vars):
        if bit == "1":
            partes.append(var)
        elif bit == "0":
            partes.append(f"(not {var})")
        # si es '-', la variable no aparece
    return " and ".join(partes) if partes else "1"


def expresion_simplificada_texto(implicantes_primos, nombres_vars):
    terminos_texto = [termino_a_texto(t, nombres_vars) for t in implicantes_primos]
    return " or ".join(f"({t})" for t in terminos_texto)



def evaluar_por_minterminos(minterminos, n_vars, valores):
    """Evalua la funcion original: 1 si la combinacion de entrada es un mintermino."""
    indice = int("".join(str(v) for v in valores), 2)
    return 1 if indice in minterminos else 0


def evaluar_implicantes(implicantes_primos, valores):
    """Evalua la expresion simplificada (OR de los implicantes primos)."""
    for termino in implicantes_primos:
        if all(bit == "-" or int(bit) == v for bit, v in zip(termino, valores)):
            return 1
    return 0


def verificar_equivalencia(minterminos, implicantes_primos, n_vars):
    """Compara la tabla de verdad original vs la simplificada en las 2^n_vars filas."""
    for valores in product([0, 1], repeat=n_vars):
        original = evaluar_por_minterminos(minterminos, n_vars, valores)
        simplificada = evaluar_implicantes(implicantes_primos, valores)
        if original != simplificada:
            return False
    return True



casos = [
        {"minterminos": [1, 3, 5, 7], "n_vars": 3, "nombres": ["A", "B", "C"]},
        {"minterminos": [0, 2, 4, 6, 8, 10, 12, 14], "n_vars": 4, "nombres": ["A", "B", "C", "D"]},
    ]

for caso in casos:
    minterminos = caso["minterminos"]
    n_vars = caso["n_vars"]
    nombres = caso["nombres"]

    implicantes = simplificar_minterminos(minterminos, n_vars)
    expresion = expresion_simplificada_texto(implicantes, nombres)
    es_equivalente = verificar_equivalencia(minterminos, implicantes, n_vars)

    print(f"\nMinterminos: {minterminos}  (variables: {nombres})")
    print("Salida de mi programa (implicantes primos, binario):", implicantes)
    print("Expresion simplificada:", expresion)
    print("Verificacion (misma tabla de verdad que el original):", es_equivalente)
    
