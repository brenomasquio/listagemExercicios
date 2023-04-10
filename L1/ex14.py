valor_produto = float(input("Digite o valor do produto: "))

desconto = 0.09   # desconto de 9%

novo_valor = valor_produto - (valor_produto * desconto)

print("Novo valor com desconto: R$ {:.2f}".format(novo_valor))