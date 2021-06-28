#10-Una escuela aplica dos exámenes a sus aspirantes, por lo que cada uno de ellos 
# obtiene dos calificaciones denotadas como C1 y C2. El aspirante que obtenga 
# calificaciones mayores que 80 en ambos exámenes es aceptado; en caso contrario es rechazado.

def run():
    c1=input('c1->')
    c2=input('c2->')
    if(c1>=80)and(c2>=80):
        print("aceptado")
    else:
        print("rechazado")
run()




