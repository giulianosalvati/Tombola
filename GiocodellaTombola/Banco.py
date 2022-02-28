#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 13:36:57 2022

@author: mariaelenacontini
"""

import Gruppo
import Giocatore
import random
import Cartellone


class Banco:
    """

    Classe Banco
    
    Utilizzata al fine di assegnare ai diversi giocatori le cartelle richieste.
        Attributi della classe:
            - n_giocatori: numero di giocatori che partecipano al gioco inseriti sulla linea di comando
            - lista_cartelle: lista di numeri, ciascuno corrispondente al numero delle cartelle richieste dall' i-esimo giocatore'
    
    """
        
    def __init__(self,n_giocatori,lista_cartelle):
        self.n_giocatori = n_giocatori
        self.lista_cartelle = lista_cartelle
     
    def assegna_cartelle(self):
        """
        Assegna a ciascun giocatore il numero richiesto di cartelle facendo in modo che
        non sia possibile assegnare a più giocatori la medesima cartella.
        
        Input
        -----
        NaN
        
        Output
        ------
        giocatori (giocatore[]) : lista di oggetti giocatore aventi ognuno il numero
                                  di cartelle richieste 
        
        """
        
        cartelle_disponibili=[]
        cartelle_disponibili = Gruppo.genera_gruppi(self.lista_cartelle)
        giocatori=[]

        # crea i giocatori (oggetti) e li inserisce nell'omonima lista
        
        for i in range(0,self.n_giocatori): 
            giocatori.append(Giocatore.Giocatore(str(i+1),self.lista_cartelle[i]))
            
            # a ciascun giocatore vengono assegnate, in maniera casuale tra quelle 
            # disponibili, il numero di cartelle richieste
            
            for j in range(0,self.lista_cartelle[i]):
                
                index_cartella = random.randint(0,len(cartelle_disponibili)-1)
                giocatori[i].prendi_cartella(cartelle_disponibili[index_cartella])
                cartelle_disponibili.pop(index_cartella)
                
        return giocatori
    
    def inizializza_cartellone(self):
        """
        Il metodo inizializza la classe Cartellone all'oggetto cartellone gli assegna le corrispondenti cartelle
        
        Input
        -----
        NaN
        
        Output
        ------
        cartellone (Cartellone) : l'oggetto cartellone che si comporta come un Giocatore con 6 cartelle 'speciali'
        
        """
        cartellone = Cartellone.Cartellone()
        cartellone.genera_cartellone()
        return cartellone
        
                    
def mostra_cartellone(cartellone):
    """
    Il metodo stampa il cartellone nel suo stato al momento della chiamata del 
    metodo per cui stampa l'elemento della casella se non è stato estratto o al 
    contrario se tale valore è stato estratto viene visualizzato con un asterisco
    
    Input
    -----
    cartellone( Cartellone) : l'oggetto cartellone che si comporta come un Giocatore con 6 cartelle 'speciali'
    
    Output
    ------
    stampa del cartellone
        
    """
    
    print('\nCartellone :\n')
        
    for i in range(6):
        if i%2==0:
            for r in range(3):
                print('[ ',end='')
                for c in range(5):
                    elemento = cartellone.elemento_cartella_cartellone(i,r,c)
                    if elemento == -1:
                        print('*',end=' ')
                    else:
                        print(int(elemento),end=' ')
                print(']',end=' ')
                print('[ ',end='')
                for c in range(5):
                    elemento = cartellone.elemento_cartella_cartellone(i+1,r,c)
                    if elemento == -1:
                        print('*',end=' ')
                    else:
                        print(int(elemento),end=' ')
                print(']')
            print('\n')
                    
        
        
        
        
        
        
    
    
      
        
        
            
            
        
        
            
            
        