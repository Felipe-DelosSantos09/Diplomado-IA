i = 1
while i <= 3:
    temp_inv = float(input("Dato de temperatura del primer invernadero: "))
    hr_inv = float(input("Dato de HR del primer invernadero: "))
    if temp_inv > 30 and hr_inv >= 30:
        print("Necesita ventilación")
    elif temp_inv > 30 and hr_inv < 30:
        print("Necesita riego y ventilación")
    elif temp_inv < 30 and hr_inv >= 30:
        print("Todo bien. No necesitas hacer nada")
    else:
        print("Necesita riego")
    i += 1




