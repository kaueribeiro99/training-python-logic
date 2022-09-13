def salario():
    sal_hora = float(input("Informe seu salário por hora: "))
    hora_mes = float(input("Informe a quantidade de horas trabalhadas no mês: "))

    salario_mes = (sal_hora * hora_mes)
    print("Salário Bruto:", salario_mes)
    ir = 11 / 100 * salario_mes
    print("IR:", ir)
    inss = 8 / 100 * salario_mes
    print("INSS:", inss)
    sindicato = 5 / 100 * salario_mes
    print("Sindicato:", sindicato)
    sal_liquido = (salario_mes - ir - inss - sindicato)
    print("Salário Liquido:", sal_liquido)


if __name__ == '__main__':
    salario()
