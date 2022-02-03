#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 11:41:28 2022

@author: mariaelenacontini
"""

import Utils
import creaGruppo
 
args = Utils.initialize_parser()
n_giocatori = Utils.check_numero_giocatori(args.giocatori)
lista_cartelle = Utils.check_lista_cartelle(n_giocatori,args.numero_di_cartelle)

print('-----------   INIZIO GIOCO   -----------')
### assegnazione cartelle 
gruppi_cartelle=creaGruppo.crea_gruppi(lista_cartelle)
list_giocatori=Utils.assegnazione_cartelle(n_giocatori,lista_cartelle,gruppi_cartelle)