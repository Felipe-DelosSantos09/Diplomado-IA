L1 = float(input("Ingrese la medida del lado a: "))
L2 = float(input("Ingrese la medida del lado b: "))
L3 = float(input("Ingrese la medida del lado c: "))
if L1 == L2 == L3:
    print("Su triangulo es equilatero")
elif L1 == L2 or L2 == L3 or L1 == L3:
    print("Su triangulo es isoseles")
else:
    print("Su triangulo es escaleno")