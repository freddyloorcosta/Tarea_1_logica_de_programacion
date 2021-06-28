#14-Diseñe un pseudocódigo para calcular la suma y producto de N números enteros,
# utilizando un bucle controlado por el usuario.

class condicion:
  def read(suma,prod,num):
   suma = 0
   prod = prod*num
   while resp<>'N'and(resp<>'n'):
     num=input(num)
     suma = suma+num
     prod= prod*num
  print("Desea continuar(S/N)")
  read()
print("Total de la suma es{}".format(suma)) 
print("total de productoes:{} ".format(prod))
condicion()
