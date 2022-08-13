#Se nos da un archivo con unos productos, de los cuales se tienen que hacer 2 informes
#Cada informe tiene que ser en JSON y en CSV

import csv
import json

def abrirArchivo():
    with open("EjemploProducts.csv", "r") as archivo:
        datos=csv.reader(archivo)
        encabezado=next(datos)

        referencias=[]
        nombre=[]
        valor=[]
        categoria=[]
        for fila in datos:
            referencias.append(fila[0])
            nombre.append(fila[1])
            valor.append(fila[2])
            categoria.append(fila[3])

    return encabezado,referencias,nombre,valor,categoria


def informe1(categoria,valor):
    conjunto=set(categoria)
    lista_categoria=list(conjunto)
    lista_categoria.sort()

    lista_json=[]
    informe1=[]
    for i in lista_categoria:
        dicc={}
        total=0
        cont=0
        for j in range(0, len(categoria)):
            if i==categoria[j]:
                total+=float(valor[j])
                cont+=1
        informe1.append([i,total,cont])
        dicc["CATEGORIA"]=i
        dicc["SUMATORIA"]=total
        dicc["CANTIDAD"]=cont
        lista_json.append(dicc)

    return informe1,lista_json


def crearCsv(listaInforme):
    with open("Informe2.csv","w") as archivo:
        escribir=csv.writer(archivo, delimiter=',')
        escribir.writerow(["REFERENCIA","NOMBRE","PRECIO","IVA","TOTAL","CATEGORIA"])
        escribir.writerows(listaInforme)


def crearJson(listaJson):
    datosJson=json.dumps(listaJson, indent=4)
    with open("Informe_2.json", "w") as archivo:
        archivo.write(datosJson)


def informe2(r,n,v,c):
    iva=0.19
    listaIva=[]
    listaTot=[]
    listaFinal=[]
    listaDicc=[]
    for i in range(len(r)):
        dicc={}
        ivaProd=float(v[i])*iva
        listaIva.append(ivaProd)
        listaTot.append(float(v[i])+ivaProd)
        listaFinal.append([r[i],n[i],v[i],listaIva[i],listaTot[i],c[i]])
        dicc["REFERENCIA"]=r[i]
        dicc["NOMBRE"]=n[i]
        dicc["PRECIO"]=float(v[i])
        dicc["IVA"]=listaIva[i]
        dicc["TOTAL"]=listaTot[i]
        dicc["CATEGORIA"]=c[i]
        listaDicc.append(dicc)

    
    return listaFinal, listaDicc


def solucion():
    e, r, n, v, c=abrirArchivo()
    #l1, l2=informe1(c,v)
    #crearCsv(l1)
    #crearJson(l2)
    lcsv,ljson= informe2(r,n,v,c)
    crearCsv(lcsv)
    crearJson(ljson)

solucion()

    