def solucion(b,n):

    cont=0
    ad= int(input ("Ingrese un número:"))

    while n!=ad:
        if ad>b or ad<0: #El número ingresado es - 0 y más que el máximo
            print("¡Te saliste del intervalo!")
        elif ad<n: #Número ingresado menos que el adivinar
            print("¡Ups! Estás por debajo")
            cont+=1
        elif ad>n:#Número ingresado más que el adivinar
            print("¡Ups! Te pasaste")
            cont+=1
        
        ad=int(input("Ingrese un número:"))

    if n==ad: #Número ingresado es igual al adivinado
        cont+=1

    print(f"¡LO LOGRASTE! Usaste {cont} intentos")

print(solucion(b=100,n=92))
