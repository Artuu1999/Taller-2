# Taller #2

**Equipo:  "Los comillas"**

[![image.png](https://i.postimg.cc/Y2m7j7Vr/image.png)](https://postimg.cc/t7ywmKpw)
- Juan Camilo Morales Hernandez
- Arturo Moreno Covaría

Espero que se encuentren excelente estimados lectores, en el presente repo desarrollaremos los puntos propuestos en el [taller número 2](https://github.com/fegonzalez7/pdc_unal_clase14), de nuestra clase de programación de computadores.

## - Punto 1:
Problema: Diseñar un código, el cual al ingresar un número entero n y separe todos los digitos que componen dicho número.
Código solución:
```sh

```

## - Punto 2:
Problema: Realizar un programa en Python, que al ingresar un número flotante, separe la parte entera y la decimal, e imprima ambas partes por separado.
Código solución:
```sh

```

## - Punto 3:
Problema: Desarrollar un código que al correr, solicite ingresar dos números enteros y determine si dichos números son espejos.
Código solución:
```sh

```

## - Punto 4:
Problema: Diseñar una función que permita calcular una aproximación de la función coseno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Taylor. Usando math para traer la función coseno y mostrando además, la diferencia entre el valor real y la aproximación, lo anterior con cuántos valores de la serie, se tienen errores del 10%, 1%, 0.1% y 0.001%.
Código solución:
```sh

```

## - Punto 5:
Problema: Crear un programa que calcule el mínimo común multiplo de dos números dados, resolver dicho problema desde la perpectiva iterativa como recursiva.
Código solución: 
```sh
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
```

## - Punto 6:
Problema: Diseñar un código que permita determinar si un elemento se repite o no, dentro de una lista
Código solución:
```sh

```

## - Punto 7:
Problema: Realizar un programa que determine si en una lista se encuentra una cadena de caracteres con dos o más vocales. Si la cadena existe debe imprimirla y si no existe debe imprimir 'No existe'.
Código solución:
```sh
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
```

## - Punto 8:
Problema: Desarrollar un programa, el cual al ser dadas dos listas, indique que elementos aparecen en la primero pero no en la segunda.
Código solución:
```sh

```

## - Punto 9:
Problema: Resolver el punto 7 del [taller número 1](https://github.com/fegonzalez7/pdc_unal_clase8) usando operaciones con vectores.
Código solución:
```sh
numeros = []
suma = 0
for i in range(5):
    numero = float(input("Ingrese un número real: "))
    numeros.append(numero)
    suma += numero
print("los numeros ingresados son", numeros )

# Calcular el promedio
promedio = suma / len(numeros)
# Calcular el promedio
promedio = suma / len(numeros)

# Ordenar los números de forma ascendente y calcular la mediana
numeros_ascendentes = sorted(numeros)
mediana = numeros[2]

# Calcular el promedio multiplicativo
producto = 1
for numero in numeros:
    producto *= numero
promedio_multiplicativo = producto**(1/len(numeros))

# Ordenar la lista de números de forma ascendente y calcular la potencia del mayor número elevado al menor número
potencia = numeros[-1]**numeros[0]

# Ordenar la lista de números de forma descendente y calcular la raíz cúbica del menor número
numeros_descendentes = sorted(numeros, reverse=True)
raiz_cubica = numeros[0]**(1/3)

# Imprimir los resultados
print("El promedio es:", promedio)
print("La mediana es:", mediana)
print("El promedio multiplicativo es:", promedio_multiplicativo)
print("Los números ordenados de forma ascendente son:", numeros)
print("Los números ordenados de forma descendente son:", numeros_descendentes)
print("La potencia del mayor número elevado al menor número es:", potencia)
print("La raíz cúbica del menor número es:", raiz_cubica)
```

## - Punto 10:
Problema: Diseñar un algoritmo que determine si una matriz es mágica o no.
<table cellspacing="1" bgcolor="">
	<tr bgcolor="#252582">
		<th><b>Matriz Mágica</b></th>
	</tr>
	<tr bgcolor="#e4e4ed">
		<td style="color:#141414">Una matriz cuadrada es mágica si la suma de cada una de sus filas, de cada una de sus columnas y de cada diagonal es igual.<br>
	</tr>
</table>
Código solución:
```sh

```
