quantidade_fitas = int(input("Digite a quantidade de fitas da locadora: "))
valor_aluguel = float(input("Digite o valor do aluguel de cada fita: "))

faturamento_mensal = quantidade_fitas / 3 * valor_aluguel
faturamento_anual = faturamento_mensal * 12
print("Faturamento anual da locadora: R$ {:.2f}".format(faturamento_anual))

multas_mensais = quantidade_fitas / 10 / 10 * valor_aluguel * 0.1
print("Valor ganho com multas por mês: R$ {:.2f}".format(multas_mensais))

fitas_estradas = quantidade_fitas * 0.02
fitas_compradas = quantidade_fitas / 10
quantidade_fitas_final = int(quantidade_fitas - fitas_estradas + fitas_compradas)
print("Quantidade de fitas no final do ano: {}".format(quantidade_fitas_final))