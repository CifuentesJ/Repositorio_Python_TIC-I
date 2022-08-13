#Ejercicio condicional: Leer tres números e imprimir ascendente

num1=float(input("Ingrese el primer número: "))
num2=float(input("Ingrese el segundo número: "))
num3=float(input("Ingrese el tercer número: "))

if num1>num2 and num1>num3:
  numMay=num1
  if num2>num3:
    numMed=num2
    numMen=num3
  elif num3>num2:
    numMed=num3
    numMen=num2
  else: print("Hubo un error.")

elif num2>num1 and num2>num3:
  numMay=num2
  if num1>num3:
    numMed=num1
    numMen=num3
  elif num3>num1:
    numMed=num3
    numMen=num1
  else: print("Hubo un error.")

elif num3>num1 and num3>num2:
  numMay=num3
  if num2>num1:
    numMed=num2
    numMen=num1
  elif num1>num2:
    numMed=num1
    numMen=num2
  else: print("Hubo un error.")
  
else: print("Hubo un error.")

if num1==numMay or num2==numMay or num3==numMay:
  print("El número menor es: ", numMen)
  print("El número del medio es: ", numMed)
  print("El número mayor es: ", numMay)