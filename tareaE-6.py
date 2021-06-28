

def salario(Ns):
    saI= int(input("ingrese salario I : "))
    if saI<= 600:
        Ns = saI + saI*0.1
    else:
        Ns = saI
    print("su salario es de:{}".format(Ns))
salario(0)
# Inicio 
# read(SI)30
# if SI<=600 then:
#     Ns = sI + SI*0.1
#     else:
#         Ns = Si
#     End_if
#     print(Ns)
# End