opc=input("1.Suma\n2.Resta\n3.Salir\n>>>")

while opc!="3":
    if opc=="1":
        num1=int(input("Digite número 1: "))
        num2=int(input("Digite número 2: "))
        suma=num1+num2
        print(f"La suma es: {suma}")
    elif opc=="2":
        num1=int(input("Digite número 1: "))
        num2=int(input("Digite número 2: "))
        rest=num1-num2
        print(f"La resta es: {rest}")
    else:
        print("La opción no es válida.")
    
    opc=input("1.Suma\n2.Resta\n3.Salir\n>>>")

print("Se terminó el programa.")
