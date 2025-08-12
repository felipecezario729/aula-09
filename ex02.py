"""
Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
"""
lista = []
for i in range(3):
    l = float(input(f'digite o {i+1}º numero da lista'))
    lista.append(l)
lista.reverse()
for i in range(3):
    print(f'posição -> {i} na lista, tem o conteudo {lista[i]}')    