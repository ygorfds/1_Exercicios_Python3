# -*- coding: utf-8 -*-
"""
Created on Sat May 16 20:06:05 2020

@author: B1X4
"""

#LISTA 1 - EXERCÍCIO 15
a = input('Você trabalha?')
if a == 'Sim' or 'sim':
    b = float(input('Quanto você ganha por hora?'))
    c = float(input('Quantas horas/mês você trabalha?'))
sal_b = b*c

print('+ Seu salário bruto é de {} reais.'.format(round(sal_b,2)))

ir = 11/100*sal_b
print('- Desconto de IR: {} reais.'.format(ir))
    
inss = 8/100*sal_b
print('- Desconto de INSS: {} reais.'.format(inss))

sind = 5/100*sal_b
print('- Desconto de sindicato: {} reais.'.format(sind))

sal_l = sal_b-ir-inss-sind
print('= Seu salário líquido é de {} reais.'.format(sal_l))


    