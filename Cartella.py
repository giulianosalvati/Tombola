#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 10:23:41 2022

@author: giuliano
"""
import numpy as np

class Cartella:
    
    def __init__(self,cartella=None,conta_colonne=None,conta_righe=None):
        self.cartella= np.zeros((3,9))
        # Inizializzo 2 matrici, conta_colonne (6,9) e conta_righe(6,3), che conteranno il numero di caselle occupate in ogni cartella, da utilizzare per verificare che i vincoli sulle righe(max 5 numeri) e sulle colonne siano rispettati
        # Nelle 2 matrici le righe i rappresentano le cartelle a cui si fa riferimento mentre le colonne rappresentano rispettivamente:
        #in conta_colonne(i,j): la colonna j-esima della cartella i-esima (j=0,1,2..9)
        #in conta_righe(i,r): la riga r-esima di ciascuna cartella i (r=0,1,2)
        self.conta_colonne= np.zeros(9)
        self.conta_righe= np.zeros(3)
    
    def aggiorna_conteggio(self,index_riga, index_colonna):
        
        self.conta_colonne[index_colonna]+=1
        self.conta_righe[index_riga] +=1
    
    
    def inserisci_numero(self,index_riga,index_colonna,numero):
        
        """
        Metodo che permette di inserire il numero in ingresso nella posizione [riga colonna] della cartella di indice dato
        
        Input
        -------
        index_cartella (int) : indice della cartella del gruppo
        riga (int): riga in cui inserire il numero
        colonna (int ): colonna in cui inserire il numero
        numero (int): il numero da inserire nella cartella
        
        Returns
        -------
        Nan
        
        """
        self.cartella[index_riga,index_colonna]= numero
        self.aggiorna_conteggio(index_riga, index_colonna)
    
    def elimina_numero(self,index_riga,index_colonna):
        
        """
        Tolgo dalla cartella il valore nella posizione [riga ,colonna]
    
        Input
        -------
        index_cartella (int) : indice della cartella del gruppo
        riga (int): riga in cui inserire il numero
        colonna (int ): colonna in cui inserire il numero
        
        Returns
        -------
        Nan
        
        """
        self.cartella[index_riga,index_colonna]=0
        self.conta_colonne[index_colonna]-=1
        self.conta_righe[index_riga] -=1
    
    def azzera_contatori(self):
        self.conta_colonne= np.zeros(9)
        self.conta_righe= np.zeros(3)
        
        
    
    
        
    
        
        
    
        
    
    
       