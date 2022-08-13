print("¡Bienvenido! En esta aplicación los estudiantes podrán gestionar las notas de su materia.")
nom=str(input("Por favor ingrese su nombre:"))
mat=str(input("Ingrese el nombre de la materia:"))
porAcu=0
notAcum=0

nota=float(input("Ingrese la nota obtenida:"))
porc=float(input("Ingrese el porcentaje de la nota:"))
porc/=100

nota*=porc
notAcum+=nota
porAcu+=porc

res=str(input("¿Falta añadir notas? S/N:"))

while res=='S':
    nota=float(input("Ingrese la nota obtenida:"))
    porc=float(input("Ingrese el porcentaje de la nota:"))
    porc/=100

    while porAcu+porc>1:
        print("El porcentaje evaluado de una materia no puede ser mayor a 100")
        nota=float(input("Ingrese la nota obtenida:"))
        porc=float(input("Ingrese el porcentaje de la nota:"))
        porc/=100

    nota*=porc
    notAcum+=nota
    porAcu+=porc    

    if porAcu<1:
        res=str(input("¿Falta añadir notas? S/N:"))
    else:
        res='N'
    
if notAcum>=3:
    resp="aprobado"
else:
    resp="reprobado"

print(f"El estudiante {nom.lower().capitalize()} cursó la materia {mat.lower().capitalize()} y obtuvo {round(notAcum,2)} resultando en {resp}")