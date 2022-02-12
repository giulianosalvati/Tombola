#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 10:23:41 2022

@author: giuliano
"""
import numpy as np

class Cartella:
    
    def __init__(self,cartella=None,conta_colonne=None,conta_righe=None):
        self.cartella = np.zeros((3,9))
        self.conta_colonne = np.zeros(9) # Contatore degli elementi sulle colonne della cartella
        self.conta_righe = np.zeros(3) # Contatore degli elementi sulle righe della cartella
    
    def aggiorna_conteggio(self,index_riga, index_colonna): 
        """
        Metodo che aggiorna i contatori su righe e colonne, incrementandoli di 1
        
        Input
        -----
        index_riga (int): indice riga da aggiornare
        index_colonna (int ): indice colonna da aggiornare
        
        Output
        ------
        Nan
        
        """
        
        self.conta_colonne[index_colonna] += 1
        self.conta_righe[index_riga] += 1
    
    
    def inserisci_numero(self,index_riga,index_colonna,numero):
        
        """
        Metodo che permette di inserire il numero in ingresso nella posizione [index_riga, index_colonna] 
        della cartella ed aggiorna i contatori su righe e colonne con il metodo della classe
        'aggiorna_conteggio'
        
        Input
        -----
        index_riga (int): indice riga in cui inserire il numero
        index_colonna (int ): indice colonna in cui inserire il numero
        numero (int): il numero da inserire nella cartella
        
        Output
        ------
        Nan
        
        """
        self.cartella[index_riga,index_colonna] = numero
        self.aggiorna_conteggio(index_riga, index_colonna)
    
    def elimina_numero(self,index_riga,index_colonna):
        
        """
        Tolgo dalla cartella il valore nella posizione [index_riga ,index_colonna] ponendolo
        a zero ed aggiorno i contatori su righe e colonne della cartella 
        con un decremento unitario
    
        Input
        -----
        index_riga (int): indice riga in cui inserire il numero
        index_colonna (int ): indice colonna in cui inserire il numero
        
        Output
        ------
        Nan
        
        """
        self.cartella[index_riga,index_colonna] = 0
        self.conta_colonne[index_colonna]-= 1
        self.conta_righe[index_riga] -= 1
    
    def azzera_contatori(self):
        """
        Metodo che azzera i contatori su righe e colonne della cartella
        
        Input
        -----
        NaN
        
        Output
        ------
        NaN
        
        """
        self.conta_colonne = np.zeros(9)
        self.conta_righe = np.zeros(3)
        
         
    def verifica_vincolo_righe(self,index_riga):
        """
        Il metodo mi dice se la riga di indice index_riga verifica o meno il vincolo 
        di avere al più 5 elementi
    
        Input
        -----
        index_riga (int): indice riga in cui inserire il numero
        
        Output
        ------
        boolean : indica se la riga supera o meno la verifica: se la supera True - altrimenti False
        
        """
        if self.conta_righe[index_riga]>=5:
            return False
        elif self.conta_righe[index_riga]<5:
            return True
        
    def posizione_libera(self,index_riga,index_colonna):
        """
        Il metodo mi dice se nella posizione [index_riga,index_colonna] è possibile
        inserire un numero, verificando che tale posizione non sia occupata e che la 
        somma degli elementi sulla riga non sia 5
    
        Input
        -----
        index_riga (int): indice riga in cui inserire il numero
        index_colonna (int ): indice colonna in cui inserire il numero
        
        Output
        ------
        boolean : indica se la posizione della cartella è libera per il posizionamento di un valore
        
        """
        if not self.verifica_vincolo_righe(index_riga):
            return False
        elif self.cartella[index_riga][index_colonna]!=0:
            return False
        else:
            return True
   
    def estrai_colonna(self, index_colonna):
        """
        Il metodo estrae dalla cartella la colonna di indice index_colonna
    
        Input
        -----
        index_colonna (int ): indice colonna idi riferimento
        
        Output
        ------
        colonna_selezionata (int[]): corrisponde alla lista degli elementi della colonna 
                                     di indice index_colonna 
        
        """
        
        colonna_selezionata = self.cartella[:,index_colonna]
        return colonna_selezionata
        
    
        
        
    
        
    
    
       