#Función que implementa el algoritmo de Euclides extendido
def euclides_ext (a,b):
    #Caso base
    if b == 0:
        return (a, 1, 0)  # mcd=a, x=1, y=0
    #Paso recursivo del algoritmo de Euclides
    mcd, x1, y1 = euclides_ext(b, a % b)
    # Actualización de los coeficientes de Bezout
    x = y1
    y = x1 - (a // b) * y1
    return (mcd, x, y)

def calcular_n(p,q):
  return p*q

def calcular_phi(p,q):
  return(p-1)*(q-1)

def calcular_d(e,phi):
    mcd, x, y = euclides_ext(e, phi)
    #Verificación de que e sea válido
    if mcd != 1:
        raise ValueError(f"e={e} no es válido, gcd(e, phi)={mcd} no es igual a 1")
    return x % phi

def cifrado (M,e,n):
  return (M**e) % n

def descifrado (C,d,n):
  return (C**d) % n

