#1.En ejemplos anteriores, diseñamos un pseudocódigo para encontrar la superficie 
# de un círculo para un radio cualquiera

def run(): 
    pi=0,3.1416
    R = input("----ingrese el radio del circulo-----: ")  
    R2=R*R
    superf=R2*pi
    print("-----la superficie del circulo es de-----:{}".format(superf))



if __name__=="__main__":
    run()   
