#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 11:06:50 2022

@author: giuliano
"""
import random

estratti=[]
while len(estratti) <90:
    numero= random.randint(1,90)
    if numero not in estratti:
        print('New extract number',numero)
        estratti.append(numero)
        input('Continue')
        