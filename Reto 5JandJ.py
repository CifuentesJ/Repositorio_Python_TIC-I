import json
import csv


def lectura():
    with open("Reto 5JyJ.csv","r") as archivo:
        datos=csv.reader(archivo)
        encabezado=next(datos)
        date=[]
        ope=[]
        high=[]
        low=[]
        close=[]
        adj=[]
        vol=[]
        for i in datos:
            date.append(i[0])
            ope.append(i[1])
            high.append(i[2])
            low.append(i[3])
            close.append(i[4])
            adj.append(i[5])
            vol.append(int(i[6]))

    return date, ope, high, low, close, adj, vol


def analisis(date,ope,close):
    listaInforme=[]
    concep=[]
    for i in range(len(date)):
        concepto=float(close[i])-float(ope[i])
        concep.append(abs(concepto))
        if concepto>0:
            con="SUBE"
        elif concepto<0:
            con="BAJA"
        elif concepto==0:
            con="ESTABLE"
        
        listaInforme.append([date[i],con,abs(concepto)])
    
    return listaInforme, concep


def crearCsv(informe):
    with open("analisis_archivoJandJ.csv","w") as archivo:
        escribir=csv.writer(archivo, delimiter="\t")
        escribir.writerow(["Fecha analizada","Comportamiento de la accion","abs Diferencia Close-Open"])
        escribir.writerows(informe)


def informe2(date,vol,dif):
    lowVol=min(vol)
    dateLow=date[vol.index(min(vol))]
    highVol=max(vol)
    dateHigh=date[vol.index(max(vol))]
    absMax=max(dif)
    dateAbs=date[dif.index(max(dif))]
    acum=0
    for i in range(len(date)):
        acum+=vol[i]
    mean=acum/float(len(vol))
    
    dicc={}
    dicc["date_lowest_volume"]=dateLow
    dicc["lowest_volume"]=lowVol
    dicc["date_highest_volume"]=dateHigh
    dicc["highest_volume"]=highVol
    dicc["mean_volume"]=mean
    dicc["date_greatest_difference"]=dateAbs
    dicc["greatest_difference"]=absMax

    return dicc


def creaJson(dict):
    datosJson=json.dumps(dict,indent=4)
    with open("detallesJandJ.json","w") as archivo:
        archivo.write(datosJson)


d,o,h,l,c,a,v=lectura()
info,conc=analisis(d,o,c)
crearCsv(info)
diccio=informe2(d,v,conc)
creaJson(diccio)