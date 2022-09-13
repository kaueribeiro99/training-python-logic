def converted_mb():
    tamanho_arq = float(input("Informe o tamanho do arquivo em MB: "))
    velocidade = float(input("Informe a velocidade do link de internet em Mbps: "))

    res = tamanho_arq / (velocidade / 8) / 60
    print("O arquivo será baixado em:", res, "minutos")


if __name__ == '__main__':
    converted_mb()
