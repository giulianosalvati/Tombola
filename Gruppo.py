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
        Lista di 6 cartelle(matrici 3x6) contenenti numeri da 1 a 90 rispettanti i vincoli forniti.

        """
      
        
        # Inizializzo matrici che tengono conto dei vincoli sulle righe(max 5 numeri) e  sulle colonne
        # Le righe rappresentano le cartelle a cui si fa riferimento mentre le colonne rappresentano rispettivamente la riga i-esima di ciascuna cartella (i=0,1,2) e la colonna j-esima della cartella stessa (j=0,1,2..9)

        conta_colonne=np.zeros((6,9)) 
        conta_righe=np.zeros((6,3))
        
        #Inizializzo per ciascuna cartella una matrice 3x9 di zeri e l'aggiungo nel gruppo
        for i in range(1,7):
            cartella=np.zeros((3,9))
            self.gruppo_cartelle.append(cartella)
            
        # Scelgo una cartella in maniera casuale in cui assegnare il 90 in basso a destra
        # c=random.randint(0,5) 
        
        self.inserisci_numero(5,2,8,90)
        # gruppo[c][2,8]=90
        conta_colonne[5,8]+=1 
        conta_righe[5,2]+=1
        
        
        
        # Procedo con un'assegnazione casuale dei primi 9 dei 90 totali rispettivamente sulla prima colonna di ciascuna cartella in modo random

        for i in range(1,10):
            t=random.randint(0,5) #Indice della cartella cui assegnerò il numero i
            r=random.randint(0,2) # Selezione della riga sulla prima colonna a cui assegnerò il numero i
            s=np.sum(conta_colonne[:,0])
                     
            while(self.gruppo_cartelle[t][r,0]!= i): #fintanto che non ho assegnato il numero  i
            
                if (self.gruppo_cartelle[t][r,0]==0  and conta_colonne[t,0]==0): #prima assegno assegno un numero ad almeno ogni cartella
                
                    self.inserisci_numero(t,r,0,i)
                    conta_colonne[t,0]+=1 #quando aggiungo elemento incremento il contatore sulle due matrici
                    conta_righe[t,r]+=1
                    
                elif( self.gruppo_cartelle[t][r,0]==0  and s>=6): 
                    
                    #entra in questo if quando ha assegnato un numero ad almeno ogni cartella (la somma sulla colonna è almeno 6)
                    
                    self.inserisci_numero(t,r,0,i)
                    conta_colonne[t,0]+=1
                    conta_righe[t,r]+=1
                    
                else:
                    t=random.randint(0,5)
                    r=random.randint(0,2)
                continue 
            
       
        # Procedo con un'assegnazione casuale dei rimanenti 79 numeri (da 10 a 89) sulle successive colonne
        
        for k in range(1,9):
            
            for i in range(k*10,(k+1)*10):
                
                t=random.randint(0,5) 
                r=random.randint(0,2) 
                s=np.sum(conta_colonne[:,k])
                
                while (self.gruppo_cartelle[t][r,k]!=i):
                    
                    sr=np.sum(conta_righe,1)
                    
                    
                    
                    if (self.gruppo_cartelle[t][r,k]==0 and conta_colonne[t,k]==0 and conta_righe[t,r]<4): 
                        
                        #assegno in maniera casuale riempendo prima ciascuna colonna, dato che ogni colonna deve avere almeno un numero
                        
                        self.inserisci_numero(t,r,k,i)
                        conta_colonne[t,k]+=1 
                        conta_righe[t,r]+=1
                        
                    elif (self.gruppo_cartelle[t][r,k]==0 and s>=6 and conta_righe[t,r]<4): #assegno in maniera casuale su qualsiasi riga
                    
                        self.inserisci_numero(t,r,k,i)
                        conta_colonne[t,k]+=1
                        conta_righe[t,r]+=1
                        
                    elif (conta_righe[t,r]==4 or conta_righe[t,r]==5): 
                        #se trovo una riga con 4 o con 5 numeri cerco le cartelle che hanno meno numeri, per individuare una posizione mirata
                    
                        if(s<6):
                        #se s<6 vuol dire che per quella colonna del gruppo, c'è una cartella che ha ancora la colonna vuota
                            t=np.argmin(conta_colonne[:,k]) #cerco la cartella che ha la colonna ancora vuota   
                            
                            r=np.argmin(conta_righe[t,:])
                            
                            self.inserisci_numero(t,r,k,i)
                            conta_colonne[t,k]+=1
                            conta_righe[t,r]+=1
                            
                        elif(s>=6):   
                            #in questo caso per assegnare il numero, cerco la cartella con meno numeri e su quella cartella, la riga con meno numeri
                            t=np.argmin(sr) #cerco la cartella che ha meno numeri
                          
                            r=np.argmin(conta_righe[t,:]) #la riga,di quella cartellla, che ha meno numeri tra le 3 
                          
                            if (self.gruppo_cartelle[t][r,k] != 0):
                                
                                #se individuo una posizione in cui già c'è un valore,per evitare una sovrascrittura,
                                #applico uno scambio di posizione nelle colonne precedenti e trovo una posizione libera 
                                   
                                riga= self.gruppo_cartelle[t][r,:]
                                indici=(np.argwhere(riga==0)) #trovo su quella riga gli indici liberi
                                j=len(indici)-1             
                                
                                while(self.gruppo_cartelle[t][r,k]!= i and j>=0):
                                    
                                    indexc=indici[j]
                                    #indice di colonna con cui scambiare
                                    for indexr in range(0,3):
                                        #cerco indice di riga con cui scambiare
                                        if (self.gruppo_cartelle[t][indexr,indexc]!= 0 and self.gruppo_cartelle[t][indexr,k]==0):
                                            #per fare lo scambio deve esserci un elemento in [indexr,indexc] 
                                            #e deve essere vuota la posizione in cui andrò ad inserire il nuovo elemento
                                            self.gruppo_cartelle[t][r,indexc] == self.gruppo_cartelle[t][indexr,indexc]   #scambio                  
                                            conta_righe[t,r]+=1
                                            self.inserisci_numero(t,indexr,indexc, 0) 
                                            r=indexr
                                            self.inserisci_numero(t,r,k,i) #inserisco nuovo elemento
                                            conta_colonne[t,k]+=1
                                            break
                                        
                                        else:
                                            indexr+=1
                                    j-=1 #scorro j finchè non trovo una cella con cui applicare lo scambio
                                    
                                    continue
                            else:
                                self.inserisci_numero(t,r,k,i)
                                conta_colonne[t,k]+=1
                                conta_righe[t,r]+=1 
                                                    
                    else:
                        
                        t=random.randint(0,5)
                        r=random.randint(0,2)
                    
                    continue
            
    def genera_gruppi(self,lista_cartelle):
     
      """ 
      Metodo che crea tanti gruppi tante quante sono le cartelle richieste
      
      Input
      -------
      lista cartelle richieste dalla linea di comando 
      
      Output 
      -------
      lista di cartelle aventi multipli di 6 elementi
      """
      
      
      lista_cartelle_richieste=[]
      conteggio= math.ceil(sum(lista_cartelle)/6)
      for i in range(0,conteggio):
          g=Gruppo()
          g.crea_gruppo()
          lista_cartelle_richieste= lista_cartelle_richieste + g.gruppo_cartelle
          
      
      return lista_cartelle_richieste
      
      
     
     
     
         
                
        
        
    