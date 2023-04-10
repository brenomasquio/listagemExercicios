salario_minimo = float(input("Digite o valor do salário mínimo: "))
quilowatts = float(input("Digite a quantidade de quilowatts gasta: "))

preco_por_quilowatt = salario_minimo / (100 * 7)
valor_a_pagar = preco_por_quilowatt * quilowatts

print("O valor a ser pago pela energia elétrica é de R$", valor_a_pagar)
