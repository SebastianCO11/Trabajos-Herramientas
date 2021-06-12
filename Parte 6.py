print("回回回回回回回回回回回回回回回回回")
print("回                          回")
print("回        Inventario        回")
print("回                          回")
print("回回回回回回回回回回回回回回回回回")
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
#leerImprimir()


def punto():
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
    for i in range (1,cantidad):
        for o in dic:
            cantidad_de_casos=[]
            add_productos= input("addP: ")
            nombre=input("nombre: ")
            precio=input("precio: ")
            cantidad= int(input("cantidad: "))
            cantidad_de_casos.append(nombre)
            cantidad_de_casos.append(precio)
            cantidad_de_casos.append(cantidad)
            dic[add_productos]=cantidad_de_casos
    cantidades=[]
    for k in codigo:
        cantidades.append(dic[k])
    cantidadtotal=0
    r=[]
    for u in range(len(cantidades)):
        cad=cantidades[u][2]
        r.append(cantidades[u][2])
    x=0
    for w in r:
        for q in range(len(r)):
            if w>r[-q]:
                x=w
                print(x)
    print(r)
    print(cantidades)
punto()
