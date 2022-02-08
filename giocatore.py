#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 11:37:39 2022

@author: mariaelenacontini
"""


"""

Classe Giocatore

"""
import numpy as np
import sys

class Giocatore:
    
    # Costruttore
    def __init__(self , nome , num_cartelle, cartelle=None):
        self.nome = nome
        self.num_cartelle = num_cartelle
        self.cartelle = [] 
        

    def prendi_cartella(self, cartella_): 
        """
        Il giocatore aggiunge alle sue cartelle una nuova cartella.
        Non ci sono parametri restituiti.
              
        parametri di ingresso:
             cartella_ : cartella da aggiungere al giocatore
              
        """
        self.cartelle.append(cartella_)
    
    def controllo_cartelle(self,numero_estratto,vincite):
        """
        Verifico che il giocatore abbia o meno il numero estratto in una delle sue cartelle
         e che il giocatore abbia effettuato una vincita.
         Non ci sono parametri in uscita     
         
         parametri di ingresso:
             numero_estratto (int) : il valore estratto dal tabellone
             vincite (int): che mi dice a che vincita siamo arrivati 
              
        """   
        if numero_estratto==90:
            colonna = 8
        else:
            colonna=numero_estratto//10
        for i in range(0,len(self.cartelle)):
            for riga in range(0,3):
                if self.cartelle[i][riga][colonna]==numero_estratto:    # Se la cartella presenta il numero
                    self.cartelle[i][riga][colonna]=-1                  # Viene sostituito un -1 
                    print('Ho il '+str(numero_estratto))
        
        for i in range(0,len(self.cartelle)):
            if vincite==5:                              # Se è gia stata vinta la cinquina
                # vedo se si è verificata la tombola: cioe i valori nella cartella sono solo 0 e -1
                occorenze = np.unique(self.cartelle[i])
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
                        if self.cartelle[i][riga][colonna] == -1:
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
        
                                       

            
    