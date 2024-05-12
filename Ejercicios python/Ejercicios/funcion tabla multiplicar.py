#Funcion tabla de multiplicar

numero1=int(input("Indique la tabla que quiere visionar: "))

def tabla(numero1):
    for i in range(0,11):
        print(numero1,"x",i,"=",numero1*i)
    
tabla(numero1)

numero1=int(input("Indique la tabla que quiere visionar: "))
for a in range(numero1,11):
    tabla(numero1)

    numero1=numero1+1
    

