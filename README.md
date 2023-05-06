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
def separarEnteros(x): #Definimos la función que vamos a utilizar para este punto
    entero = int(x) #Señalamos únicamente la parte entera del número mediante el uso de int
    decimal = abs(x - entero) #Para la parte decimal señalamos el valor absoluto de la resta del número flotante y su parte entera
    digitosEnteros = [] #Creamos una lista vacia en la que se agregaran los dígitos enteros
    digitosDecimales = [] #Creamos otra lista vacia en la cual se agregaran los digitos decimales
    
    while entero > 0: #Mediante un ciclo while se ejecutara la función mientras el valor entero sea mayor a 0, es decir positivo
        digito = entero % 10 #El residuo del cociente de la parte entera y diez será el primer dígito después de la coma decimal
        digitosEnteros.insert(0, digito) #Se inserta dicho dígito en la primera posición de la lista de digitos enteros
        entero //= 10 #Se actualiza la variable entero dividiendola entre 10 y tomando solo la parte entera
     
    for i in range(8): #Ahora bien mediante un ciclo for se establecen cuantos decimales tendrán la lista
        decimal *= 10 #Los dígitos decimales se van obteniendo uno por uno al multiplicarlos por 10
        digito = int(decimal) #Se toma como entero la parte decimal
        digitosDecimales.append(digito) #Se agregan los digitos de la parte decimal a la lista
        decimal -= digito # Se actualiza el ciclo para que se siga ejecutando hasta que se cumpla el rango del ciclo
        
    return digitosEnteros, digitosDecimales #Se retornan las variables trabajadas anteriorment

if __name__ == "__main__": #Se hace uso de la función main para llamar las funciones definidad
    x = float(input("Ingrese el número decimal: ")) #Se solicita al usuario el ingreso del número real
    digitosEnteros, digitosDecimales = separarEnteros(x) #Se llama la función
    print("Parte entera: ", digitosEnteros) #Se imprime la lista de los dígitos enteros
    print("Parte decimal: ", digitosDecimales) #Se imprime la lista de dígitos decimales
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
import math #Importar la función matemática predeterminada de Python

#Definimos la función para hallar los números factoriales
def factorial(n):
    fact = 1 # Se inicializa el ciclo
    for i in range(1, n+1): # Se determina el rango
        fact *= i #Se actualiza el ciclo
    return fact

# Definimos la función aproximacionCoseno para poder aproximar el coseno mediante el uso de la serie de Taylor de un número x utilizando n términos
def aproximacionCoseno(x, n):
    cosenoAprox = 0 # Se inicializa
    for i in range(0, n+1): #Declaramos el ciclo for y su rango
        termino = ((-1)**i) * (x**(2*i) / factorial(2*i)) #Colocamos el valor de la expresión
        cosenoAprox += termino #Actualizar la función
    return cosenoAprox

# Se calcula el coseno real de x
def cosenoreal(x):
    coseno = math.cos(x) #Se trae la función coseno del modulo math
    return coseno

# Definimos una función para reconocer el error
def calcularn(x, margenError):
    n = 0 #Se inicializa la variable
    coseno_real = cosenoreal(x)
    aprox = aproximacionCoseno(x, n)
    error = abs(aprox - coseno_real)
    while error > margenError: #Se declara el ciclo while
        n += 1 #Se actualizan las variables
        aprox = aproximacionCoseno(x, n)
        error = abs(aprox - coseno_real)
    return n

#Definir una función para reconocer la cantidad de n para cada margen de error
def margenError(x):
    margenes = [0.1, 1, 10, 1000] #Poner en una lista la cantidad de margenes de errores
    for margen in margenes: #Ciclo for para recorrer uno por uno
        n = calcularn(x, margen/100) #Se calcula
        print("Con un margen de error del "+str(margen)+"%, se necesitan "+str(n)+" valores de la serie.")
        
# Se llaman las funciones, se solicita el ingreso de las variables y se imprimen los resultados       
if __name__ == "__main__":
    x = float(input("Ingrese un valor para hallar su coseno: "))
    n = int(input("Ingrese la cantidad de veces que quiere que se repita la serie: "))
    coseno_real = cosenoreal(x)
    aprox = aproximacionCoseno(x, n)
    error = abs(aprox - coseno_real)
    unidades = calcularn(x, 0.001)
    print("El valor aproximado usando la serie de Taylor es de:", aprox)
    print("Valor real usando la función math:", round(coseno_real, 3))
    print("La diferencia entre el valor real y el aproximado es de:", error)
    print("La cantidad de 'n' necesarios para un margen de error menor al 0.001% es de:", unidades)
    margenError(x)
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
#Se define la función para saber si hay elementos repetidos o no
def repeticiones (lista:list):
    repetido = False 
    for i in range(n): #Mediante un ciclo for se recorren los elementos de la lista
        for j in range(i+1, n):  #Determina los elementos según su índice
            if lista[i] == lista[j]: #Compara si ambos elementos son iguales
                repetido = True
                break  #Rompe el ciclo

# Se llaman las funciones, se solicita el ingreso de las variables y se imprimen los resultados       
if __name__ == "__main__":
    lista = [] #Se crea una lista vacia
    n = int(input("Ingrese la cantidad de elementos de la lista: "))
    for i in range(n): #Ciclo for para recorrer dicha lista
        elemento = int(input("Ingrese un número para la lista: ")) 
        lista.append(elemento) #Se agrega elemento por elemento a la lista
    print("la lista ingresada anteriormente es:", lista)
    if repetido: #Se condiciona
        print("La lista contiene elementos repetidos.")
    else:
        print("La lista no contiene elementos repetidos.")
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
