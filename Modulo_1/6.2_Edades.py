edad = int(input("Introduzca su edad: "))
if edad < 13:
    print("Eres un niño")
elif edad < 18:
    print("Eres un adolescente")
elif edad < 65:
    print("Eres un adulto")
else:
    print("Eres un adulto mayor")