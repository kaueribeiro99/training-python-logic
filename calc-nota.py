def calc_nota():
    nota_aluno = float(input("Digite uma nota entre 0 e 10: "))
    if nota_aluno <= 10:
        print("A nota digitada foi:", nota_aluno)
    else:
        while nota_aluno < 0 or nota_aluno > 10:
            nota_aluno = float(input("Nota digitada incorretamente. Digite uma nota entre 0 e 10: "))
        if nota_aluno <= 10:
            print("A nota digitada foi:", nota_aluno)


if __name__ == '__main__':
    calc_nota()
