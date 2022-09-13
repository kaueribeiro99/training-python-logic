#Exercicio 1
print("Lojas Quase Dois - Tabela de preços")
a = 1
while a < 51:
    print(a, "Total R$:", (a * 1.99))
    a = a + 1

#Exercicio 2
print("Panificadora Pão de Ontem - Tabela de preços")
quantity = int(input("Informa a quantidade de pães: "))
while quantity < 51:
    print(quantity, "Total R$:", (quantity * 0.18))
    quantity = quantity + 1

#Exercicio 3
caract = []
vogais = ["a", "e", "i", "o", "u"]
contvogal = 0
x = 1
while x <= 10:
    entrada = input("Caractere %d: " % x)
    x += 1
    caract.append(entrada)
    if entrada in vogais:
        contvogal += 1
print("Consoantes: ", (len(caract)) - contvogal)

# While até mostrar o número correto
nota = float(input("informe um numero de 0 a 10: "))
while (nota > 10) or (nota < 0):
    nota = float(input("informe um numero de 0 a 10: "))
print('A nota digitada foi:', nota)

# While não permite usuário e senha iguais
usuario = str(input('Digite seu usuário: '))
senha = str(input('Digite sua senha: '))
while usuario == senha:
    print("Erro: O usuário não pode ser igual a senha, tente novamente")
    usuario = str(input('Digite seu usuário: '))
    senha = str(input('Digite sua senha: '))
else:
    print('Usuário registrado com sucesso !')

# While para validar informação
nome = str(input('Informe seu nome: '))
while (len(nome) <= 3):
    nome = str(input('Informe seu nome: '))

idade = int(input('Informe sua idade: '))
while (idade > 150 or idade < 0):
    idade = int(input('Informe sua idade: '))

salario = float(input('Informe seu salário: '))
while (salario < 0):
    salario = float(input('Informe seu salário: '))

sexo = str(input('Informe a inicial do seu sexo: (M ou F): '))
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Informe a inicial do seu sexo: (M ou F): '))

estado_civil = str(input('Informe a inicial do seu estado civil (S,C,V ou D): '))
while (estado_civil != "S" and estado_civil != "C" and estado_civil != "V" and estado_civil != "D"):
    estado_civil = str(input('Informe a inicial do seu estado civil (S,C,V ou D): '))

print('Os dados digitados foram:')
print('Nome:', nome)
print('Idade:', idade)
print('Salario:', salario)
print('Sexo:', sexo)
print('Estado Civil:', estado_civil)

# While ultrapassa população
a = 80000
b = 200000
ano = 0

while a <= b:
    a += a * 0.03
    b += b * 0.015
    ano += 1

print("A População 'A' ultrapassa ou iguala a População 'B' em %d anos" % ano)





