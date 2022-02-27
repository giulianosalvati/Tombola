#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 11:37:39 2022

@author: mariaelenacontini
"""


import numpy as np
import Cartella

class Giocatore:
        
    """
    
    Classe Giocatore che prende le cartelle assegnatele dal banco, controlla 
    su di essa i numeri estratti e comunica la vincita.
        Attributi della classe:
            - nome: identificativo del giocatore.
            - num_cartelle: numero delle cartelle richieste dal giocatore.
            - cartelle: lista inizializzata vuota che successivamente verrà riempita nel momento in cui 
                       il banco assegna le cartelle richieste dal giocatore.
    
    """
    
    # Costruttore
    def __init__(self , nome , num_cartelle, cartelle=None):
        self.nome = nome
        self.num_cartelle = num_cartelle
        self.cartelle = [] 
        

    def prendi_cartella(self, cartella_): 
        """
        Il giocatore aggiunge alle sue cartelle una nuova cartella.
        Non ci sono parametri restituiti.
                      
        Input:      
        ------
        cartella_ : cartella da aggiungere al giocatore     
           
        Output
        ------
        Nan
            
        """
        self.cartelle.append(cartella_)
    
    def controllo_numero(self,numero_estratto):
        """
        Verifico che il giocatore abbia o meno il numero estratto in una delle sue cartelle
        ed in caso positivo viene posto uguale a -1 per 'segnarlo'
         
        Input:      
        ------
        numero_estratto (int) : il valore estratto dal tabellone
        
        Output
        ------
        Nan
              
        """   
        if numero_estratto==90:
            colonna = 8
        else:
            colonna=numero_estratto//10
        stampa = True                                # Questo valore mi dice se devo stampare il fatto di avere o meno un numero
                                                    # viene inizializzato a true quindi se il giocatore ha in una delle sue cartelle il numero
                                                    # viene stampato un messaggio e reso false la variabile, cosi da non stampare il messaggio nel caso in cui
                                                    # il giocatore abbia nuovamente il numero in altre cartelle
        for i in range(0,len(self.cartelle)):
            for riga in range(0,3):
                if self.cartelle[i].cartella[riga][colonna]==numero_estratto:    # Se la cartella presenta il numero
                    self.cartelle[i].cartella[riga][colonna]=-1                  # Viene sostituito un -1 
                    
                    
                    if stampa:                     # Tale if è necessario per non stampare più 
                                                        # di una volta il messaggio
                        print('Ho il '+str(numero_estratto))
                        stampa = False
        
        
    def controllo_vincite(self,vincite):
        """
        Verifico che il giocatore abbia o meno effettuato una vincita.
         
        Input:      
        ------
        vincite (int): che mi dice a che vincita siamo arrivati 
        
        Output
        ------
        Nan
              
        """   
    
        for i in range(self.num_cartelle):
           
            if vincite==5:           # Se è gia stata vinta la cinquina
                                    # vedo se si è verificata la tombola: 
                                    # cioe i valori nella cartella sono solo 0 e -1
                occorenze = np.unique(self.cartelle[i].cartella)
                
                if len(occorenze)==2: 
                    
                    print('Tombola!')
                    vincite = 6 
                    
                else:
                    
                    return vincite
                
            else:
                for riga in range(0,3):
                    contatore=0
                    vincita_successiva = vincite+1      
                    for colonna in range(0,9):
                        if self.cartelle[i].numero_gia_estratto(riga,colonna):
                            contatore=contatore+1
                    if contatore == vincita_successiva:
                        vincite = vincita_successiva
                        
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
        
    def mostra_cartelle(self):
        """
        Il metodo permette di mostrare le cartelle del giocatore nel loro stato al 
        momento della chiamata del metodo. Se un numero è stato estratto
        ed era presente nella cartella, viene mostrato con il simbolo '*', le caselle
        della cartella che non contengono nulla (per convenzione del programma sono 0) 
        vengono mostrati come spazi vuoti, mentre tutti gli altri numeri della cartella
        che non sono stati estratti vengo visualizzati normalmente.
        
        Input
        -----
        NaN
        
        Output
        ------
        Vengono stampate le cartelle del giocatore come descritto precedentemente
        e il metodo non ha variabili di output
        """
        
        print(f"\nCartelle del giocatore {self.nome} :\n")
        for i in range(0,len(self.cartelle)):
            print('Cartella '+str(i+1))
            for r in range(3):
                print('[ ',end='')
                for c in range(9):
                    if self.cartelle[i].elemento_cartella(r,c) == 0:
                        print(' ',end=' ')
                    elif self.cartelle[i].elemento_cartella(r,c) == -1:
                        print('*',end=' ')
                    else:
                        print(int(self.cartelle[i].elemento_cartella(r,c)),end=' ')
                print(']')
                
                
                
                