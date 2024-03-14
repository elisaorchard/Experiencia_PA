import random
def adivinar_numero():
    """
    Esta función representa el juego de adivinar un número.
    Debes generar un número al azar entre 1 y 10, y luego pedir al usuario que adivine el número.
    Se debe mostrar un mensaje si el usuario adivina correctamente o no.
    """
    # Ema está haciendo este
    print('Bienvenido al juego "Adivina un número"')
    n = random.randint(1,10)
    x = int(input('Elige un número del 1 al 10: '))
    while x != n:
        print('Lamentablemente no adivinaste el número, inténtalo de nuevo')
        x = int(input('Elige un número del 1 al 10: '))

    print('¡Adivinaste el número!')

