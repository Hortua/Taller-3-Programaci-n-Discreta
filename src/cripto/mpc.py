import random
def dividir_nota(x, M):
    s1 = random.randint(0, M - 1)
    s2 = random.randint(0, M - 1)
    s3 = (x - s1 - s2) % M
    return (s1, s2, s3)

def repartir_notas(notas, M):
    servidor1 = []
    servidor2 = []
    servidor3 = []   
    for nota in notas:
        s1, s2, s3 = dividir_nota(nota, M)
        servidor1.append(s1)
        servidor2.append(s2)
        servidor3.append(s3) 
    return servidor1, servidor2, servidor3

def calcular_suma(servidor1,servidor2,servidor3,M):
  suma_s1=sum(servidor1)
  suma_s2=sum(servidor2)
  suma_s3=sum(servidor3)
  suma_total=(suma_s1+suma_s2+suma_s3) % M
  return suma_total

def calcular_promedio(suma_total,numero_notas):
  return suma_total/numero_notas

notas=[40,35,50,25]
M=1000003
serv1,serv2,serv3=repartir_notas(notas,M)
suma=calcular_suma(serv1,serv2,serv3,M)
promedio=calcular_promedio(suma,len(notas))
print(f'Suma total= {suma}, Promedio= {promedio}')
