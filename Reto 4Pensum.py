pensum=[{"0123":{"nombre":"intro a la ing", "créditos":2},
        "4567":{"nombre":"inglés", "créditos":1}},
        {}, {}
        ]


def es_semestre_valido(p, s):
    if s>len(p) or s<1:
        val=False
    else: 
        val=True

    return val


def es_semestre_vacio(p, s):
    s-=1
    if p[s]=={}:
        val2=True
    else:
        val2=False
    
    return val2


def es_materia_valida(p, s, m):
    s-=1
    for i in range(0,len(p[s])):
        if m in p[s]:
            val3=True
        else:
            val3=False
    
    return val3


def modificar_materia(pensum, semestre, materia, nombre, creditos):
    if (es_semestre_valido(pensum,semestre) == True) and (es_semestre_vacio(pensum,semestre) == False) and (es_materia_valida(pensum,semestre,materia) == True):
        pensum[semestre-1][materia]["nombre"]=nombre
        pensum[semestre-1][materia]["créditos"]=creditos

    return pensum


def eliminar_materia(pensum, semestre, materia):
    if (es_semestre_valido(pensum,semestre) == True) and (es_semestre_vacio(pensum,semestre) == False) and (es_materia_valida(pensum,semestre,materia) == True):
        pensum[semestre-1].pop(materia)
    
    return pensum


print(f"PENSUM INICIAL\n{pensum}")
print("\n")
print("------------------------------------")
print("\n")
print(modificar_materia(pensum, 1, "0123","lectoescritura",3))
print("\n")
print("------------------------------------")
print("\n")
print(eliminar_materia(pensum, 1, "0123"))

