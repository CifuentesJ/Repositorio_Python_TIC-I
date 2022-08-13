def modificar_materia(pensum, semestre, materia, nombre, creditos):
    semestre-=1
    ''''
    pensum=[
            {"0123":{"nombre":nombre, "creditos":creditos},
            "4567":{"nombre":"inglés", "creditos":1}},
            {}, {}
        ]
    '''

    if semestre==0 or semestre==1 or semestre==2: 
        if pensum[semestre] == {}:
            mensaje="El semestre no tiene materias"
        else:
            if materia == "0123":
                pensum[0]["0123"]["nombre"]=nombre
                pensum[0]["0123"]["créditos"]=creditos
                mensaje="Modificada con éxito"
            elif materia == "4567":
                pensum[0]["4567"]["nombre"]=nombre
                pensum[0]["4567"]["créditos"]=creditos
                mensaje="Modificada con éxito"
            elif materia != "0123" or materia != "4567":
                mensaje="La materia no existe"
            
    else:
        mensaje="Ingrese un semestre válido"
    
    semestre+=1
    print(semestre, materia, nombre)
    print(pensum, mensaje)
    return mensaje

print(modificar_materia(pensum="pensum", semestre=1, materia="4567", nombre="lectoescritura", creditos=3))

