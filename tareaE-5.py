#5-Dado como dato la calificación de un alumno en un examen,escriba “aprobado” si 
# su calificación es mayor o igual que 7 y “Reprobado” en caso contrario.
def calificacion(cal):   
    cal= int(input("ingrese una calificacion: "))
    if cal >7:
         print("__usted_esta:")
         print('aprobado')
        
    else:
        print("lo sentimos _usted_esta:")
        print('Reprobado')
calificacion(0)










# "inicio
#   read(cal)
#   if cal >=7 then:
#     print("aprobado")
#   else:
#     print("reprobado")
#   end_if
# end 