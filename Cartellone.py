#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 16:24:14 2022

@author: giuliano
"""
import numpy as np

class Cartellone:
    """
    Classe Cartellone ha l'ufficio di generare le cartelle costituenti il cartellone stesso ed
    i relativi metodi per segnalarne i numeri estratti e le eventuali vincite.
        Attributi della classe:
            - cartellone: lista inizializzata vuota che successivamente verrà riempita da 6 cartelle speciali(matrici 3x5) 
                ciascuna con opportuni multipli della sequenza  (1 2 3 4 5) o (6 7 8 9 10)
    """
    
    def __init__(self,cartellone=None):
      
        self.cartellone=[]
    
    
    def genera_cartellone(self):
        """
        Il metodo prevede la generazione di 6 cartelle speciali (matrici 3x5) che costituiscono il noto 'Cartellone' della tombola
        contenente i numeri da 1 a 90 .
        Input
        -----
        NaN
        
        Output
        ------
        Cartellone([]): lista contenente 6 cartelle (matrici 3x5) contenenti in maniera ordinata numeri da 1 a 90

        """
        # Inizializzo le cartelle (matrici 3 x 5)
        for i in range(6):
            
            cartellas=np.zeros((3,5))
            self.cartellone.append(cartellas)  
        
        #  Esplicito le prime righe rispettivamente della parte sx e dx del cartellone 
        #(corrispondenti alle prime righe delle prime due cartelle )
        sx=list((range(1,6)))
        dx=list((range(6,11)))
        
        # poichè ciascuna cartella conterra multipli di dieci delle due precedenti righe
        # il ciclo che segue andrà ad inserire i multipli in maniera opportuna nelle specifiche cartelle nella parte dx e sx del cartellone
        # si hanno 3 cartelle per lato ciascuna di 3 righe e 5 elementi
        for i in range(6):
            # se i è pari ci si riferisce alla parte sx del cartellone, nello specifico si hanno 3 cartelle ( i=0, i=2, i=4) 
            if i% 2 == 0:
                if i==0:
                    # (cartella 0 ---> 1....5; 11.....15.;21....25)
                    for riga in range(3):
                     
                        for index in range(len(sx)):
                            
                   
                            self.cartellone[i][riga][index]= sx[index]+ 10*riga
                       
                elif i == 2:
                    # (cartella 2 ---> 31....35; 41.....45.;51....55)
                    for riga in range(3):
                         
                        for index in range(len(sx)):
                       
                            self.cartellone[i][riga][index] = sx[index]+ (riga+ i+1)*10
                else:
                    # (cartella 4 ---> 61....10; 71.....20.;81....90)
                    for riga in range(3):
                         
                        for index in range(len(sx)):
                       
                            self.cartellone[i][riga][index]= sx[index]+ (riga+ i+ 2)*10
                     
                    
                 
            #Altriemnti se i è dispari, si fa riferimento alle cartelle situate nella parte sx del cartellone
            else:
                       
                if i==1:
                    
                    # (cartella 1 ---> 6....10; 16.....20.;26....30)
                      
                    for riga in range(3):
                        for index in range(len(dx)):
                            self.cartellone[i][riga][index]= dx[index] + riga*10
                 
                  
                elif i == 3:
                     # (cartella 3---> 36....40; 46.....50.;56....60)
                    for riga in range(3):
                        for index in range(len(dx)):
                            self.cartellone[i][riga][index]= dx[index] + (riga+i)*10
                       
                else:
                    # (cartella 5---> 66....70; 76.....80.;86....90)
                    for riga in range(3):
                        for index in range(len(dx)):
                            self.cartellone[i][riga][index]= dx[index] + (riga+i+1)*10
                            
    def check_estrazione_cartellone(self,numero_estratto):
       
        """
        Verifico che il cartellone abbia o meno il numero estratto in una delle sue cartelle
         
        Input:      
        ------
        numero_estratto (int) : intero estratto dal tabellone
        
        Output
        ------
        Nan
              
              
        """   

        for i in range(6):
            for riga in range (3):
                for index in range(5):
                    if self.cartellone[i][riga][index]== numero_estratto:
                        self.cartellone[i][riga][index]= -1
                        
    def check_vincite_cartellone(self,vincite):
        """
        Verifico che il cartellone abbia o meno effettuato una vincita.
         
        Input:      
        ------
        vincite (int): intero corrispondente  alla vincita alla quale si è arrivati 
        
        Output
        ------
        Nan


        """
         
        for i in range(6):
           
            if vincite==5:                              # Se è gia stata vinta la cinquina
                # vedo se si è verificata la tombola: cioe i valori nella cartella sono solo 0 e -1
                occorenze = np.unique(self.cartellone[i])
                
                if len(occorenze)==2: 
                    
                    print('Tombola!')
                    vincite = 6 
                    
                else:
                    
                    return vincite
                
            else:
                for riga in range(0,3):
                    contatore=0
                    vincita_successiva = vincite+1      
                    for colonna in range(0,5):
                        if self.cartellone[i][riga,colonna]==-1:
                            contatore=contatore+1
                    if contatore == vincita_successiva:
                        vincite = vincita_successiva
                        
                        if vincite==2 :
                            print('Il cartellone ha fatto Ambo')
                            return vincite  
                        
                        elif vincite==3 :
                            print('Il cartellone ha fatto Terna')
                            return vincite  
                            
                        elif vincite==4 :
                            print('Il cartellone ha fatto  Quaterna')
                            return vincite  
                            
                        elif vincite==5 :
                            print('Il cartellone ha fatto Cinquina')
                            return vincite
             
            return vincite
        
    
                 
                        
        
    
       
            
            