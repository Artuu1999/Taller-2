def buscar_vocales(lista):
    # Inicializamos una lista vacía para almacenar las cadenas que cumplan con la condición.
    cadenas_encontradas = []

    for cadena in lista:
        contador = 0
        for letra in cadena:
            if letra in 'aeiouAEIOU':
                contador += 1
                if contador >= 2:
                    # Si la cadena cumple con la condición, la agregamos a la lista de cadenas encontradas.
                    cadenas_encontradas.append(cadena)
                    break

    if cadenas_encontradas:
        # Si la lista de cadenas encontradas no está vacía, imprimimos todas las cadenas.
        for cadena in cadenas_encontradas:
            print(cadena)
    else:
        # Si la lista de cadenas encontradas está vacía, imprimimos 'No existe'.
        print('No existe')

# Ejemplo de uso:
lista = ["hola", "halo", "estas", "amigo"]
buscar_vocales(lista)