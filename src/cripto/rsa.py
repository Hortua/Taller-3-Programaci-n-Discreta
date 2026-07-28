def euclides_ext (a,b):
    if b == 0:
        return (a, 1, 0)  # mcd=a, x=1, y=0
    mcd, x1, y1 = euclides_ext(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return (mcd, x, y)

def calcular_n(p,q):
  return p*q

def calcular_phi(p,q):
  return(p-1)*(q-1)

def calcular_d(e,phi):
    mcd, x, y = euclides_ext(e, phi)
    if mcd != 1:
        raise ValueError(f"e={e} no es válido, gcd(e, phi)={mcd} no es igual a 1")
    return x % phi

def cifrado (M,e,n):
  return (M**e) % n

def descifrado (C,d,n):
  return (C**d) % n

p,q,e,M=61,53,17,65
n=calcular_n(p,q)
print(f'n= {n}')
phi=calcular_phi(p,q)
print(f'phi= {phi}')
d=calcular_d(e,phi)
print(f'd= {d}')
C=cifrado(M,e,n)
print(f'C= {C}')
M1=descifrado(C,d,n)
print(f'M= {M1}')
