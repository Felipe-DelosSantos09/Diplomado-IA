num_secreto = 6
adivinado = False

while not adivinado:
    num_usuario = int(input("Ingrese un número entre el 1 y el 10: "))
    if num_usuario == num_secreto:
        print("Adivinaste el número")
        adivinado = True
    else:
        print("Intentalo otra vez")