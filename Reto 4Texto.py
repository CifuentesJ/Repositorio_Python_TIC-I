import reto_4textos 
lista=reto_4textos.lista3()


def limpieza(lista):
    caracteres='-¿?.,;¡!:"_–'
    listaNueva=[]
    for i in lista:
        i=i.lower()
        for k in range(len(caracteres)):
            i=i.replace(caracteres[k],"")
        listaNueva.append(i)
    return listaNueva


def repetidas(listaNueva):    
    cantidades={}
    conjuCont=set()
    lista1=[]
    for i in listaNueva:
        cont=0
        cont=listaNueva.count(i)
        if i =="primo":
            cont-=1
        conjuCont.add(cont)
        reps=list(conjuCont)
        reps.sort(reverse=True)
        cantidades[i]=cont
    for i in cantidades:
        lista1.append([i,cantidades[i]])
    return reps, lista1


def palbras20(veces,lista1):
    listaListas=[]
    for i in veces:
        for k in lista1:
                if i==k[1]:
                    listaListas.append(k)
    listaFinal=[]
    for i in range(20):
        listaFinal.append(listaListas[i])

    return listaFinal

ln=limpieza(lista)
r,l=repetidas(ln)
f=palbras20(r,l)
print(f)
