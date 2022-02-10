#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 17:22:02 2022

@author: mariaelenacontini
"""

"""
Classe Tabellone

"""

import random

class Tabellone(object):
    
    def __init__(self,n):
        
        self.n = n
        self.extracted = []
    
    def __iter__(self):
        """
        Metodo che restituisce un iteratore su iterabile
        """
        self.extracted = []
        return self
    
    def __next__(self):
        """
         Metodo per ottenere gli elementi uno alla volta fino a quando
         StopIteration non termina l'iterazione
         
         Input
         -----
         NaN
         Output
         ------
         x (int): il valore estratto tra 1 e 90
         ed un messaggio
         
         Altrimenti
         Avviene lo StopIteration
         
        """
        if len(self.extracted)<self.n:
            x = random.randint(1,self.n)
            while x in self.extracted:
                x = random.randint(1,self.n)
            self.extracted.append(x)
            print('\nÈ uscito il numero: ' + str(x))
            input('Premi INVIO per vedere i risultati e per continuare a giocare!')
            return x
        else:
            raise StopIteration


      
    