import json
import csv

with open("Informe_1.json","r") as archivo:
    cosa=json.load(archivo)


with open("Reto 5JyJ.csv","r") as archivo:
    datos=csv.DictReader(archivo)
    #encabezado=next(datos)
    listaDatos=[]
    for i in datos:
        listaDatos.append(i)
    print(listaDatos[80])