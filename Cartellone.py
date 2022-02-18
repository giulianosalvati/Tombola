#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 16:24:14 2022

@author: giuliano
"""
import numpy as np
import math

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
        Il metodo prevede la generazione di 6 cartelle speciali (matrici 3x5) che 
        costituiscono il noto 'Cartellone' della tombola contenente i numeri da 1 a 90 .
        
        Input
        -----
        NaN
        
        Output
        ------
        NaN
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
                       
                            self.cartellone[i][riga][index] = sx[index]+ (riga+ i+ 2)*10
                     
                    
                 
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
        Il metodo 'segnato' il numero estratto nella cartella del cartellone che 
        lo contine, ponendolo a -1
         
        Input:      
        ------
        numero_estratto (int) : intero estratto dal tabellone
        
        Output
        ------
        index_cartella (int): indice della cartella del cartellone che contiene il numero estratto
              
              
        """   
        decina_numero = numero_estratto//10
        riga_cartella=math.trunc(decina_numero/3) # Pensando al cartellone reale quindi formato da 3x2 cartelle, 
                                                    # questo valore indica la riga in cui è posizionata la cartella
                                                    # rispetto al cartellone
        unita_numero = numero_estratto%10
        sx=list((range(1,6)))
        if riga_cartella == 0:
            if unita_numero in sx:
                index_cartella = 0
            else:
                index_cartella = 1
        if riga_cartella == 1:
           if unita_numero in sx:
               index_cartella = 2
           else:
               index_cartella = 3
        if riga_cartella == 2:
            if unita_numero in sx:
                index_cartella = 4
            else:
                index_cartella = 5
                
        for riga in range (3):
            for colonna in range(5):
                if self.cartellone[index_cartella][riga][colonna]== numero_estratto:
                    self.cartellone[index_cartella][riga][colonna]= -1
        return index_cartella
    
    def check_vincite_cartellone(self,vincite,index_cartella):
        """
        Verifico che il cartellone abbia o meno effettuato una vincita, nella
        cartella che conteneva l'ultimo numero estratto
         
        Input:      
        ------
        vincite (int): intero corrispondente  alla vincita alla quale si è arrivati 
        index_cartella (int): indice della cartella del cartellone che conteneva il numero estratto
                              e quindi l'unica per cui è necessario il check delle vincite nel cartellone
        
        Output
        ------
        vincite (int): variabile di ingresso aggiornata


        """
        if vincite==5:   # Se è gia stata vinta la cinquina
               # vedo se si è verificata la tombola: cioe i valori nella cartella 
               # sono solo 0 e -1                           
            occorenze = np.unique(self.cartellone[index_cartella])
                
            if len(occorenze)==2: 
                print('\nIl cartellone ha fatto tombola!')
                vincite = 6 
                    
            else:
                    
                return vincite
                
        else:
            for riga in range(0,3):
                contatore=0
                vincita_successiva = vincite+1      
                for colonna in range(0,5):
                    if self.cartellone[index_cartella][riga,colonna]==-1:
                        contatore=contatore+1
                if contatore == vincita_successiva:
                    vincite = vincita_successiva
                    if vincite==2 :
                        print('\nIl cartellone ha fatto ambo')
                        return vincite  
                        
                    elif vincite==3 :
                        print('\nIl cartellone ha fatto terna')
                        return vincite  
                            
                    elif vincite==4 :
                        print('\nIl cartellone ha fatto quaterna')
                        return vincite  
                    
                    elif vincite==5 :
                        print('\nIl cartellone ha fatto cinquina')
                        return vincite      
        return vincite
        
    def elemento_cartella_cartellone(self,i,index_riga,index_colonna):
        """
        Il metodo restituisce l'elemento della cartella i-esima del cartellone
        nella posizione [index_riga,ondex_colonna].
    
        Input
        -----
        i (int) : indice della cartella del cartellone
        index_riga (int): indice riga della posizione
        index_colonna (int ): indice colonna della posizione
        
        Output
        ------
        elem (int): l'elemento della cartella nella posizione [index_riga,ondex_colonna]
        che puo essere:
            -1 se il valore in quella casella è stato estratto
            oppure un valore da 1 a 90 
                        
            
        """
        elem = self.cartellone[i][index_riga,index_colonna]
        return elem
            
    
                 
                        
        
    
       
            
            