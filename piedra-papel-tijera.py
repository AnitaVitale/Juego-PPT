nombre1 = input("Nombre jugador1: ") 
nombre2 = input("Nombre jugador2: ")

puntos_jugador1 = 0
puntos_jugador2 = 0

vueltas = 0

while vueltas < 3:
    jugador1 = input(f"¡Hola {nombre1}! ¿Qué eliges? ¿Piedra, papel o tijera?: ").lower()
    jugador2 = input(f"¡Hola {nombre2}! ¿Qué eliges? ¿Piedra, papel o tijera?: ").lower()

    condicion1 = jugador1 == "piedra" and jugador2 == "tijera"
    condicion2 = jugador1 == "papel" and jugador2 == "piedra"
    condicion3 = jugador1 == "tijera" and jugador2 == "papel"

    if jugador1 == jugador2:
        print("Empate entre ambos")
    elif condicion1 or condicion2 or condicion3:
        print(f"Gana {nombre1}")
        puntos_jugador1 += 1
    else:
        print(f"Gana {nombre2}")
        puntos_jugador2 += 1
    
    vueltas += 1

print("\nResultados finales:")
print(f"{nombre1}: {puntos_jugador1} puntos")
print(f"{nombre2}: {puntos_jugador2} puntos")

if puntos_jugador1 > puntos_jugador2:
    print(f"El ganador es {nombre1}!")
elif puntos_jugador2 > puntos_jugador1:
    print(f"El ganador es {nombre2}!")
else:
    print("¡Es un empate!")






