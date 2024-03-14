
"""n es la cantidad de numeros a memorizar"""
def memoria():
    import random
    import time
    print("Cuantos numeros desea memorizar, tendras 5 segundos para esto")
    list = []
    n = int(input())
    for i in range(n):
        list += [random.randint(0,9)]
    print(list)
    time.sleep(5)
    print("\n" * 40)
    print("Ingrese la secuencia de numeros separados por una coma")
    r = input()
    list2 = r.split(",")
    l2 = []
    for i in list2:
        i = int(i)
        l2 += [i]
    if list == l2:
        print("Felicidades!, memorizaste correctamente los numeros")
    else:
        print("Incorrecto! esos no eran los numeros")
    time.sleep(2)
    print('Secuencia original:', list)
    print('Tu respuesta:', l2)