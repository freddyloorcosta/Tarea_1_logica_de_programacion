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
