#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 12:16:53 2022

@author: giuliano

"""

import math
import random 
import Cartella
import numpy as np


class Gruppo:
    
    """
    Classe Gruppo fornisce in uscita una lista di 6 cartelle (1 gruppo) che soddisfa i vincoli preposti.
        Attributo della classe:
            - gruppo_cartelle:lista inizializzata vuota che verrà successivamente riempita con 6 cartelle (matrici 3x9 ciascuna)
                              costituenti un gruppo di cartelle rispettante i vincoli sulle colonne e sulle righe.

    """
    
    # Variabile globale che corrisponde alla cartella scelta in maniera soggettiva a cui verrà assegnato il numero 90 rispettando i vincoli
    posizione_scelta=5 
    
    def __init__(self,gruppo_cartelle=None,cartellone=None):
        
        self.gruppo_cartelle=[]
        self.cartellone=[]
        
   
    def inizializza_cartelle(self):
       
        """
        Inizializzazione del gruppo di 6 cartelle costituenti il gruppo
        
        Input
        -----
        NaN
        
        Output
        ------
        NaN
        
        """
        for i in range(0,6):
            cartella= Cartella.Cartella()
            self.gruppo_cartelle.append(cartella)
            
    def svuota_gruppo(self):
        """
        Metodo che azzera tutti gli elementi delle cartelle del gruppo_cartelle e i contatori

        Input
        -------
        Nan
        Output
        ------
        NaN
        
        """
        for i in range(0,6):
            self.gruppo_cartelle[i].svuota_cartella()
    
    
    def posiziona_90(self):
        
        """
        Il numero 90, come imposto dai vincoli, viene collocato in basso a dx 
        nella cartella indetta dalla variabile globale (ultima cartella)
        
        Input
        -----
        NaN
        
        Output
        ------
        NaN

        """
        
        self.gruppo_cartelle[self.posizione_scelta].inserisci_numero(2,8,90)
        
   
    def assegna_posizioni(self):
       
        """
        Metodo che assegna 1 in posizioni tali da rispettare i vincoli sulle righe
       
        Input
        -----
        NaN
        
        Output
        ------
        NaN
        
        """
        
        
        # assegno almeno un 1 su ciascuna colonna di ciascuna cartella, scegliendo casualmente la riga (occupando 54 caselle) 
        
        for i in range(0,6):
            for j in range(0,9):
                if(i== self.posizione_scelta and j==8): #su questa colonna già c'è almeno un numero, ovvero 90 (non devo riassegnarlo)
                    pass
                else:
                    r=random.randrange(3)
                    while not self.gruppo_cartelle[i].verifica_vincolo_righe(r): #nell'estrazione random tengo conto del vincolo sulle righe: se ho già 5 elementi su una riga ne devo estrarre un'altra
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
        
                        
    def somma_colonneGruppo(self):
        """
        Il seguente metodo conta la somma degli elementi presenti su ciascuna colonna del gruppo_cartelle

        Input
        ------
        Nan
        
        Output
        ------
        somma_colonne(array[]) è un vettore che contiene il numero totale delle caselle occupate per ciascuna colonna del gruppo_cartelle
        """
        somma_colonne=np.zeros(9)
        for c in range(0,6):
            for colonna in range(0,9):
                somma_colonne[colonna] += self.gruppo_cartelle[c].conta_colonne[colonna] 
        return somma_colonne
    
    def controllo_vincoli_colonne(self, vincoli):
        """
        Metodo che controlla se sono rispettati i vincoli su ciascuna colonna del gruppo_cartelle

        Input
        -----
        vincoli (array[]): lista contenente 9 elementi ciascuno corrispondente al numero massimo di elementi di ciascuna colonna del gruppo

        Output
        ------
        boolean : indica se i vincoli su ciascuna colonna del gruppo_cartelle sono rispettati
                  -True se sono rispettati, -False altrimenti

        """
        somma_colonne=self.somma_colonneGruppo()
        if np.array_equal(somma_colonne, vincoli): #array_equal restituisce True se i due vettori che riceve in ingresso sono uguali, False altrimenti
           return True
        else:
            return False
    
    
    def swap_posizioni(self,vincoli):
        
        """
        
        Il seguente metodo permette un controllo riga per riga, considerando 
        i vincoli sulle colonne, in maniera tale da effettuare, al fine di 
        rispettare questi ultimi, uno swap tra opportuni posizionamenti.

        Input
        ----------
        vincoli (array[]): lista contenente 9 elementi ciascuno corrispondente al numero massimo di elementi di ciascuna colonna del gruppo

        Output
        -------
        NaN

        """
      
        
        for i in range(0,6): 
            for r in range(0,3):
                if self.controllo_vincoli_colonne(vincoli): #se restituisce True il ciclo può terminare perchè vuol dire che i vincoli sono già rispettati e quindi non sono più necessari altri swap
                    break
                riga = self.gruppo_cartelle[i].estrai_riga(r)
                indici_occupati= np.argwhere(riga==1) #trovo indici delle caselle occupate su quella riga
                for k in indici_occupati:
                    somma_colonne=self.somma_colonneGruppo()
                    if(somma_colonne[k]>vincoli[k] and self.gruppo_cartelle[i].conta_colonne[k]>1):
                        indici_vuoti=np.argwhere(riga==0)
                        differenza= vincoli[indici_vuoti]-somma_colonne[indici_vuoti]
                        colonna_min=np.argmax(differenza) #scelgo la colonna in cui la differenza tra vincoli e s_colonne è massima
                        swap=indici_vuoti[colonna_min]
                        self.gruppo_cartelle[i].elimina_numero(r,k)
                        self.gruppo_cartelle[i].inserisci_numero(r,swap,1) #applico lo swap e aggiorno i contatori

        
    def assegna_numeri(self):
        
        """
        Collocazione dei numeri da 1 a 90 nelle posizioni individuate 
        (sostituisco gli uni presenti nelle 6 cartelle)
        
        Input
        -----
        NaN
        
        Output
        ------
        NaN
        
        """
        # Dopo aver trovato le posizioni assegno i numeri da 1 a 90, in maniera casuale nelle posizioni individuate nel gruppo_cartelle
                   
        # Inizio con la prima colonna del gruppo, assegnando i numeri da 1 a 9
        estratti=[]
        for i in range(0,6):
            self.gruppo_cartelle[i].azzera_contatori()
            self.gruppo_cartelle[self.posizione_scelta].aggiorna_conteggio(2,8) #aggiorno il contatore per 90 che non viene inserito in questa fase
            colonna= self.gruppo_cartelle[i].estrai_colonna(0)
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
                colonna=self.gruppo_cartelle[i].estrai_colonna(k)
                pos_occ=np.argwhere(colonna==1)
                for j in pos_occ:
                    n=random.randrange(k*10,(k+1)*10)
                    while n in estratti:
                        n=random.randrange(k*10,(k+1)*10)
                    self.gruppo_cartelle[i].inserisci_numero(int(j),k,n)
                    estratti.append(n)
   
        
    
    def crea_gruppo(self):
        
        """
        Implementazione del gruppo di 6 cartelle (matrici 3x9) contenenti 
        numeri da 1 a 90 che rispettano i vincoli forniti.
        
        Input
        -----
        NaN
        
        Output
        ------
        NaN
        
        """
        
        
        self.inizializza_cartelle()
        
        #creo un vettore rappresentativo dei vincoli su ogni colonna del gruppo_cartelle 
        #(nella prima colonna ci dovranno essere 9 caselle occupate per inserire i numeri da 1 a 9, dalla seconda alla punultima le caselle 
        # da occupare sono 10, nell'ultima 11 per inserire i numeri da 80 a 90)
        
        vincoli_colonne=np.array([9,10,10,10,10,10,10,10,11])

        controllo_superato=False
        
        while not controllo_superato: #il ciclo termina solo quando effettivamente il gruppo rispetta i vincoli
            
            self.svuota_gruppo()
            
            self.posiziona_90()
    
            self.assegna_posizioni()
    
            self.swap_posizioni(vincoli_colonne)
            
            controllo_superato=self.controllo_vincoli_colonne(vincoli_colonne)
        
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
          

                
        
        
    