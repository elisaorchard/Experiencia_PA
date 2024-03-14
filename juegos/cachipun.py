def cachipun():
    """
    Esta función representa el juego de cachipun.
    Debes pedir al usuario que elija piedra, papel o tijera, y luego comparar su elección con la de la computadora.
    La computadora debe elegir una opción al azar.
    """
    print("¡Vamos a jugar cachipun!")
    usuario = input("Elige: piedra, papel o tijera: ")

    from random import randint

    n = randint(1,3)

    if n == 1:
        computador = "piedra"
    elif n == 2:
        computador = "papel"
    elif n == 3:
        computador = "tijera"
    
    if computador == "piedra" and usuario == "papel":
        print("El computador sacó piedra. Le ganaste al computador!")
    elif computador == "piedra" and usuario == "tijera":
        print("El computador sacó piedra. Te ganó un computador!")
    elif computador == usuario:
        print("Hubo un empate!")
    elif computador == "papel" and usuario == "tijera":
        print("El computador sacó papel. Le ganaste al computador!")
    elif computador == "papel" and usuario == "piedra":
        print("El computador sacó papel. Te ganó un computador!")
    elif computador == "tijera" and usuario == "piedra":
        print("El computador sacó tijera. Le ganaste al computador!")
    elif computador == "tijera" and usuario == "papel":
        print("El computador sacó tijera. Te ganó un computador!")

