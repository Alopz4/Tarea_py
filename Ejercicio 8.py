precio_str = input("Por favor, ingresa el precio del producto en euros con dos decimales (por ejemplo, 12.34): ")

try:
    precio = float(precio_str)
except ValueError:
    print("El formato del precio no es válido.")
else:
    euros = int(precio)
    centavos = int((precio - euros) * 100)

    print(f"El precio ingresado es {euros} euros y {centavos} céntimos.")
