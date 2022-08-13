import numpy as np
import random

def encriptado(texto):
    listaInicial=list(texto)

    while True:                             #AÑADE ELEMENTOS FALTANTES
        raiz1=np.sqrt(len(listaInicial))
        raiz2=int(raiz1)
        dif=raiz1-raiz2
        if dif == 0.0:
            break
        listaInicial.append("_")


    dicc={}
    clave1=[]
    for i in range(0,len(listaInicial)):    #HACE UN DICCIONARIO PARA LAS CLAVES
        dicc[i]=listaInicial[i]
        clave1.append(i)                    #CREA LA LISTA DE CLAVES


    clave=np.random.permutation(clave1)     #DESORDENA LAS CLAVES


    listaDesorden=[]
    for i in clave:                         #DESORDENA LAS LETRAS SEGÚN LAS CLAVES DEL DICCIONARIO
        listaDesorden.append(dicc[i])


    unicode=[]                              #CREA EL UNICODE PARA CADA LETRA
    for i in range(0,len(listaDesorden)):
        unicode.append(ord(listaDesorden[i]))


    arreglo=np.array(unicode)


    array_final=arreglo.reshape(int(raiz1),int(raiz2))   

    return array_final, clave

def desencriptado(array_encriptado, clave):
    
    fila, columna=array_encriptado.shape    #TOMA LOS VALORES DE FILA Y COLUMNA
    listaDesord=[]      
    for i in range(fila):                   #RECORRE F Y C DE MATRIZ
        for k in range(columna):            #AGREGA A LA LISTA CADA LETRA CONVERTIDA DE ASCII
            listaDesord.append(chr(array_encriptado[i,k]))


    clave2=list(clave)
    dicci={}
    for i in range(0, len(clave2)):         #AGREGA AL DICCIONARIO CADA VALOR DE CADA POSICIÓN DE LA
        dicci[clave2[i]]=listaDesord[i]     #LISTA CLAVE EL VALOR EN POSIC DE LA LISTA DESORDENADA


    listaOrdenada=[]
    for i in range(0,len(clave2)):          #OBTIENE ORDENADA CADA VALOR DEL DICCIONARIO POR
        listaOrdenada.append(dicci.get(i))  #PARTE DE LAS CLAVES CON EL FOR EN POSICIÓN ASCENDENTE

    
    while True:
        if "_" in listaOrdenada:            #SI ELEMENTO EXIST LO ELIMINA, SE HACE EL PROCESO HASTA 
            listaOrdenada.remove("_")       #QUE NO ENCUENTRE MÁS
        else:
            break

    texto="".join(listaOrdenada)


    return texto

encriptad,clav= encriptado("CUALQUIER COSA QUE YO DIGA ACÁ, VA A APARECER EN EL DESENCRIPTADO DE UNA MANERA MARAVILLOSA, ENTONCES ES ALGO GENIAL MANO, QUIERO QUE ESTA LÍNEA TENGA POR AHÍ 300 LÍNEA, DE LAS CUALES APAREZCA UNA MATRIZ GRANDÍSIMA.   ")
text=desencriptado(encriptad,clav)

print(encriptad)
print(clav)
print("---------------------------------------------------------------------------")
print(text)