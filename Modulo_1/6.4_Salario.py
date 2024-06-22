salario = int(input("Ingrese su salario: "))
edad = float(input("Ingrese su edad: "))
if salario < 20000 and edad < 18:
    print("Estas exento de immpuestos")
elif salario < 20000 and edad >= 18:
    print("Pagas el 5 porciento de impuestos")
elif salario <= 50000:
    print("Pagas el 10 porciento de impuestos")
else:
    print("Pagas el 20 porciento de impuestos")