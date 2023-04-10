num_identificacao = int(input("Digite o número de identificação do aluno: "))
nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
nota3 = float(input("Digite a terceira nota do aluno: "))
me = float(input("Digite a média dos exercícios do aluno: "))

ma = (nota1 + nota2*2 + nota3*3 + me) / 7

if ma >= 9:
    conceito = "A"
    situacao = "APROVADO"
elif 7.5 <= ma < 9:
    conceito = "B"
    situacao = "APROVADO"
elif 6 <= ma < 7.5:
    conceito = "C"
    situacao = "APROVADO"
elif 4 <= ma < 6:
    conceito = "D"
    situacao = "REPROVADO"
else:
    conceito = "E"
    situacao = "REPROVADO"

print("Número de identificação:", num_identificacao)
print("Notas: %.1f, %.1f, %.1f" % (nota1, nota2, nota3))
print("Média dos exercícios: %.1f" % me)
print("Média de aproveitamento: %.1f" % ma)
print("Conceito:", conceito)
print("Situação:", situacao)
