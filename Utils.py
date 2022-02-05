#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 11:03:17 2022

@author: mariaelenacontini
"""

import argparse

import giocatore


def initialize_parser():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-g", "--giocatori",
                        help="Numero di giocatori",
                        required=True,
                        type=int)
    parser.add_argument("-n", "--numero_di_cartelle",
                        help="Numero di cartelle per ciascun giocatore",
                        type=int,
                        required=True,
                        nargs='+')
    return parser.parse_args()

def check_numero_giocatori(n_giocatori):
    """
    verifica se il numero di giocatori è rispetta le regole (>1 e <=8)
    restituisce il numero di giocatori se le regole sono rispettate,
    altrimenti stampa un messaggio e termina il programma 
    
    parametri di ingresso:
        n_giocatori (int): numero dei giocatori
    """
    if n_giocatori>1 and n_giocatori<9:
        return n_giocatori
    else:
        print('Errore - Il numero di giocatori deve essere superiore ad 1 fino ad un massimo di 12')
        exit()

def check_lista_cartelle(n_giocatori, lista_cartelle):
    """
    verifica se la linghezza della lista di cartelle inserita corrisponde al numero
    di giocatori 
    restituisce la lista delle cartelle se coincidono e se ad ogni giocatore sono assegnate
    da 1 a 5 cartelle,
    altrimenti stampa un messaggio e termina il programma 
    
    parametri di ingresso:
        n_giocatori (int): numero dei giocatori
        lista_cartelle (int[]): lista delle cartelle da assegnare a ciascun giocatore
    """
    if len(lista_cartelle)!=n_giocatori:
        print('Errore - Vi sono giocatori a cui non è stata assegnata alcuna cartella')
        if len(lista_cartelle)<n_giocatori:
            sc=n_giocatori-len(lista_cartelle)
            if sc == 1:
                 print(' *** Mancano cartelle a ' +str(sc)+' giocatore! ***')
            else:
                 print(' *** Mancano cartelle a ' +str(sc)+' giocatori! ***')
        else:
            sc=len(lista_cartelle)-n_giocatori
            if sc == 1:
                print(' *** Hai assegnato troppe cartelle, manca ' +str(sc)+' giocatore! ***')
            else:
                print(' *** Hai assegnato troppe cartelle, mancano ' +str(sc)+' giocatori! ***')
                
        exit()
    for c in lista_cartelle:
        if c<=0:
            print('Errore - Il numero delle cartelle per giocatore deve essere almeno 1')
            exit()
        elif c>5:
            print('Errore - Il numero delle cartelle non deve superare il limite di 5 cartelle per giocatore')
            exit()
    return lista_cartelle




def assegnazione_cartelle(n_giocatori,lista_cartelle,gruppi_cartelle):
    """
    Assegna a ciascun giocatore il numero richiesto di cartelle facendo in modo che
    non sia possibile assegnare a più giocatori la medesima cartella.
    Restituisce i giocatori inizializzati ognuno con il proprio nome, numero di cartelle che ha e 
    quel numero di cartelle.
    
    parametri di ingresso:
        n_giocatori (int): numero dei giocatori
        lista_cartelle (int[]): lista del numero di cartelle da assegnare a ciascun giocatore
        gruppi_cartelle: cartelle generate da assegnare a ciascun giocatore
    """
    
    giocatori={}
    nomi=['cartella1','cartella2','cartella3','cartella4','cartella5','cartella6']
    cartelle=[]
    for i in range(0,len(gruppi_cartelle)):
        cartelle.append(nomi)
    
    for i in range(1, n_giocatori+1):
        
        g=giocatore.Giocatore(str(i),lista_cartelle[i-1])
        
        for j in range (1,g.num_cartelle+1):
            
            for gruppo in list(range(0,len(gruppi_cartelle))):
                if len(cartelle[gruppo])!=0:
                    g.prendi_cartella(gruppi_cartelle[gruppo][cartelle[gruppo][0]])
                    cartelle[gruppo].pop(0)
                    break                    
                                         
        giocatori[str(i)]=g
        
    return giocatori





                    
                
