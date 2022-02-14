 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 11:41:28 2022

@author: mariaelenacontini
"""

import Utils
import Banco
import Tabellone
import sys

args = Utils.initialize_parser()
n_giocatori = Utils.check_numero_giocatori(args.giocatori)
lista_cartelle = Utils.check_lista_cartelle(n_giocatori,args.numero_di_cartelle)

def check_estrazione_corrente(giocatori,numero_estratto,vincite):
    """
    Verifico che i giocatore abbiano o meno il numero estratto in una delle loro cartelle
    e che abbiano effettuato una vincita.   
         
    Input
    -----
    giocatori (Giocatore[]) : gli oggetti giocatori della tombola
    numero_estratto (int) : il valore estratto dal tabellone
    vincite (int): che mi dice a che vincita siamo arrivati 
     
    Output 
    ------
    vincite (int): che mi dice a che vincita siamo arrivati 
             
    """   
    
    for i in range(0,len(giocatori)):
        print('Giocatore'+ str(i+1)+' :') 
        giocatori[i].controllo_numero(numero_estratto)
        vincite= giocatori[i].controllo_vincite(vincite)
    
    return vincite

print('\n-----------   INIZIO GIOCO   -----------')

Banco = Banco.Banco(n_giocatori,lista_cartelle) 

# La variabile 'vincite' è una variabile globale inizializzata ad 1 che tiene il
# conto delle vincite uscite. Ogni volta che viene fatta una vincita, questa variabile 
# aumenta di 1. 
# ES.: viene fatto ambo --> vincite == 2 ... aumentando di 1 ad ogni vincita si avrà che 
# una volta che viene effutuata la cinquina 'vincite' è ==5. A questo punto il programma
# sa che la prossima vincià è la tombola
vincite = 1 
giocatori = Banco.assegna_cartelle()



N=90
for i,n in zip(range(1,N+1), Tabellone.Tabellone(N)):
      numero_estratto = n
      vincite = check_estrazione_corrente(giocatori,n,vincite)
      Utils.domanda_di_stampa(n_giocatori,giocatori)
      if vincite==6:
          print('\n------------------- FINE PARTITA ---------------------')
          sys.exit() 


