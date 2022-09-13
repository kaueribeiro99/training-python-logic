tabuada = int(input('Tabuada do número: '))
start = int(input('Começar do número: '))
end = int(input('Terminar no número: '))

if (end < start):
    print('O número final precisa ser maior que o inicial')
else:
    print('Vamos montar a tabuada do', tabuada, 'começando em', start, 'e terminando em', end)

for n in range(start, end+1):
    print(f'{tabuada} x {n} = {tabuada * n}')




