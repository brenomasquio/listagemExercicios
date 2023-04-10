valor = float(input("Digite o valor da prestação em atraso: "))
taxa = float(input("Digite a taxa de juros em percentual: "))
tempo = int(input("Digite o tempo de atraso em dias: "))

prestacao = valor + (valor * (taxa / 100) * (tempo / 30))   # Cálculo do valor atualizado da prestação

print("O valor atualizado da prestação é: R$ {:.2f}".format(prestacao))