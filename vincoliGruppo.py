# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 15:53:16 2022

@author: Marco
"""

import random 
import numpy as np

gruppo={}
conta_colonne=np.zeros((6,9)) #matrice in cui le righe sono le cartelle mentre le colonne sono le colonne di ciascuna cartella, gli elementi della matrice
#sono il numero di elementi diversi da zero su quella colonna
conta_righe=np.zeros((6,3))   # come prima ma le colonne sono le righe di ciascuna cartella

for i in range(1,7):
    cartella=np.zeros((3,9))
    gruppo[f'cartella{i}']=cartella

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

for k in range(1,8):
    for i in range(k*10,(k+1)*10):
        t=random.randint(1,6) 
        r=random.randint(0,2) 
        s=np.sum(conta_colonne[0:6,k])
        
        while(gruppo[f'cartella{t}'][r,k]!=i):
            if (gruppo[f'cartella{t}'][r,k]==0 and conta_colonne[t-1,k]==0):
                gruppo[f'cartella{t}'][r,k]=i
                conta_colonne[t-1,k]+=1 
                conta_righe[t-1,r]+=1
            elif(gruppo[f'cartella{t}'][r,k]==0 and s>=6):        
                gruppo[f'cartella{t}'][r,k]=i
                conta_colonne[t-1,k]+=1
                conta_righe[t-1,r]+=1
            else:
                t=random.randint(1,6)
                r=random.randint(0,2)
            continue        

for i in range(80,91):
    t=random.randint(1,6) 
    r=random.randint(0,2) 
    s=np.sum(conta_colonne[0:6,8])
    
    while(gruppo[f'cartella{t}'][r,8]!=i):
        if (gruppo[f'cartella{t}'][r,8]==0 and conta_colonne[t-1,8]==0):
            gruppo[f'cartella{t}'][r,8]=i
            conta_colonne[t-1,8]+=1 
            conta_righe[t-1,r]+=1
        elif(gruppo[f'cartella{t}'][r,8]==0 and s>=6):        
                gruppo[f'cartella{t}'][r,8]=i
                conta_colonne[t-1,8]+=1
                conta_righe[t-1,r]+=1    
        else:
            t=random.randint(1,6)
            r=random.randint(0,2)
        continue