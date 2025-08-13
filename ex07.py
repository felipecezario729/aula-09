"""
Faça um programa que leia 5 números e informe o maior número.
"""
vetor = []
soma =0
multiplicacao = 1

for i in range(5):
    n = int(input(f'digite o {i+1}º número'))
    vetor.append(n)
    soma += n 
    multiplicacao *= n
print('os números são ...')
for i in range(5):
    print(f'{i+1}º número : {vetor[i]}')
print(f'  A  soma é {soma} e a m1 multiplicação {multiplicacao}')
