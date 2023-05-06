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