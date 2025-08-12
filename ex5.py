"""
Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
"""
vetor = []
vetorpar = []
vetorimpar = []

for i in range(5):
    n = int(input(f'digite um numero {i+ 1}º número '))
    vetor.append(n)
    if n % 2 == 0:
        vetorpar.append(n)
    else:
        vetorimpar.append(n)
# imprimir os dados dos vetores 
        print(f'vetor {vetor}')
        print(f'vetor par {vetorpar}') 
        print(f'vetor{vetorimpar}')

