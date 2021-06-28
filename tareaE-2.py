class Descuento:
    Tcompras = float(input("Ingrese el total de compras: "))

    Descuen = Tcompras*0.15
    Cpagar = Tcompras - Descuen

    print("la cantidad a pagar es de :$ {} ".format(Cpagar))
descuento=Descuento()


