a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))

temp = a
a = b
b = temp

print("Valores trocados: A = {}, B = {}".format(a, b))