numero_telefono = input("Por favor, ingresa un número de teléfono en formato +34-XXXXXXXXX-XX: ")

partes = numero_telefono.split('-')

if len(partes) != 3 or partes[0] != '+34' or len(partes[1]) != 9 or len(partes[2]) != 2:
    print("El formato del número de teléfono no es válido.")
else:
    numero_sin_prefijo_y_extension = partes[1]
    print("Número de teléfono sin prefijo y extensión:", numero_sin_prefijo_y_extension)
