DIASANO = 365
SEMANAANO = 48
MESANO = 12
HORASANOS = 8.766


def calc_anos_dias():
    idade_anos = int(input('Digite sua idade em anos: '))

    calc_idade_segundos = idade_anos * (HORASANOS * 60) * 60
    calc_idade_minutos = idade_anos * (HORASANOS * 60)
    calc_idade_horas = idade_anos * HORASANOS
    calc_idade_dias = idade_anos * DIASANO
    calc_idade_semanas = idade_anos * SEMANAANO
    calc_idade_meses = idade_anos * MESANO

    print('Você tem', calc_idade_segundos, 'segundos de vida!')
    print('Você tem', calc_idade_minutos, 'minutos de vida!')
    print('Você tem', calc_idade_horas, 'horas de vida!')
    print('Você tem', calc_idade_dias, 'dias de vida!')
    print('Você tem', calc_idade_semanas, 'semanas de vida!')
    print('Você tem', calc_idade_meses, 'meses de vida!')


if __name__ == '__main__':
    calc_anos_dias()
