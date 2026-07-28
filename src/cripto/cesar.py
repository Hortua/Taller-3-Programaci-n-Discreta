mayusculas=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
minusculas=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def cifrar (mensaje,k):
    cifrado=""
    for l in mensaje:
        if l in mayusculas:
            posicion = mayusculas.index(l)
            desp = (posicion + k ) % 26
            cifrado += mayusculas[desp]
        elif l in minusculas:
            posicion=minusculas.index(l)
            desp = (posicion + k) %26
            cifrado += minusculas[desp]
        else:
            cifrado += l
    return cifrado

def descifrar (mensaje,k):
    descifrado=""
    for l in mensaje:
        if l in mayusculas:
            posicion = mayusculas.index(l)
            desp = (posicion - k ) % 26
            descifrado += mayusculas[desp]
        elif l in minusculas:
            posicion=minusculas.index(l)
            desp = (posicion - k) %26
            descifrado += minusculas[desp]
        else:
            descifrado += l
    return descifrado

def no_k (mensaje):
    for k in range (26):
        intento= descifrar (mensaje,k)
        print(f'k={k}, mensaje descifrado: {intento}')

mensaje= "HOLA UNAL"
cifrado= cifrar(mensaje,3)
print(f'El mensaje original es: {mensaje}, con un k=3 el mensaje cifrado es: {cifrado}')
descifrado=descifrar(cifrado,3)
print(f'El mensaje cifrado es: {cifrado}, con un k=3 el mensaje descifrado es: {descifrado}')
mensaje1= "hola unal"
cifrado1= cifrar(mensaje1,3)
print(f'El mensaje original es: {mensaje1}, con un k=3 el mensaje cifrado es: {cifrado1}')
descifrado1=descifrar(cifrado1,3)
print(f'El mensaje cifrado es: {cifrado1}, con un k=3 el mensaje descifrado es: {descifrado1}')

mensaje1= "2;hola ,% unal5."
cifrado1= cifrar(mensaje1,3)
print(f'El mensaje original es: {mensaje1}, con un k=3 el mensaje cifrado es: {cifrado1}')
descifrado1=descifrar(cifrado1,3)
print(f'El mensaje cifrado es: {cifrado1}, con un k=3 el mensaje descifrado es: {descifrado1}')

no_k(cifrado)
