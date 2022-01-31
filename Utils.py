#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 11:03:17 2022

@author: mariaelenacontini
"""

import argparse

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
            
            
                
            
                    
                
