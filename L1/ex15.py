PI = 3.1416   # constante PI

raio = float(input("Digite o valor do raio da lata de óleo: "))
altura = float(input("Digite o valor da altura da lata de óleo: "))

volume = PI * (raio ** 2) * altura   # Cálculo do volume da lata de óleo

print("O volume da lata de óleo é: {:.2f}".format(volume))