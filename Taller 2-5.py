# Definiremos la funcion MinimoComunMultiploiterativ
def MinimoComunMultiploiterativo(a, b):
    mcm = (a, b)
    # Inicializamos la variable mcm en 1 para luego ir multiplicándola por el valor de i.
    mcm = 1
    i = 1
    # El programa empieza con mcm 1  hasta encontrar el primer número que sea divisible por ambos números ingresados.
    while True:
        if ((mcm * i) % a == 0) and ((mcm * i) % b == 0):
            mcm = mcm * i
            break
        i += 1
    # Devolvemos el resultado del MinimoComunMultiploiterativo.
    return mcm

if __name__ == "__main__":
    # Pedimos al usuario que ingrese los dos números 
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))

    # Calculamos el mcm utilizando la función MinimoComunMultiploiterativo.
    mcm = MinimoComunMultiploiterativo(a, b)

    # Imprimimos el resultado del mcm.
    print("El minimo comun multiplo de", a, "y", b, "es:", mcm)