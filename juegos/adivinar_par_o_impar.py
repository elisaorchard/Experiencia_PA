import random
def adivinar_par_o_impar():
    respuesta='xd'
    print('Adivina si el numero es par o impar')
    numero = random.randint(1,100)
    if numero%2==0:
        respuesta='PAR'
    else:
        respuesta='IMPAR'
    print('Ingresa "PAR" O "IMPAR" segun cual crees que sera el numero')
    adivinanza=input()
    if adivinanza==respuesta:
        print('Felicitaciones! Adivinaste')
    else:
        print('No adivinaste, sigue jugando')

    """
    Esta función representa el juego de adivinar si un número es par o impar.
    Tienes que permitir que el usuario ingrese una de las dos opciones y
    generar un número aleatorio para ver si es par o impar.
    Se debe mostrar si el usuario adivina correctamente o no.
    """
    pass

