#6.Dado el sueldo de un empleado, encontrar el nuevo sueldo si obtiene un aumento del 10% 
# si su sueldo es inferior a $600, en caso contrario no tendrá aumento.

def salario(Ns):
    saI= int(input("ingrese salario I : "))
    if saI<= 600:
        Ns = saI + saI*0.1
    else:
        Ns = saI
    print("su salario es de:{}".format(Ns))
salario(0)
