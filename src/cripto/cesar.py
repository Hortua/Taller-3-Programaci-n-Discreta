#Listas con las letras en mayúsculas y minúsculas que se usarán para hacer el corrimiento con el k
mayusculas=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
minusculas=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#Función para cifrar los mensajes con un k dado: #Recibe el mensaje y k
def cifrar (mensaje,k):
    cifrado=""
#Se itera el mensaje
    for l in mensaje:
        #Si el caracter está en una de las listas, usa su índice para realizar el corrimiento
        if l in mayusculas:
            posicion = mayusculas.index(l)
            desp = (posicion + k ) % 26
            cifrado += mayusculas[desp]
        elif l in minusculas:
            posicion=minusculas.index(l)
            desp = (posicion + k) %26
            cifrado += minusculas[desp]
        #De lo contrario, el caracter que da igual
        else:
            cifrado += l
    return cifrado

#Función para descifrar los mensajes, mismo funcionamiento que cifrar(), resta la k en lugar de sumar
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

#Función que prueba los 26 k posibles
def no_k (mensaje):
    for k in range (26):
        intento= descifrar (mensaje,k)
        print(f'k={k}, mensaje descifrado: {intento}')


