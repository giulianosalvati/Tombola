#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 11:37:39 2022

@author: mariaelenacontini
"""


"""

Classe giocatore

"""

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
        
        for i in range(0,len(self.cartelle)):
            self.cartelle[i].check_numero_estratto(numero_estratto)
        for j in range(0,len(self.cartelle)):
            vincite = self.cartelle[j].check_vincite(vincite)                                            

            
    