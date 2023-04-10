idade = int(input("Digite a idade do trabalhador: "))
tempo_servico = int(input("Digite o tempo de serviço em anos: "))

if idade >= 65:
    print("Aposentadoria concedida por idade.")
elif tempo_servico >= 30:
    print("Aposentadoria concedida por tempo de serviço.")
elif idade >= 60 and tempo_servico >= 25:
    print("Aposentadoria concedida por idade e tempo de serviço.")
else:
    print("Não é possível se aposentar.")
