frase = input("Por favor, ingresa una frase: ")

vocal = input("Ingresa una vocal para convertir a mayúscula: ")

if len(vocal) == 1 and vocal.islower() and vocal in 'aeiouAEIOU':
    frase_modificada = frase.replace(vocal, vocal.upper())
    
    print("Frase con la vocal en mayúscula:", frase_modificada)
else:
    print("La entrada no es una vocal en minúscula.")
