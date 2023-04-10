dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

if mes < 1 or mes > 12:
    print("Data inválida.")
else:
if mes == 2:
        if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
            dias_no_mes = 29
        else:
            dias_no_mes = 28
    elif mes in [4, 6, 9, 11]:
        dias_no_mes = 30
    else:
        dias_no_mes = 31

    if dia < 1 or dia > dias_no_mes:
        print("Data inválida.")
    else:
        print(f"{dia}/{mes}/{ano} é uma data válida.")
