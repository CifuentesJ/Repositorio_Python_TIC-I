from Reto_2N_list import lista 

estud=lista()


def calcular_promedio_y_cuadro_honor(grupo):
    sum=0
    lista=[]
    dicc1={}
    for i in range(0, len(grupo)):
        nota=grupo[i]["nota_fundamento"]
        sum+=nota
        lista.append(nota)
    prom=sum/len(grupo)

    lista2=set(lista)
    lista3=list(lista2)
    lista3.sort(reverse=True)
    listaP1=[]
    listaP2=[]
    listaP3=[]
    dicc1={1:[],2:[],3:[]}
    for i in range(0,len(grupo)):
        nota=grupo[i]["nota_fundamento"]
        if nota==lista3[0]:
            listaP1.append(grupo[i]["cédula"])
        if nota==lista3[1]:
            listaP2.append(grupo[i]["cédula"])
        if nota==lista3[2]:
            listaP3.append(grupo[i]["cédula"])
    
    dicc1[1]=listaP1
    dicc1[2]=listaP2
    dicc1[3]=listaP3
    
    
    return prom, dicc1

print(calcular_promedio_y_cuadro_honor(estud))