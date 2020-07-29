"""
9. Faรงa um Programa que peรงa a temperatura em graus Farenheit, transforme e 
mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9).
"""

# LISTA 1 - EXERCICIO 9
f = float(input('Entre com o valor da temperatura em F:'))
c = (5*f-160)/9
c = round(c,2)
print(f'{f} graus em FARENHEIT equivalem a {c} graus em CELSIUS.')
