import random
import time
"""n es la cantidad de numeros a memorizar"""
def memoria(n):
    list = []
    n = int(n) 
    for i in range(n):
        list += [random.randint(0,9)]
    return [list]
print("Cuantos numeros desea memorizar")
n = input()
numeros = memoria(n)
numeros = numeros[0]
print(numeros)
time.sleep(5)
print("\n" * 40)
print("Ingrese la secuencia de numeros separados por una coma")
r = input()
list2 = r.split(",")
l2 = []
for i in list2:
    i = int(i)
    l2 += [i]
if numeros == l2:
    print("Felicidades!, memorizaste correctamente los numeros")
else:
    print("Incorrecto! esos no eran los numeros")
time.sleep(2)
print('Secuencia original:', numeros)
print('Tu respuesta:', l2)