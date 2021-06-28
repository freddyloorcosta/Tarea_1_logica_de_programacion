#8-Leer tres números enteros diferentes entre sí y determinar el número mayor de los tres.


def numero_mayor(nmayor=0):
    n1,n2,n3=0,0,0
    n1 = input("Ingrese un primer numero: ")
    n2 = input("Ingrese un segundo numero: ")
    n3 = input("Ingrese un tercer numero: ")
    if (n1>n2) and (n1>n3):
        nmayor=n1
    else:
        if (n2>n3):
            nmayor = n2
        else:
            nmayor = n3
    print("el numero mayor es:{} ".format(nmayor))
numero_mayor()
