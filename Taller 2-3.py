n = int(input("Ingrese un número de dos digitos: ")) #Ingresa el número de dos digitos
i = int(input("Ingrese un número de dos digitos: "))  #Ingresa el número de dos digitos  
lista1 = list(str(n)) #Se vuelven los dos digitos en dos números de una lista
lista2 = list(str(i)) #Se vuelven los dos digitos en dos números de una lista
if lista1[0] in lista2 and lista1[1] in lista2: #Sí el primer indice de la lista 1 esta en lista2 y sí el segundo numero de la lista 1 esta en lista2
    print(str(n)+" es espejo de "+str(i)) #Imprime que los números son espejos
else: #Sino 
    print("Los números ingresados no son espejos")#Imprime que los numeros no son espejos
