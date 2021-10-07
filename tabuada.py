n = int(input('Digite um número para ver sua tabuada: '))
cont = 0
print('=' * 18)
print('Tabuada do {}'.format(n))
print('=' * 18)

while(cont <= 10):
    print('{} x {} = {}'.format(n, cont, (n * cont)))
    cont = cont + 1