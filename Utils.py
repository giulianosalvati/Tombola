#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 11:03:17 2022

@author: mariaelenacontini
"""

import argparse

import Giocatore




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
    Verifica se il numero di giocatori è rispetta le regole (>1 e <=8)
    
    Input
    -------
    n_giocatori (int): numero dei giocatori
    
    Output
    ------
    n_giocatori (int): numero dei giocatori
    oppure
    un messaggio e termina il programma
    """
        
    if n_giocatori>1 and n_giocatori<9:
        return n_giocatori
    else:
        print('\n- ERRORE - Il numero di giocatori deve essere superiore ad 1 fino ad un massimo di 8\n')
        exit()

def check_lista_cartelle(n_giocatori, lista_cartelle):
    """
    Verifica se la linghezza della lista di cartelle inserita corrisponde al numero
    di giocatori 

    Input
    -------
    n_giocatori (int): numero dei giocatori
    lista_cartelle (int[]): lista delle cartelle da assegnare a ciascun giocatore
    
    Output
    ------
    lista_cartelle (int[]): lista delle cartelle da assegnare a ciascun giocatore
    oppure
    un messaggio e termina il programma
    """
    if len(lista_cartelle)!=n_giocatori:
        print('\n- ERRORE -  Vi sono giocatori a cui non è stata assegnata alcuna cartella\n')
        if len(lista_cartelle)<n_giocatori:
            sc=n_giocatori-len(lista_cartelle)
            if sc == 1:
                 print(' *** Mancano cartelle a ' +str(sc)+' giocatore! ***\n')
            else:
                 print(' *** Mancano cartelle a ' +str(sc)+' giocatori! ***\n')
        else:
            sc=len(lista_cartelle)-n_giocatori
            if sc == 1:
                print(' *** Hai assegnato troppe cartelle, manca ' +str(sc)+' giocatore! ***\n')
            else:
                print(' *** Hai assegnato troppe cartelle, mancano ' +str(sc)+' giocatori! ***\n')
                
        exit()
    for c in lista_cartelle:
        if c<=0:
            print('\n- ERRORE -  Il numero delle cartelle per giocatore deve essere almeno 1\n')
            exit()
        elif c>5:
            print('\n- ERRORE -  Il numero delle cartelle non deve superare il limite di 5 cartelle per giocatore\n')
            exit()
    return lista_cartelle
      

# def domanda_di_stampa(n_giocatori,giocatori):
#     boolean = input('Vuoi vedere le cartelle dei giocatori? y/n : ')
#     if boolean == 'y' or boolean == 'yes':
#         nome_giocatore = input('Indica il numero del giocatore: ')
#         if nome_giocatore in list(range(1,n_giocatori+1)):
#             for i in range(0,n_giocatori):
#                 if giocatori[i].Giocatore.nome == str(nome_giocatore):
#                     giocatori[i].Giocatore.stampa_cartelle()
        
        
        
        
        




                    
                
