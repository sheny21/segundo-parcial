mail = input("Ingrese un mail:")
cantidad = 0  

x = 0  
while x < len(mail):  
    if mail[x] == "@":
        cantidad += 1  
    x += 1  

if cantidad == 1:
    print("Contiene solo un caracter @ el mail ingresado")  
else:
    print("Incorrecto")