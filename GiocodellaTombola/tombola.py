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
# Verifica che i dati inseriti siano corretti:
n_giocatori = Utils.check_numero_giocatori(args.giocatori)
lista_cartelle = Utils.check_lista_cartelle(n_giocatori,args.numero_di_cartelle)

def check_estrazione_corrente(giocatori,numero_estratto,vincite,cartellone):
    """
    Verifico che i giocatore abbiano o meno il numero estratto in una delle loro cartelle
    e che abbiano effettuato una vincita.   
         
    Input
    -----
    giocatori (Giocatore[]) : gli oggetti giocatori della tombola
    numero_estratto (int) : il valore estratto dal tabellone
    vincite (int): che mi dice a che vincita siamo arrivati 
    cartellone(Cartellone[]):  oggetto cartellone 
    
    Output 
    ------
    vincite (int): che mi dice a che vincita siamo arrivati 
             
    """       
    for i in range(0,len(giocatori)):
        print('Giocatore'+ str(i+1)+' :') 
        giocatori[i].controllo_numero(numero_estratto)
        vincite= giocatori[i].controllo_vincite(vincite)
    index_cartella_numero_estratto=cartellone.check_estrazione_cartellone(numero_estratto) # In uscita ho l'indice della cartella del cartellone che contine il numero estratto
    vincite = cartellone.check_vincite_cartellone(vincite,index_cartella_numero_estratto)
        
    return vincite

print('\n-----------   INIZIO GIOCO   -----------')

# Inizializzazione del Banco, che assegna le cartelle ai giocatori ed inizializza il cartellone
Banco = Banco.Banco(n_giocatori,lista_cartelle) 
giocatori = Banco.assegna_cartelle() 
cartellone= Banco.inizializza_cartellone()

# La variabile 'vincite' ci indica la vincita a cui siamo arrivati ed è inizializzata a 1,
# ogni volta che si verifica una vincita tale variabile incrementa di 1. Il gioco termina
# quando 'vincite' è uguale a 6, cioè quando viene effettuata la tombola.
vincite = 1

N=90
for i,n in zip(range(1,N+1), Tabellone.Tabellone(N)):
      numero_estratto = n
      vincite = check_estrazione_corrente(giocatori,n,vincite,cartellone)
      Utils.domanda_di_stampa(n_giocatori,giocatori,cartellone)
      if vincite==6: # Se è stata fatta tombola -> termina il gioco
          print('\n------------------- FINE PARTITA ---------------------')
          sys.exit() 


