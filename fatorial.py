import math
numero = int(input("\nDigite o número que quer realizar o fatorial : "))
count = numero
fatorial = math.factorial(numero)

for i in range(numero - 1):
    print(count, end=" x ")
    count -= 1
print("1 =", fatorial)