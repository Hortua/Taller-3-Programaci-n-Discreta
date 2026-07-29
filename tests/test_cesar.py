import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.cripto.cesar import cifrar, descifrar, no_k

print("==================================================")
print("             PRUEBAS: CIFRADO CÉSAR               ")
print("==================================================\n")

# Caso de prueba obligatorio del taller
mensaje = "HOLA UNAL"
cifrado = cifrar(mensaje, 3)
print(f'Caso 1 (Obligatorio):')
print(f'Original:  {mensaje}')
print(f'Cifrado:   {cifrado} (Esperado: KROD XQDO)')
print(f'Descifrado:{descifrar(cifrado, 3)}\n')

# Caso de prueba 2: Minúsculas
mensaje1 = "hola unal"
cifrado1 = cifrar(mensaje1, 3)
print(f'Caso 2 (Minúsculas):')
print(f'Original:  {mensaje1}')
print(f'Cifrado:   {cifrado1}')
print(f'Descifrado:{descifrar(cifrado1, 3)}\n')

# Caso de prueba 3: Caracteres especiales y números
mensaje2 = "2;hola ,% unal5."
cifrado2 = cifrar(mensaje2, 3)
print(f'Caso 3 (Especiales y límites):')
print(f'Original:  {mensaje2}')
print(f'Cifrado:   {cifrado2}')
print(f'Descifrado:{descifrar(cifrado2, 3)}\n')

# Caso donde no se conoce k
print("Caso 4 (Fuerza Bruta - Todos los K):")
no_k(cifrado)
