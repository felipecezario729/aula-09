"""
Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
"""
vetor = []
total = 0
for i in range(10):
    letra = input('digite uma letra')
    vetor.append(letra)
    if letra.isalpha() and letra not in 'aeiou':
        total += 1
        print(f'Letra {vetor[i]}')
print(f'Foi informado {total} consoantes')

    