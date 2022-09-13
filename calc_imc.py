def calc_imc():
    peso = float(input('Digite seu peso: '))
    altura = float(input('Digite sua altura: '))

    calculo_imc = peso / (altura * altura)

    if calculo_imc < 18.5:
        print('IMC:', calculo_imc, '- Abaixo do peso')
    elif calculo_imc <= 24.9 >= 18.5:
        print('IMC:', calculo_imc, '- Peso normal')
    else:
        print('IMC:', calculo_imc, '- Acima do peso')

    calcula_novamente = int(input('Calcular novamente? (s) ou (n): '))
    if calcula_novamente == 's':
        calculo_imc
    else:
        pass


if __name__ == '__main__':
    calc_imc()
