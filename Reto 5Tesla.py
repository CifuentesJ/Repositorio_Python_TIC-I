import csv, json, math

def lectura():
    with open("Reto 5Tesla.csv","r") as archivo:
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
            ope.append(float(i[1]))
            high.append(float(i[2]))
            low.append(float(i[3]))
            close.append(float(i[4]))
            adj.append(float(i[5]))
            vol.append(int(i[6]))

    return date, ope, high, low, close, adj, vol


def analisis(date,ope,close,adj):
    listaInforme=[]
    concep=[]
    for i in range(len(date)):
        concepto=float(close[i])-float(ope[i])
        if concepto>0:
            compor="SUBE"
        elif concepto<0:
            compor="BAJA"
        elif concepto==0:
            compor="ESTABLE"
        
        op=math.sqrt(math.pow((float(close[i])-float(adj[i])),2))
        listaInforme.append([date[i],compor,op])
    
    return listaInforme


def crearCsv(informe):
    with open("analisis_archivoTesla.csv","w") as archivo:
        escribir=csv.writer(archivo, delimiter="\t")
        escribir.writerow(["Fecha","Comportamiento de la accion","Ajuste Cuadratico de Close"])
        escribir.writerows(informe)


def informe2(date,vol,ope,clos,high,low):
    lowOpe=min(ope)
    dateLow=date[ope.index(min(ope))]
    highClos=max(clos)
    dateHigh=date[clos.index(max(clos))]
    acum=0
    listaDif=[]
    for i in range(len(date)):
        dif=0
        acum+=vol[i]
        dif=abs(float(low[i])-float(high[i]))
        listaDif.append(dif)
    mean=acum/float(len(vol))
    highDif=max(listaDif)
    dateDif=date[listaDif.index(max(listaDif))]

    dicc={}
    dicc["date_lowest_open"]=dateLow
    dicc["lowest_open"]=lowOpe
    dicc["date_highest_close"]=dateHigh
    dicc["highest_close"]=highClos
    dicc["mean_volume"]=mean
    dicc["date_greatest_difference"]=dateDif
    dicc["greatest_difference"]=highDif

    return dicc


def creaJson(dict):
    datosJson=json.dumps(dict,indent=4)
    with open("detallesTesla.json","w") as archivo:
        archivo.write(datosJson)


d,o,h,l,c,a,v=lectura()
info=analisis(d,o,c,a)
crearCsv(info)
diccio=informe2(d,v,o,c,h,l)
creaJson(diccio)