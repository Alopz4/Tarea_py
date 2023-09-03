fecha_nacimiento = input("Por favor, ingresa tu fecha de nacimiento en formato dd/mm/aaaa: ")

partes = fecha_nacimiento.split('/')

if len(partes) == 3 and partes[0].isdigit() and partes[1].isdigit() and partes[2].isdigit():
    dia = partes[0]
    mes = partes[1]
    año = partes[2]
    
    print(f"Día: {dia}")
    print(f"Mes: {mes}")
    print(f"Año: {año}")
else:
    print("El formato de la fecha no es válido.")
