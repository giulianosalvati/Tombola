#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 11:37:39 2022

@author: mariaelenacontini
"""

import numpy as np
import sys


class Giocatore:
    def __init__(self , nome , num_cartelle, cartelle=None):
        self.nome = nome
        self.num_cartelle = num_cartelle
        self.cartelle = []
        
    def prendi_cartella(self, cartella):     
        self.cartelle.append(cartella)
        
    def check_numero_estratto(self,cartella,numero_estratto):
        colonna=numero_estratto//10
        for riga in range(0,3):
            if cartella[riga][colonna]==numero_estratto:
                cartella[riga][colonna]=-1
                print('Ho il '+str(numero_estratto))
        return cartella
    
    def check_vincite(self,cartella,vincite):
        if vincite==5:
            # vedo se si è verificata la tombola: cioe i valori nella cartella sono solo 0 e -1
            occorenze = np.unique(cartella)
            if len(occorenze)==2: 
                print('Tombola!')
                print('------------------- FINE PARTITA ---------------------')
                sys.exit()
                
            else:
                return vincite
            
        else:
            for riga in range(0,3):
                contatore=0
                vincita_successiva = vincite+1
                for colonna in range(0,9):
                    if cartella[riga][colonna] == -1:
                        contatore=contatore+1
                if contatore == vincita_successiva:
                    vincite=vincita_successiva
                    if vincite==2 :
                        print('Ambo')
                        return vincite  
                    elif vincite==3 :
                        print('Terna')
                        return vincite  
                        
                    elif vincite==4 :
                        print('Quaterna')
                        return vincite  
                        
                    elif vincite==5 :
                        print('Cinquina')
                        return vincite
            return vincite


            
            
    