"""
12. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo
que calcule seu peso ideal, usando a seguinte formula: (72.7*altura) - 58
"""

#LISTA 1 - EXERCICIO 12

nome = input('Seja vem vinda (o), qual seu nome? ')
alt = float(input(f'{nome}, qual a sua altura em metros?'))
peso = (72.7*alt)-58
peso = round(peso,2)
print(f'Considerando sua altura, o peso ideal eh de {peso} Kg.')
