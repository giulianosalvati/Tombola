#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 10:23:41 2022

@author: giuliano
"""
import numpy as np

class Cartella:
    
    """
    La classe Cartella:
        Attributi della classe:
            - cartella che viene inizializzata come una matrice 3x9 di zeri e successivamente in 15 posizioni di
            questa matrice vengono inseririti seguendo i vincoli richiesti
            - conta_colonne è un vettore lungo 9 inizializzato come vettore di zeri.È un contatore degli
            elementi sulle colonne della cartella che viene incrementato di 1
            ogni volta che viene inserito un numero nella cartella nella rispettiva colonna
            e decrementa di 1 se eliminato
            - conta_righe è un vettore lungo 3 inizializzato come vettore di zeri. Analogo del 
            contatore precedente ma riferito alle righe
    """
    
    def __init__(self,cartella=None,conta_colonne=None,conta_righe=None):
        
        self.cartella = np.zeros((3,9))
        self.conta_colonne = np.zeros(9) 
        self.conta_righe = np.zeros(3) 
        
    
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
    
    def elemento_cartella(self,index_riga,index_colonna):
        """
        Il metodo restituisce l'elemento della cartella nella posizione 
        [index_riga,ondex_colonna].
    
        Input
        -----
        index_riga (int): indice riga della posizione
        index_colonna (int ): indice colonna della posizione
        
        Output
        ------
        elem (int): l'elemento della cartella nella posizione [index_riga,ondex_colonna]
                    che puo essere:
                        0 se a quella casella non è statto assegnato alcun valore
                        -1 se il valore in quella casella è stato estratto ed era presente nella cartella
                        oppure un valore da 1 a 90 
                    
        
        """
        elem = self.cartella[index_riga,index_colonna]
        return elem
    def azzera_contatori(self):
        """
        Metodo che azzera i contatori su righe e colonne della cartella
        
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
        
    def posizione_occupata(self,index_riga,index_colonna):
        """
        Il metodo verifica se la casella in posizione [index_riga,index_colonna]
        è vuota o contine un valore
    
        Input
        -----
        index_riga (int): indice riga della posizione
        index_colonna (int ): indice colonna della posizione
        
        Output
        ------
        boolean : True se la casella contine un valore o lo conteneva (quindi contine un 
                                                                       numero da 1 a 90 o -1)
                  False se la casella è vuota (quindi contiene 0)
                    
        
        """
        if self.elemento_cartella(index_riga, index_colonna) != 0:
            return True 
        else:
            return False
        
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
        elif self.posizione_occupata(index_riga,index_colonna):
            return False
        else:
            return True
   
    def estrai_colonna(self, index_colonna):
        """
        Il metodo estrae dalla cartella la colonna di indice index_colonna
    
        Input
        -----
        index_colonna (int ): indice colonna da estrarre
        
        Output
        ------
        colonna_selezionata (int[]): corrisponde alla lista degli elementi della colonna 
                                     di indice index_colonna 
        
        """
        
        colonna_selezionata = self.cartella[:,index_colonna]
        return colonna_selezionata
    
    def estrai_riga(self, index_riga):
        """
        Il metodo estrae dalla cartella la riga di indice index_riga
    
        Input
        -----
        index_riga (int ): indice riga da estrarre
        
        Output
        ------
        riga_selezionata (int[]): corrisponde alla lista degli elementi della riga
                                     di indice index_riga
        
        """
        
        riga_selezionata = self.cartella[index_riga,:]
        return riga_selezionata
        
    def numero_gia_estratto(self,index_riga,index_colonna):
        """
        Il metodo mi dice se nella posizione [index_riga,index_colonna] il valore
        è stato estratto (cioe uguale a -1 per la convenzione del programma)
    
        Input
        -----
        index_riga (int): indice riga della posiziona
        index_colonna (int ): indice colonna della posizione
        
        Output
        ------
        boolean : indica se nella posizione della cartella il numero è stato estratto o meno,
                 True se estratto - False se non è stato estratto
        
        """
        if self.cartella[index_riga][index_colonna] == -1:
            return True
        else:
            return False
 
    
    
       