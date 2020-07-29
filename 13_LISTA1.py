"""
13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo 
que calcule seu peso ideal, utilizando as seguintes fórmulas:
a. Para homens: (72.7*h) - 58
b. Para mulheres: (62.1*h) - 44.7

# lista 1 - exercicio 13

print('CALCULADORA - PESO IDEAL')
sexo=input('Qual o seu sexo?')
h=float(input('Qual a sua altura em metros?'))
if sexo=='Masculino' or 'masculino':
    peso=(72.7*h)-58
    print('Seu peso ideal eh de {} Kg.'.format(round(peso,2)))
if sexo=='Feminino or feminino':
    peso=(62.1*h)-44.7
    print('Seu peso ideal eh de {} Kg.'.format(round(peso,2)))
    