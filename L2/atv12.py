codigo = int(input("Digite o código do aluno: "))
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

if nota1 > nota2 and nota1 > nota3:
    maior_nota = nota1
    peso_maior = 4
elif nota2 > nota1 and nota2 > nota3:
    maior_nota = nota2
    peso_maior = 4
else:
    maior_nota = nota3
    peso_maior = 4

media = (nota1*3 + nota2*3 + nota3*2) / 8

print("Código do aluno:", codigo)
print("Notas: {:.1f}, {:.1f}, {:.1f}".format(nota1, nota2, nota3))
print("Média: {:.1f}".format(media))

if media >= 5:
    print("APROVADO")
else:
    print("REPROVADO")
