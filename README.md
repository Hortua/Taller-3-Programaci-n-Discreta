\# Taller 3 - Programación discreta



\## Descripción



Este taller tiene como propósito aplicar conceptos fundamentales de Matemáticas Discretas a través de su implementación práctica en código. A lo largo de los ejercicios se abordan temas como criptografía clásica y moderna, teoría de grafos, álgebra de Boole, teoría de la información (entropía de Shannon) y una introducción a la computación cuántica, buscando conectar la teoría vista en clase con soluciones computacionales concretas.



\## Integrante: Julián Camilo Hortúa Franco



\## Lenguaje y ejecución



Los ejercicios fueron desarrollados en Python. No se utilizaron librerías externas con el fin de facilitar la ejecución del proyecto en cualquier computador sin necesidad de instalar paquetes adicionales.



\## Ejercicios desarrollados



\### Bloque A - Criptografía : 1. Cifrado César, 2. RSA de juguete, 3. MPC básico

\### Bloque B - Grafos : 4. Algoritmo de Dijkstra, 5. Cierre de estación, 6. Coloreo de grafos

\### Bloque D - Boole, Shannon y Cuántica : 7. Tablas de verdad, 8. Simplificación booleana, 9. Entropía de Shannon, 10. Simulador de un qubit



\## Estructura del proyecto



En la carpeta docs/ se encuentra el documento en formato pdf donde se explica para cada punto la idea matemática que se usa para resolverlo y una explicación corta de la forma en que se diseñó el programa que lo resuelve.

En la carpeta src/ se encuentra el código fuente con la resolución de cada uno de los ejercicios.

Para verificar el correcto funcionamiento de las soluciones, se deben ejecutar los archivos correspondientes ubicados en la carpeta tests/, cada uno asociado al ejercicio que valida.

Ubicado desde la raíz del proyecto, se pueden ejecutar los siguientes comandos para verificar las pruebas:



python -m tests.test\_cesar

python -m tests.test\_rsa

python -m tests.test\_mpc

python -m tests.test\_dijkstra

python -m tests.test\_cierre\_estacion

python -m tests.test\_coloreo

python -m tests.test\_tablas\_verdad

python -m tests.test\_simplificacion

python -m tests.test\_shannon

python -m tests.test\_qubit

