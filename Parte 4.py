print("回回回回回回回回回回回回回回回")
print("回                       回")
print("回      JaveTienda       回")
print("回                       回")
print("回回回回回回回回回回回回回回回")
print()


def inventario():
    dic={}
    codigo=[]
    longitud= int(input("longitud: "))
    i=0
    while i<longitud:
        productos= input("clave: ")
        dic[productos]=[]
        codigo.append(productos)
        i+=1
    cantidad=int(input("casos: "))
    p=0
    while p<cantidad:
        for o in dic:
            cantidad_de_casos=[]
            add_productos= input("addP ")
            nombre=input("nombre: ")
            precio=input("precio: ")
            cantidad= int(input("cantidad: +"))
            cantidad_de_casos.append(nombre)
            cantidad_de_casos.append(precio)
            cantidad_de_casos.append(cantidad)
            dic[add_productos]=cantidad_de_casos
        p+=1
    return dic,codigo

def leerImprimir():
    total= inventario()
    dic=total[0]
    n= total[1]
    k= input("producto a buscar: ")
    for i in n:
        m=int(dic[k][1])
        con_iva= m*0.08+m
        print(con_iva)
leerImprimir()


