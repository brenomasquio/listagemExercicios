conta = input("Digite o número da conta corrente (3 dígitos): ")
conta_invertida = conta[::-1]
soma = int(conta) + int(conta_invertida)
soma_digitos = 0
for i, digito in enumerate(str(soma)):
    soma_digitos += int(digito) * (i+1)  
digito_verificador = soma_digitos % 10  
print("O dígito verificador da conta {} é {}".format(conta, digito_verificador))