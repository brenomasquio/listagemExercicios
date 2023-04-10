n_lados = int(input("Digite o número de lados do polígono: "))
medida_lado = float(input("Digite a medida do lado: "))

if n_lados == 3:
    perimetro = medida_lado * 3
    print("TRIANGULO - Perímetro:", perimetro)
elif n_lados == 4:
    area = medida_lado ** 2
    print("QUADRADO - Área:", area)
elif n_lados == 5:
    print("PENTAGONO")
elif n_lados < 3:
    print("Não é polígono")
else:
    print("Polígono não identificado")
