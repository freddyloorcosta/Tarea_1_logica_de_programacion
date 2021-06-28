#4.Construir un algoritmo tal, que dado como dato la calificación de un alumno 
# en un examen, escriba

class califi:
    cal= input("ingrese una calificacion: ")
    def calificacion(cal):
       if cal >7:
        cal=7
       print('aprobado')
    calificacion(0)
califi()