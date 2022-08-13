'''
Elaborar un algoritmo que encuentre los N primeros términos de la
sucesión del FIBONACCI, donde el número N será ingresado por el
usuario. Recuerde que la serie del FIBONACCI empieza con los
números 0 y 1 y el tercer término se genera como la suma de los dos
anteriores así: 0 1 1 2 3 5 8 13 21... éste ejemplo muestra los 9 primeros
términos de la sucesión.
'''

n= int(input("Ingrese el número>> "))
fib=0
ult=1
penUlt=0

print("0 1", end=" ")
for i in range(0,n-2):    
    fib=ult+penUlt
    print(fib, end=" ")
    penUlt=ult
    ult=fib
    
