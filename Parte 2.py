print("回回回回回回回回回回回回回回回回")
print("回                        回")
print("回       Javeciales       回")
print("回                        回")
print("回回回回回回回回回回回回回回回回")
print()

Nota1 = float(input("Digite la nota del primer parcial: "))
Nota2 = float(input("Digite la nota del segundo parcial: "))
Nota3 = float(input("Digite la nota del taller: "))
Nota4 = float(input("Digite la nota del proyecto: "))

Total = (Nota1 * 0.25) + (Nota2 * 0.25) + (Nota3 * 0.20) + (Nota4 * 0.30)

print("Resultado: ", Total)

if Total >= 3.0:
    print ("De milagro, pero paso la materia")
elif Total >= 4.0:
    print ("Excelente, sigue esforzandote")
elif Total >= 4.5:
    print ("Un desempeño espectacular")
else:
    ()
