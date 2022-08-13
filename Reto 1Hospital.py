def solucion(edad,peso):
    edad=int(input("Ingrese la edad del paciente:"))
    peso=float(input("Indicar el peso del paciente en kilogramos:"))
    dias=0

    if edad>=5 and edad<=10: #Entre 5 y 10 años
        if peso<16: #desnutrición
            estado='A'
            while peso<22:
                peso+=0.1019
                dias+=1
        elif peso>28: #sobrepeso
            estado='B'
            while peso>24:
                peso-=0.03104
                dias+=1
        else: #saludable
            estado='C'
            while peso<28:
                peso+=0.0026
                dias+=1

    elif edad>10 and edad<=13: #Entre 10 y 13 años
        if peso<30: #desnutrición
            estado='A'
            while peso<32:
                peso+=0.1019
                dias+=1
        elif peso>50: #sobrepeso
            estado='B'
            while peso>43:
                peso-=0.03104
                dias+=1
        else: #saludable
            estado='C'
            while peso<50:
                peso+=0.0026
                dias+=1

    elif edad>13 and edad<=17: #Entre 13 y 17 años
        if peso<51: #desnutrición
            estado='A'
            while peso<56:
                peso+=0.1019
                dias+=1
        elif peso>63: #sobrepeso
            estado='B'
            while peso>58:
                peso-=0.03104
                dias+=1
        else: #saludable
            estado='C'
            while peso<63:
                peso+=0.0026
                dias+=1

    if estado=="A" or estado=="B":
        print(f"El estado nutricional del paciente es {estado} y se requieren {dias} días de dieta para que alcance un peso saludable")
    else:
        print(f"El estado nutricional del paciente es {estado} y se requieren {dias} días de dieta para que alcance el peso máximo")

print(solucion(edad=0,peso=0))