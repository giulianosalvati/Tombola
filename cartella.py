#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 13:51:10 2022

@author: mariaelenacontini
"""

class Cartella:
    
    def __init__(self,cartella):
        self.cartella = cartella
    
    # def check_numero_estratto(self,numero_estratto,INDEX):
    #     """
    #     Verifico che la cartella abbia o meno il numero estratto, per cui 
    #     se il numero era presente viene sostituito con -1 e stampato un messaggio
    #     altrimenti non viene modificata la cartella
    #     Non vi è alcuna uscita
              
    #      parametri di ingresso:
    #          numero_estratto (int) : il valore estratto dal tabellone
              
    #     """    
    #     colonna=numero_estratto//10 
    #     for riga in range(0,3):
    #         if self.cartella[INDEX][riga][colonna]==numero_estratto:    # Se la cartella presenta il numero
    #             self.cartella[INDEX][riga][colonna]=-1                  # Viene sostituito un -1 
    #             print('Ho il '+str(numero_estratto))
        
    

    # def check_vincite(self,vincite):       
    #     """
    #     Verifico che sia stata effettuata una vincita nella cartella.
    #     Restiruisce il parametro vincita il quale
    #     all'inizio del gioco vale 1 ed aumenta ogni volta che avviene una vincita
              
    #      parametri di ingresso:
    #          vincite (int) che mi dice a che vincita siamo arrivati 
             
    #     """                                           
        
    #     if vincite==5:                              # Se è gia stata vinta la cinquina
    #         # vedo se si è verificata la tombola: cioe i valori nella cartella sono solo 0 e -1
    #         occorenze = np.unique(self.cartella)
    #         if len(occorenze)==2: 
    #             print('Tombola!')
    #             print('------------------- FINE PARTITA ---------------------')
    #             sys.exit() 
                
    #         else:
    #             return vincite
            
    #     else:
    #         for riga in range(0,3):
    #             contatore=0
    #             vincita_successiva = vincite+1      
    #             for colonna in range(0,9):
    #                 if self.cartella[riga][colonna] == -1:
    #                     contatore=contatore+1
    #             if contatore == vincita_successiva:
    #                 vincite=vincita_successiva
    #                 if vincite==2 :
    #                     print('Ambo')
    #                     return vincite  
    #                 elif vincite==3 :
    #                     print('Terna')
    #                     return vincite  
                        
    #                 elif vincite==4 :
    #                     print('Quaterna')
    #                     return vincite  
                        
    #                 elif vincite==5 :
    #                     print('Cinquina')
    #                     return vincite
    #         return vincite
