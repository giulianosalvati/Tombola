# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 12:53:24 2022

@author: Marco
"""

import random 
import numpy as np
import math


def crea_gruppi(lista_cartelle):
    lista_gruppi = []
    num_gruppi_necessari = math.ceil(sum(lista_cartelle)/6)
    
    for g in range(1,num_gruppi_necessari+1):
        gruppo={}
        conta_colonne=np.zeros((6,9)) #matrice in cui le righe sono le cartelle mentre le colonne sono le colonne di ciascuna cartella, gli elementi della matrice
        #sono il numero di elementi diversi da zero su quella colonna
        conta_righe=np.zeros((6,3))   # come prima ma le colonne sono le righe di ciascuna cartella
        
        for i in range(1,7):
            cartella=np.zeros((3,9))
            gruppo[f'cartella{i}']=cartella
            
        c=random.randint(1,6) #scelgo una cartella in maniera casuale in cui assegnare il 90 in basso a destra
        gruppo[f'cartella{c}'][2,8]=90
        conta_colonne[c-1,8]+=1 
        conta_righe[c-1,2]+=1
        
        for i in range(1,10):
            t=random.randint(1,6) #cartella a cui assegno il numero i
            r=random.randint(0,2) #riga della prima colonna a cui assegno il numero i
            s=np.sum(conta_colonne[0:6,0])
                     
            while(gruppo[f'cartella{t}'][r,0]!=i): #fintanto che non ho assegnato il numero  i
                if (gruppo[f'cartella{t}'][r,0]==0 and conta_colonne[t-1,0]==0): #prima assegno assegno un numero ad almeno ogni cartella
                    gruppo[f'cartella{t}'][r,0]=i
                    conta_colonne[t-1,0]+=1 #quando aggiungo elemento incremento il contatore sulle due matrici
                    conta_righe[t-1,r]+=1
                elif(gruppo[f'cartella{t}'][r,0]==0 and s>=6): 
                    #entra in questo if quando ha assegnato un numero ad almeno ogni cartella (la somma sulla colonna è almeno 6)
                    gruppo[f'cartella{t}'][r,0]=i
                    conta_colonne[t-1,0]+=1
                    conta_righe[t-1,r]+=1
                else:
                    t=random.randint(1,6)
                    r=random.randint(0,2)
                continue        
        
        for k in range(1,9):
            for i in range(k*10,(k+1)*10):
                t=random.randint(1,6) 
                r=random.randint(0,2) 
                s=np.sum(conta_colonne[0:6,k])
                
                while(gruppo[f'cartella{t}'][r,k]!=i):
                    sr=np.sum(conta_righe,1)
                    if (gruppo[f'cartella{t}'][r,k]==0 and conta_colonne[t-1,k]==0 and conta_righe[t-1,r]<4): 
                        #assegno in maniera casuale riempendo prima ciascuna colonna
                        gruppo[f'cartella{t}'][r,k]=i
                        conta_colonne[t-1,k]+=1 
                        conta_righe[t-1,r]+=1
                    elif(gruppo[f'cartella{t}'][r,k]==0 and s>=6 and conta_righe[t-1,r]<4): #assegno in maniera casuale       
                        gruppo[f'cartella{t}'][r,k]=i
                        conta_colonne[t-1,k]+=1
                        conta_righe[t-1,r]+=1
                    elif(conta_righe[t-1,r]==4 or conta_righe[t-1,r]==5): #cerco le cartelle che hanno meno numeri
                        if(s<6):
                            g=np.argmin(conta_colonne[0:6,k]) #cerco la cartella che ha la colonna ancora vuota   
                            t=g+1
                            l=np.argmin(conta_righe[t-1,0:3])
                            r=l
                            gruppo[f'cartella{t}'][r,k]=i
                            conta_colonne[t-1,k]+=1
                            conta_righe[t-1,r]+=1
                        elif(s>=6):      
                            j=np.argmin(sr) #cerco la cartella che ha meno numeri
                            t=j+1
                            l=np.argmin(conta_righe[t-1,0:3]) #la riga,di quella cartellla, che ha meno numeri tra le 3 
                            r=l
                            if(gruppo[f'cartella{t}'][r,k]!=0):
                                #se individuo una posizione in cui già c'è un valore applico uno scambio di posizione nelle colonne precedenti
                                #e trovo una posizione libera per evitare una sovrascrittura
                                riga=gruppo[f'cartella{t}'][r,0:k]
                                indici=(np.argwhere(riga==0))
                                j=len(indici)-1                      
                                while(gruppo[f'cartella{t}'][r,k]!=i and j>=0):
                                    indexc=indici[j]
                                    for indexr in range(0,3):
                                        if(gruppo[f'cartella{t}'][indexr,indexc]!=0 and gruppo[f'cartella{t}'][indexr,k]==0):
                                           gruppo[f'cartella{t}'][r,indexc]=gruppo[f'cartella{t}'][indexr,indexc]                     
                                           conta_righe[t-1,r]+=1
                                           gruppo[f'cartella{t}'][indexr,indexc]=0    
                                           r=indexr
                                           gruppo[f'cartella{t}'][r,k]=i
                                           conta_colonne[t-1,k]+=1
                                           break
                                        else:
                                           indexr+=1
                                    j-=1
                                    continue
                            else:
                                gruppo[f'cartella{t}'][r,k]=i
                                conta_colonne[t-1,k]+=1
                                conta_righe[t-1,r]+=1 
                                                    
                    else:
                        t=random.randint(1,6)
                        r=random.randint(0,2)
                    continue
        lista_gruppi.append(gruppo)
    return lista_gruppi
            
