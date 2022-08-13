#RECORRER CONJUNTOS
estudiantes={1:{"nombre":"Juan", "apellido":"Perez", "notas":[3.2,4,1.8,2]},
             2:{"nombre":"María", "apellido":"Mora", "notas":[3.5,0,2.8]},
             3:{"nombre":"Mateo", "apellido":"Segura", "notas":[4.8,5,3.1]}}

for i in estudiantes: #recorre claves iniciales 
    temp=estudiantes[i] #guarda el valor de cada clave
    for j in temp: #recorre "temp"
        if j=="notas": #cuándo llegue a notas haga:
            lista=temp[j] #lista=notas
            print(temp["nombre"], end=" ")
            prom=0
            for k in lista: #recorre las notas 
                prom+=k #suma de cada nota en un promedio
            prom/=len(lista) #hace el promedio de las 3 notas
            print(f"Las notas son: {prom}", end=" ")
            if prom>=3:
                print(", aprobaste")
            else:
                print(", reprobaste")