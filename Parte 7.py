print("回回回回回回回回回回回回回回回回")
print("回                        回")
print("回      Promedio Estu     回")
print("回                        回")
print("回回回回回回回回回回回回回回回回")
print()

Notas = []

EST =1
while EST <=30:
    Nt=eval(input("Digite aqui su nota: "))
    Notas.append(Nt)
    EST = EST + 1

print(Notas)

Rango=len(Notas)
contador=0
while contador<Rango:
    if Notas[contador]>4.5:
        print("notas mayores de 4.4: ", Notas[contador])
        print("Excelente desempeño")
    contador=contador+1
