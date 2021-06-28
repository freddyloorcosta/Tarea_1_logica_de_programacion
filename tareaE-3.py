#3.Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas. 
# El vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por 
# las tres ventas que realiza en el mes y el total que recibirá en el mes tomando 
# en cuenta su sueldo base y sus comisiones.

class totalventas:
    SalarioB = int(input("Ingrese salario base: "))
    v1 = int(input("Ingrese el valor de la primera venta: "))
    v2 = int(input("Ingrese el valor de la segunda venta: "))
    v3 = int(input("Ingrese el valor de la tercera venta: "))
    
    TotalV = v1+v2+v3
    c = TotalV * 0.1
    Total = SalarioB + c
    print("su total a recibir es de:{}".format(Total))
totalventas()
