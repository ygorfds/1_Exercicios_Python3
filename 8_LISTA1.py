"""
8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
"""

# LISTA 1 - EXERCÍCIO 8
nome = input('Olá, qual o seu nome?')
hora = float(input(f'{nome} quanto você ganha por hora trabalhada?'))
semanal = int(input(f'{nome}, quantas horas você trabalha por semana?'))
salario = hora*semanal*4
print(f'{nome}, seu salário mensal é de {salario} reais por mês.')