import random

def dividir_nota(x, M):
    #Se generan dos números aleatorios s1 y s2 entre 0 y M-1
    s1 = random.randint(0, M - 1)
    s2 = random.randint(0, M - 1)
    #Se calcula s3
    s3 = (x - s1 - s2) % M
    return (s1, s2, s3)

def repartir_notas(notas, M):
    servidor1 = []
    servidor2 = []
    servidor3 = []
    #Se divide cada nota y se reparten los pedazos en los servidores
    for nota in notas:
        s1, s2, s3 = dividir_nota(nota, M)
        servidor1.append(s1)
        servidor2.append(s2)
        servidor3.append(s3) 
    return servidor1, servidor2, servidor3

def calcular_suma(servidor1,servidor2,servidor3,M):
    #Se hace la suma conjunta de los tres servidores
  suma_s1=sum(servidor1)
  suma_s2=sum(servidor2)
  suma_s3=sum(servidor3)
  suma_total=(suma_s1+suma_s2+suma_s3) % M
  return suma_total

def calcular_promedio(suma_total,numero_notas):
  return suma_total/numero_notas


