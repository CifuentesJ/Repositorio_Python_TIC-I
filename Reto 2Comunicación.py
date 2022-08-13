from numpy import conj


def encriptador(men):
    alfab=['A','B','C','D','E','F','G','H','I','J', 'K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    #men=list(men)

    conju=set()
    for i in range(0, len(men)):        #Carácteres únicos
        conju.add(men[i])


    dicc1={}
    l=0
    for i in conju:                     #Creación del diccionario
        dicc1[i]=alfab[l]               #Recorre los Carac. Unicos y agrega según valor de alfabeto
        l+=1

    lista=[]                            #Obtiene valores del dicc y agrega a lista según orden 
    for i in men:
        lista.append(dicc1.get(i))    

    encrip="".join(lista)    
        
    
    return dicc1, encrip
    


def desencriptador(e,c):
    c={v: k for k,v in c.items()}       #Revierte clave-valor
        
    
    lista=[]
    for i in e:                         #Agrega a la lista según obtiene el valor de clave
       lista.append(c.get(i))           #de forma ordenada
    
    desenc="".join(lista)

    return desenc

x, t=encriptador("Mensaje a encriptar")
print(x)
print(t)

print(desencriptador(t,x))