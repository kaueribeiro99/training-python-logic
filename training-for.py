# For gerando tabuada - primeira forma
numero = int(input('Digite um número de 1 a 10: '))
for n in range(1, 11):
    print(f'{numero} x {n} = {numero * n}')

# For gerando tabuada - segunda forma
tabuada=int(input("Tabuada do número: "))
for count in range(10):
    print("%d x %d = %d" % (tabuada, count+1, tabuada*(count+1)))