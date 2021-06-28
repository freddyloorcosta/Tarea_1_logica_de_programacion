#2.En una tienda se ofrece un descuento del 15% sobre el total de la compra y 
# un cliente desea saber cuánto deberá pagar finalmente por su compra.

class Descuento:
    Tcompras = float(input("Ingrese el total de compras: "))

    Descuen = Tcompras*0.15
    Cpagar = Tcompras - Descuen

    print("la cantidad a pagar es de :$ {} ".format(Cpagar))
descuento=Descuento()


