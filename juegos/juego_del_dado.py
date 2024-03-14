import time
def tiempo():
    for i in range(3):
        print(".",end="\n")
        time.sleep(0.3)

from random import randint
def juego_del_dado():
    print("Hola mundo!\nBienvenido al juego del dado, en este juego por turnos cada uno lanzará un dado e irá sumando el número a su puntaje. El primero en llegar a 30 puntos gana.")
    x=input("¿Deseas jugar? (sí/no):\n")
    while x!="no":
        if x!="sí" and x!="si":
            x=input("¿Deseas jugar? (sí/no):")
        else:
            puntuacion_jugador=0
            puntuacion_comp=0
            print("Tu partes")
            while puntuacion_jugador<30 and puntuacion_comp<30:
                input("Apreta enter para lanzar.")
                print("Y tú número es")
                tiempo()
                numero=randint(1,6)
                print(f"{numero}!")
                puntuacion_jugador+=numero
                print(f"Llevas {puntuacion_jugador} puntos.\n")
                if puntuacion_jugador>=30:
                    print("Felicidades! Has ganado")
                else:
                    input("Apreta enter si estás listo para mi lanzamiento")
                    print("Ahora voy yo. Mi número es")
                    tiempo()
                    numero=randint(1,6)
                    print(f"Mi número es {numero}!")
                    puntuacion_comp+=numero
                    print(f"Mi puntuación es de {puntuacion_comp}!\n")
            if puntuacion_comp>=30:
                print("Te gané! Buen intento.")
            x=input('¿Revancha? (sí/no)\n')
    print("Hasta luego!")
