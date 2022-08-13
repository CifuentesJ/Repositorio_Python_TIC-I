import csv, json, math

def lectura():
    with open("Reto 5Globant.csv","r") as archivo:
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


def analisis(date,ope,close,high,low):
    listaInforme=[]
    listaOpera=[]
    contSu=0
    contB=0
    contE=0
    for i in range(len(date)):
        opera=0
        concepto=float(close[i])-float(ope[i])
        if concepto>0:
            compor="SUBE"
            contSu+=1
        elif concepto<0:
            compor="BAJA"
            contB+=1
        elif concepto==0:
            compor="ESTABLE"
            contE+=1
        
        opera=(float(high[i])-float(low[i]))/2
        listaOpera.append(opera)
        listaInforme.append([date[i],compor,opera])
    
    return listaInforme,contB,contSu,contE


def crearCsv(informe):
    with open("analisis_archivoGlobant.csv","w") as archivo:
        escribir=csv.writer(archivo, delimiter="\t")
        escribir.writerow(["Fecha","Comportamiento de la accion","Punto medio HIGH-LOW"])
        escribir.writerows(informe)


def informe2(date,high,low,c1,c2,c3):
    lowPri=min(low)
    dateLow=date[low.index(min(low))]
    highPri=max(high)
    dateHigh=date[high.index(max(high))]
    

    dicc={}
    dicc["date_lowest_price"]=dateLow
    dicc["lowest_price"]=lowPri
    dicc["date_highest_price"]=dateHigh
    dicc["highest_price"]=highPri
    dicc["cantidad_veces_sube"]=c2
    dicc["cantidad_veces_baja"]=c1
    dicc["cantidad_veces_estable"]=c3

    return dicc


def creaJson(dict):
    datosJson=json.dumps(dict,indent=4)
    with open("detallesGlobant.json","w") as archivo:
        archivo.write(datosJson)



d,o,h,l,c,a,v=lectura()
info,c1,c2,c3=analisis(d,o,c,h,l)
crearCsv(info)
dicc=informe2(d,h,l,c1,c2,c3)
creaJson(dicc)