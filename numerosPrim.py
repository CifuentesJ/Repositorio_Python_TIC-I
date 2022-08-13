max=10000
for i in range(2,max+1):
    sw=True
    for j in range(2,i):
        if i%j==0:
            sw=False
            break
    if sw == True:
        print(i, end=" ")

       
        

    