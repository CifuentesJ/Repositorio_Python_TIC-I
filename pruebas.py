##############################################
nombres=[]
tipos=[] 
edades=[]
pesos=[]
##############################################
x=0
y=0
#######################contadores y acumuladores###############
cont_edad_cf=0
cont_edad_be=0
suma1=0
suma2=0

##########################listas###############################
nombres=["Fini","Saori","Lincon","Gertru","Brise","Jerry"]
tipos=["Canino","Canino","Felino","Bovino","Equino","Roedor"]
edades=[10,1,9,15,15,1]
pesos=[8,6,10,100,98.5,0.20]
#######################diccionarios vacios####################
diccionario={}
beneficiarios_can_fel={}
beneficiarios_equ_bov={}

#######################diccionario Completos###################

for i in nombres:
    x=x+1
    diccionario.update({str(x):[nombres[y],tipos[y],edades[y],pesos[y]]})
    y=y+1
print(diccionario)
#print("Fin Diccionario 1")
x=0
y=0
z=0
######################beneficiarios Caninos y Felinos#################
for i in tipos:
    if (((tipos[y]=="Canino") or (tipos[y]=="Felino"))and(edades[z]>=9)):
        x=x+1
        beneficiarios_can_fel.update({str(x):[nombres[y],tipos[y],pesos[y]]})
        suma1=edades[y]+suma1
        cont_edad_cf=cont_edad_cf+1
    y=y+1            
    z=z+1
    

    
  
print(beneficiarios_can_fel)

#print("Fin Diccionario 2")
x=0
y=0
z=0
######################beneficiarios equinos y bobinos################
for i in tipos:
    if (((tipos[y]=="Bovino") or (tipos[y]=="Equino"))and(edades[z]>=16)):
        x=x+1
        beneficiarios_equ_bov.update({str(x):[nombres[y],tipos[y],pesos[y]]})
        suma2=edades[y]+suma2
        cont_edad_be=cont_edad_be+1
    y=y+1            
    z=z+1


print(beneficiarios_equ_bov)

#print("Fin Diccionario 3")

###########################promedios de edades#################
if (cont_edad_cf>0):
    promedio_can_fel=suma1/cont_edad_cf    
    print(promedio_can_fel)
else:
    print("none")

if (cont_edad_be>0):
    promedio_equ_bov=suma2/cont_edad_be
    print(promedio_equ_bov)
else:
    print("none")
    