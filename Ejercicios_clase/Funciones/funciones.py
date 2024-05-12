#funciones
numero1  = int(input("Indique el primer sumando: "))
numero2  = int(input("Indique el segundo sumando: "))

def suma():    
    resultado=numero1 + numero2
    print(resultado)
    
def resta():
    resultado=numero1 - numero2
    print(resultado)

suma()
resta()

a  = int(input("Indique el primer multiplicando: "))
b  = int(input("Indique el segundo mulitplicando: "))

def multiplicacion(a,b):
    c=a*b
    return c

resultado=multiplicacion(a,b)
print(resultado)


print("FIN")
