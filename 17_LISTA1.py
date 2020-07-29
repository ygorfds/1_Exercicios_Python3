#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 17:13:39 2020

@author: ygorfds
"""

print('CALCULADORA DE VOLUME DE TINTA - LOJA SUVINIL')

b = float(input('(1) Entre com o valor da base em metros:'))
h = float(input('(2) Entre com o valor da altura em metros:'))
print()
a = b*h
print('- A área do cômodo é {} m2;'.format(a))
v = a/6
print('- O volume de tinta necessário é de {} litros.'.format("%.2f" % v))
print()

v1 = 3.6 #volume de 3,6 litros referente ao galão
p1 = 25 #preço de R$ 25,00 referente ao galão 
v2 = 18 #volume de 18 litros referente a lata 
p2 = 80 #preço de R$ 80,00 referente a lata

q1 = v/v1 #divisão entre o volume calculado e o volume do galão de 3,6 litros
q2 = v/v2 #divisão entre o volume calculado e o volume do galão de 18 litros
q3 = v//v1 #divisão INTEIRA entre o volume calculado e o volume do galão
q4 = v//v2 #divisão INTEIRA entre o volume calculado e o volume da lata


# CONDIÇÃO 1: VOLUME PARA COMPRA MENOR OU IGUAL A 3,6 LITROS-------------------
if v<=v1:
    print('CONDIÇÃO 1')
    print('Sugiro comprar 1 galão de 3,6 litros.') 
    print('O valor total ficará em {} reais.'.format(p1))
   
# CONDIÇÃO 2: VOLUME PARA COMPRA ENTRE 3,6 E 18 LITROS (DUAS CONDIÇÕES DE PREÇO PARA ESCOLHA)
if v>v1 and v<v2: 
    print('CONDIÇÃO 2')
    q1 = round(q1+0.5) #NOVO q1: NÚMERO DE GALÕES UTILIZANDO ARRENDONDAMENTO PRA CIMA (VALOR REAL)
    pt1 = q1*p1 #PREÇO TOTAL DOS GALÕES - CONDIÇÃO 2.1
    print('Sugiro comprar {} galões de 3,6 litros, totalizando {} reais; ou'.format(q1,pt1))
    # OUTRA OPÇÃO NA CONDIÇÃO 2
    q2 = round(q2+0.5) #NOVO q2: NÚMERO DE LATAS UTILIZANDO ARRENDONDAMENTO PRA CIMA (VALOR REAL)
    pt2 = q2*p2 #PREÇO TOTAL DAS LATAS - CONDIÇÃO 2.2
    print('Sugiro comprar {} lata de 18 litros, totalizando {} reais.'.format(q2,pt2))

# CONDIÇÃO 3: VOLUME PARA COMPRA TINTA - PÓS 18 LITROS (CONDIÇÃO DE COMPRA SOMENTE DE LATAS DE 18l)    
if v>=v2 and v%v2==0:
    print('CONDIÇÃO 3')
    pt3 = q2*p2 #PREÇO TOTAL DAS LATAS - CONDIÇÃO 3
    print('Sugiro comprar {} latas de 18 litros, totalizando {} reais.'.format(q2,pt3))  
         
# CONDIÇÃO 4: VOLUME PARA COMPRA DE TINTA - COMBINAÇÃO DE LATAS E GALÕES DE TINTA    
if v>=v2 and v%v2!=0:
    print('CONDIÇÃO 4')
    q2 = round(q2-0.5) #NOVO q2: NÚMERO DE LATAS UTILIZANDO ARRENDONDAMENTO PRA BAIXO (VALOR REAL)
    r = v%v2 #RESTO DA RAZAO ENTRE O VOLUME CALCULADO E O VOLUME DE 18 LITROS DA LATA
    r2 = r/v1 #RAZÃO ENTRE O RESTO DA EQUAÇÃO ACIMA E O VOLUME DE 3,6 LITROS DO GALÃO
    r2 = round(r2+0.5) #NOVO r2: VALOR REFERENTE A RESTANTE DE TINTA (GALÃO) PARA SOMAR C/ AS LATAS
    vt = (q2*v2)+(r2*v1) #CÁLCULO DO VOLUME TOTAL DE TINTA
    print('Sugiro comprar:')
    print('- {} latas (18 litros cada) + {} galões (3,6 litros cada);\n- Com volume total de: {} litros.'.format(q2,r2,vt))
    pt4 = q2*p2 #PREÇO TOTAL DAS LATAS - CONDIÇÃO 4.1
    pt5 = r2*p1 #PREÇO TOTAL DAS GALÕES - CONDIÇÃO 4.2
    pt6 = pt4+pt5 #SOMATÓRIO DOS PREÇOS DAS LATAS E DOS GALÕES
    print('O valor total será de {} reais, sendo {} reais pelas latas e {} reais pelos galões.'.format(pt6,pt4,pt5))                                                        
                                                              
                                                    
    

                


    

    


    