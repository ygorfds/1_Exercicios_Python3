#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 12:46:47 2020

@author: ygorfds
"""

#LISTA 1 - EXERCICIO 14

peixe=float(input('Quantos Kgs de peixe você pescou?'))
if peixe<=50 :
    print('Para 50 Kg de peixe ou menos, não haverá taxação.')
    print('Ou seja, não será taxado!')
else:
    exced=(peixe-50)
    taxa=exced*4
    print('Para 50 Kg de peixe ou menos, não haverá taxação.')
    print('Peso excedente, sujeito a taxação:{} Kgs.'.format(round(exced,2)))
    print('Como ultrapassou o limite, sua taxa será de R$ {}.'.format(round(taxa,2)))
    
    