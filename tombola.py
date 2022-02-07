#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 11:41:28 2022

@author: mariaelenacontini
"""

import Utils
import Banco

args = Utils.initialize_parser()
n_giocatori = Utils.check_numero_giocatori(args.giocatori)
lista_cartelle = Utils.check_lista_cartelle(n_giocatori,args.numero_di_cartelle)

print('-----------   INIZIO GIOCO   -----------')

Banco = Banco.Banco(n_giocatori,lista_cartelle) 
vincite = 1
giocatori = Banco.assegna_cartelle()


# N=90
# for i,n in zip(range(1,N+1), tabellone.Tabellone(N)):
#     numero_estratto = n
#     Utils.check_estrazione_corrente(giocatori,numero_estratto,vincite)


