def separar(n: int): #Se define la función para separar
    lista4= list(str(n)) #Al número ingresado el string separa cada digito y lo ingresa en la lista
    for i in lista4:  #Se toma cada número de la lista
        print(i) #Se imprime cada número de la lista
        
if __name__=="__main__":
    n = int(input("Ingrese un número: ")) #Se pregunta el número que quiere ingresar
    sepa = separar(n) #Se llama la función
    print(sepa) #Se imprime