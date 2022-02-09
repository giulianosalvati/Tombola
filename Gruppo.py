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
import numpy as np


class Gruppo:
    
    def __init__(self,gruppo_cartelle=None):
        
        self.gruppo_cartelle=[]
        
    def inserisci_numero(self,index_cartella,riga,colonna,numero):
        
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
        self.gruppo_cartelle[index_cartella][riga,colonna]= numero
    
    def elimina_numero(self,index_cartella,riga,colonna):
        
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
        self.gruppo_cartelle[index_cartella][riga,colonna]=0
    
   
        
    
    def crea_gruppo(self):
        """
        Implementazione del gruppo di 6 cartelle
        
        Input
        -------
        Nan.
       

        Returns
        -------
        gruppo_cartelle: Lista di 6 cartelle (matrici 3x9) contenenti numeri da 1 a 90 che rispettano i vincoli forniti.

        """
        # Inizializzo 2 matrici, conta_colonne (6,9) e conta_righe(6,3), che conteranno il numero di caselle occupate in ogni cartella, da utilizzare per verificare che i vincoli sulle righe(max 5 numeri) e sulle colonne siano rispettati
        # Nelle 2 matrici le righe i rappresentano le cartelle a cui si fa riferimento mentre le colonne rappresentano rispettivamente:
        #in conta_colonne(i,j): la colonna j-esima della cartella i-esima (j=0,1,2..9)
        #in conta_righe(i,r): la riga r-esima di ciascuna cartella i (r=0,1,2)
        conta_colonne=np.zeros((6,9)) 
        conta_righe=np.zeros((6,3))

        #Inizializzo le 6 matrici cartella della lista gruppo_cartelle
        for i in range(0,6):
            cartella=np.zeros((3,9))
            self.gruppo_cartelle.append(cartella)
    
        #assegno come posizione del numero novanta, l'ultima colonna dell'ultima riga dell'ultima cartella
        pos_novanta=5
        self.inserisci_numero(pos_novanta,2,8,90)
        conta_colonne[pos_novanta][8]+=1
        conta_righe[pos_novanta][2]+=1

        #step 1: assegno in modo random un 1 alle caselle da occupare in ciascuna cartella, rispettando i vincoli
       
        #step 1.1: assegno almeno un 1 su ciascuna colonna di ciascuna cartella, scegliendo casualmente la riga (occupando 54 caselle) 
        for i in range(0,6):
            for j in range(0,9):
                if(i==pos_novanta and j==8): #su questa colonna già c'è almeno un numero che è 90 (non devo riassegnarlo)
                    pass
                else:
                    r=random.randrange(3)
                    while conta_righe[i][r]==5: #nell'estrazione random tengo conto del vincolo sulle righe: se ho già 5 elementi su una riga ne devo estrarre un'altra
                        r=random.randrange(3)
                    self.inserisci_numero(i,r,j,1)
                    conta_colonne[i][j]+=1
                    conta_righe[i][r]+=1
        
        #step 1.2: occupo le restanti 36 caselle in maniera casuale, rispettando però i vincoli sulle righe ed evitando sovrascritture
        for k in range(0,36):
            i=random.randrange(6)
            j=random.randrange(9)
            r=random.randrange(3)
            while conta_righe[i][r]==5 or self.gruppo_cartelle[i][r][j]!=0:
                i=random.randrange(6)
                j=random.randrange(9)
                r=random.randrange(3)
            self.inserisci_numero(i,r,j,1)
            conta_colonne[i][j]+=1
            conta_righe[i][r]+=1
    
        #creo un vettore con i vincoli su ogni colonna del gruppo_cartelle 
        #(nella prima colonna ci dovranno essere 9 caselle occupate per inserire i numeri da 1 a 9, nell'ultima 11 per inserire i numeri da 80 a 90)
        vincoli=[9,10,10,10,10,10,10,10,11]
        vincoli=np.array(vincoli)

        #step 1.3: controllo, procedendo riga per riga, quali colonne del gruppo_cartelle superano il vincolo e applico uno swap mirato
        #andando ad individuare la colonna, con casella vuota sulla riga in esame, più lontana dal rispettare il vincolo.
        for i in range(0,6): 
            for r in range(0,3):
               riga=self.gruppo_cartelle[i][r]
               indici_occ=np.argwhere(riga==1) #trovo indici delle caselle occupate su quella riga
               for k in indici_occ:
                   s_colonne=np.sum(conta_colonne,0) # è un vettore che contiene il numero totale delle caselle occupate per ciascuna colonna del gruppo_cartelle
                   if(s_colonne[k]>vincoli[k] and conta_colonne[i,k]>1):
                       indici_vuoti=np.argwhere(riga==0)
                       differenza=vincoli[indici_vuoti]-s_colonne[indici_vuoti]
                       colonna_min=np.argmax(differenza) #scelgo la colonna in cui la differenza tra vincoli e s_colonne è massima
                       swap=indici_vuoti[colonna_min]
                       self.elimina_numero(i,r,k)
                       conta_colonne[i][k]-=1
                       self.inserisci_numero(i,r,swap,1) #applico lo swap e aggiorno i contatori
                       conta_colonne[i][swap]+=1

        #step 2: dopo aver trovato le posizioni assegno i numeri da 1 a 90, in maniera casuale nelle posizioni individuate nel gruppo_cartelle
                   
        #inizio con la prima colonna del gruppo, assegnando i numeri da 1 a 9
        estratti=[]
        for i in range(0,6):
            colonna=self.gruppo_cartelle[i][:,0] 
            #individuo sulla colonna della singola cartella quali sono le posizioni occupate a cui devo assegnare un numero da 1 a 9
            pos_occ=np.argwhere(colonna==1) 
            for j in pos_occ:
                n=random.randrange(1,10) #estraggo un numero a caso tra 1 e 9 che non sia già stato estratto
                while n in estratti:
                    n=random.randrange(1,10)
                self.inserisci_numero(i,int(j),0,n)
                estratti.append(n)
                           
        #continuo con le restanti colonne
        for k in range(1,9):
            estratti=[]
            for i in range(0,6):
                colonna=self.gruppo_cartelle[i][:,k]
                pos_occ=np.argwhere(colonna==1)
                for j in pos_occ:
                    n=random.randrange(k*10,(k+1)*10)
                    while n in estratti:
                        n=random.randrange(k*10,(k+1)*10)
                    self.inserisci_numero(i,int(j),k,n)
                    estratti.append(n)
        

     
def genera_gruppi(lista_cartelle):
     
    """ 
    La funzuine genera n gruppi utilizzando il metodo 'crea_gruppo' della classe Gruppo()
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
          
      
     
         
                
        
        
    