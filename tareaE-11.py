#11.Una escuela aplica dos exámenes a sus aspirantes, por lo que cada uno de ellos 
# obtiene dos calificaciones denotadas como C1 y C2. El aspirante que obtenga una 
# calificación mayor que 90 en cualquiera de los exámenes es aceptado; en caso contrario es rechazado.

def run():
    c1=input('c1->')
    c2=input('c2->')
    if(c1>=90)or(c2>=90):
        print("aceptado")
    else:
        print("rechazado")
run()



