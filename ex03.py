"""
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

"""
notas =  []

soma = media = 0
for i in range(4):
    nota = float(input(f'Digite a {i+1}ª nota =>'))
    notas.append(nota)
    soma += nota 
media = soma/4    
print(f' A media das notas é {media}')


lista = []
for i in range(4):
    notas = float(input(f'Digite aqui o valor das {i+1}º notas: '))
    lista.append(notas)
print(f'A sua lista de notas é {lista}')

media = sum(lista) / len(lista)
print(f'A média das notas é {media}')