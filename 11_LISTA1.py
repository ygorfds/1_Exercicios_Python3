"""
11. Faça um Programa que peça 2 números inteiros e um número real. 
Calcule e mostre:
a. o produto do dobro do primeiro com metade do segundo .
b. a soma do triplo do primeiro com o terceiro.
c. o terceiro elevado ao cubo.
"""

#LISTA 1 - EXERCICIO 11
p1 = int(input('Digite um número inteiro:'))
p2 = int(input('Digite outro número inteiro:'))
p3 = float(input('Digite um número real:'))

a = (2*p1)*(0.5*p2)
print(a)

b = (3*p1)+(p3)
print(b)

c = p3**3
c = round(c,2)
print(c)
