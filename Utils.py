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
    if n_giocatori>1 and n_giocatori<13:
        return n_giocatori
    else:
        print('Errore - Il numero di giocatori deve essere superiore ad 1 fino ad un massimo di 12')
        exit()

def check_lista_cartelle(n_giocatori, lista_cartelle):
    if len(lista_cartelle)!=n_giocatori:
        print('Errore - Il numero di giocatori e quello delle cartelle non coincidono')
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
    
    
        

                
            
                    
                
