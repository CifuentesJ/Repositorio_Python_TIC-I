valUni=float(input("Ingrese el valor unitario:"))
iva=str(input("¿Elproducto cuenta con IVA?:"))
cant=int(input("Ingrese la cantidad que lleva el cliente del producto a registrar:"))
subTot=0

if iva=='S':
    valUni=((valUni*0.19)+valUni)*cant
    print("IVA incluído")
elif iva=='N':
    valUni=valUni*cant
    print("PRODUCTO SIN IVA")

subTot+=valUni
print(f"SUBTOTAL: {subTot}")

res=str(input("¿Faltan productos por cobrar? S/N:"))

while res=='S':
    valUni=float(input("Ingrese el valor unitario:"))
    iva=str(input("¿Elproducto cuenta con IVA?:"))
    cant=int(input("Ingrese la cantidad que lleva el cliente del producto a registrar:")) 
    if iva=='S':
        valUni=((valUni*0.19)+valUni)*cant
        print("IVA incluído")
    elif iva=='N':
        valUni=valUni*cant
        print("PRODUCTO SIN IVA")

    subTot+=valUni
    print(f"SUBTOTAL: {subTot}")

    res=str(input("¿Faltan productos por cobrar? S/N:"))

print(f"TOTAL A COBRAR: {subTot}")