import math


def calc_tinta():
    litros_lata = 18
    preco_lata = 80

    m2 = float(input("Por favor, insira o tamanho da área em metros quadrados: "))
    litros_necessarios = m2 / 3

    # a - apenas latas de 18L
    qtd_latas = math.ceil(litros_necessarios / litros_lata)
    custo_latas = qtd_latas * preco_lata
    print("Somente latas de 18L:")
    print(f'O cliente precisa comprar {qtd_latas} latas, que custarão R${custo_latas}.')


if __name__ == '__main__':
    calc_tinta()
