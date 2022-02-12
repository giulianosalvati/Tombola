#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 12:16:53 2022

@author: giuliano

"""

"""
Classe  che fornisce in uscita una lista di 6 cartelle (1 gruppo) che soddisfa i vincoli preposti

"""

import math
import random 
import Cartella
import numpy as np


class Gruppo:
    
    posizione_scelta=5
    
    def __init__(self,gruppo_cartelle=None):
        
        self.gruppo_cartelle=[]
        
   
    def inizializza_cartelle(self):
       
        """
        Inizializzazione del gruppo di 6 cartelle costituenti il gruppo
        
        Input
        -----
        None.

        Output
        -------
        Gruppo di sei cartelle (matrici 3x9) di zeri

        """
        for i in range(0,6):
            cartella= Cartella.Cartella()
            self.gruppo_cartelle.append(cartella)
    
    
    def posiziona_90(self):
        
        """
        Il numero 90, come imposto dai vincoli, viene collocato in basso a dx 
        nella cartella indetta dalla variabile globale (ultima cartella)
        
        Input
        -----
        None.

        Output
        -------
        None.

       
        """
        
        self.gruppo_cartelle[self.posizione_scelta].inserisci_numero(2,8,90)
        
   
    def assegna_posizioni(self):
       
        """
        Metodo che assegna 1 in posizioni tali da rispettare i vincoli sulle righe
        
        Input
        -----
        None.

        Output
        -------
        Gruppo di cartelle (matrici 3x6) costituite da 0 e 1, in particolare 5 uni su ciascuna riga

        """
        
        
        # assegno almeno un 1 su ciascuna colonna di ciascuna cartella, scegliendo casualmente la riga (occupando 54 caselle) 
        
        for i in range(0,6):
            for j in range(0,9):
                if(i== self.posizione_scelta and j==8): #su questa colonna già c'è almeno un numero, ovvero 90 (non devo riassegnarlo)
                    pass
                else:
                    r=random.randrange(3)
                    while self.gruppo_cartelle[i].conta_righe[r]==5: #nell'estrazione random tengo conto del vincolo sulle righe: se ho già 5 elementi su una riga ne devo estrarre un'altra
                        r=random.randrange(3)
                    
                    self.gruppo_cartelle[i].inserisci_numero(r,j,1)
                    
        # occupo le restanti 36 caselle in maniera casuale, rispettando però i vincoli sulle righe ed evitando sovrascritture
  
        for k in range(0,36):
            i=random.randrange(6)
            j=random.randrange(9)
            r=random.randrange(3)
            while not self.gruppo_cartelle[i].posizione_libera(r,j):
                i=random.randrange(6)
                j=random.randrange(9)
                r=random.randrange(3)
            self.gruppo_cartelle[i].inserisci_numero(r,j,1)
        
    
    def swap_posizioni(self,vincoli):
        
        """
        
        Il seguente metodo permette un controllo riga per riga, considerando i vincoli sulle colonne,
        in maniera tale da effettuare, al fine di rispettare questi ultimi, uno swap tra opportuni posizionamenti.

        Input
        ----------
        vincoli (array[]): lista contenente 9 elementi ciascuno corrispondente al numero massimo di elementi di ciascuna colonna del gruppo

        Output
        -------
        Gruppo di cartelle (matrici 3x6) costituite da 0 e 1, rispettante sia i vincoli sulle colonne che quelli sulle righe

        """
      
        
        for i in range(0,6): 
            for r in range(0,3):
                riga= self.gruppo_cartelle[i].cartella[r]
                indici_occupati= np.argwhere(riga==1) #trovo indici delle caselle occupate su quella riga
                for k in indici_occupati:
                    somma_colonne=np.zeros(9)
                    for c in range(0,6):
                        for colonna in range(0,9):
                            somma_colonne[colonna] += self.gruppo_cartelle[c].conta_colonne[colonna] # è un vettore che contiene il numero totale delle caselle occupate per ciascuna colonna del gruppo_cartelle
                    if(somma_colonne[k]>vincoli[k] and self.gruppo_cartelle[i].conta_colonne[k]>1):
                        indici_vuoti=np.argwhere(riga==0)
                        differenza= vincoli[indici_vuoti]-somma_colonne[indici_vuoti]
                        colonna_min=np.argmax(differenza) #scelgo la colonna in cui la differenza tra vincoli e s_colonne è massima
                        swap=indici_vuoti[colonna_min]
                        self.gruppo_cartelle[i].elimina_numero(r,k)
                        self.gruppo_cartelle[i].inserisci_numero(r,swap,1) #applico lo swap e aggiorno i contatori
                        
        
        
        
    def assegna_numeri(self):
        
        """
        Collocazione dei numeri da 1 a 90 nelle posizioni individuate (sostituisco gli uni presenti nelle 6 cartelle)
        
        Input
        -----
        None.

        Output
        -------
        None.

        """
        # Dopo aver trovato le posizioni assegno i numeri da 1 a 90, in maniera casuale nelle posizioni individuate nel gruppo_cartelle
                   
        # Inizio con la prima colonna del gruppo, assegnando i numeri da 1 a 9
        estratti=[]
        for i in range(0,6):
            self.gruppo_cartelle[i].azzera_contatori()
            colonna=self.gruppo_cartelle[i].cartella[:,0] 
            # Individuo sulla colonna della singola cartella quali sono le posizioni occupate a cui devo assegnare un numero da 1 a 9
            pos_occ=np.argwhere(colonna==1) 
            for j in pos_occ:
                n=random.randrange(1,10) #estraggo un numero a caso tra 1 e 9 che non sia già stato estratto
                while n in estratti:
                    n=random.randrange(1,10)
                self.gruppo_cartelle[i].inserisci_numero(int(j),0,n)
                estratti.append(n)
                           
        # Continuo con le restanti colonne
        for k in range(1,9):
            estratti=[]
            for i in range(0,6):
                colonna=self.gruppo_cartelle[i].cartella[:,k]
                pos_occ=np.argwhere(colonna==1)
                for j in pos_occ:
                    n=random.randrange(k*10,(k+1)*10)
                    while n in estratti:
                        n=random.randrange(k*10,(k+1)*10)
                    self.gruppo_cartelle[i].inserisci_numero(int(j),k,n)
                    estratti.append(n)
   
        
    
    def crea_gruppo(self):
        
        """
        Implementazione del gruppo di 6 cartelle
        
        Input
        -------
        Nan.
       

        Output
        -------
        gruppo_cartelle: Lista di 6 cartelle (matrici 3x9) contenenti numeri da 1 a 90 che rispettano i vincoli forniti.

        """
       
        self.inizializza_cartelle()
        
        self.posiziona_90()

        self.assegna_posizioni()
    
        #creo un vettore con i vincoli su ogni colonna del gruppo_cartelle 
        #(nella prima colonna ci dovranno essere 9 caselle occupate per inserire i numeri da 1 a 9, nell'ultima 11 per inserire i numeri da 80 a 90)
        
        vincoli_colonne=np.array([9,10,10,10,10,10,10,10,11])

        self.swap_posizioni(vincoli_colonne)
        
        self.assegna_numeri()
                        

        
        
def genera_gruppi(lista_cartelle):
     
    """ 
    La funzione genera n gruppi utilizzando il metodo 'crea_gruppo' della classe Gruppo()
    in base a quante cartelle sono richieste dai giocatori
        
    Input
    -------
    lista_cartelle (int[]): lista dei numeri di cartelle da assegnare a ciascun giocatore
        
    Output 
    -------
    lista_cartelle_richieste (array[]) : lista di cartelle generate 
          
    """
          
          
    lista_cartelle_richieste=[]
    conteggio= math.ceil(sum(lista_cartelle)/6)
    for i in range(0,conteggio):
        g=Gruppo()
        g.crea_gruppo()
        lista_cartelle_richieste= lista_cartelle_richieste + g.gruppo_cartelle
    return lista_cartelle_richieste
          
      
     
         
                
        
        
    