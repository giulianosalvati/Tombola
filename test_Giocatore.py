#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 11:15:07 2022

@author: giuliano
"""

import unittest
import numpy as np
from GiocodellaTombola import Cartella
from GiocodellaTombola import Giocatore


class TestGiocatore(unittest.TestCase):
   
    cartella1=Cartella.Cartella()
    cartella1.cartella= np.array([[0,10,21,38,42,0,0,0,83],[0,0,25,32,49,0,0,79,82],[1,18,0,37,0,59,61,0,0]])
    cartella2= Cartella.Cartella()
    cartella2.cartella= np.array([[0,16,24,34,48,0,0,0,85],[2,0,0,0,47,56,68,0,86],[0,14,23,0,40,0,0,70,89]])
    
    def setUp(self):
        self.a = Giocatore.Giocatore('Marta','2')
        self.a.prendi_cartella(self.cartella1)
        self.a.prendi_cartella(self.cartella2)
        
        
    def test_prendi_cartella(self):
        self.assertEqual(len(self.a.cartelle),2)
    
    def test_estrazione(self):
        self.assertFalse(self.a.controllo_numero(89))
      
    def test_controllo_vincite_ambo_e_varie(self):
        vincite=1
        self.a.controllo_numero(89)
        self.a.controllo_numero(70)
        self.assertEqual(self.a.controllo_vincite(vincite),2)
        vincite= self.a.controllo_vincite(vincite)
        self.a.controllo_numero(11)
        self.assertEqual(self.a.controllo_vincite(vincite),2)
    
    def test_controllo_vincite_terno_e_succ(self):
        self.a.controllo_numero(89)
        self.a.controllo_numero(70)
        vincite=2
        self.a.controllo_numero(23)
        self.assertEqual(self.a.controllo_vincite(vincite),3)
        vincite=self.a.controllo_vincite(vincite)
        self.a.controllo_numero(14)
        self.assertEqual(self.a.controllo_vincite(vincite),4)
        vincite=self.a.controllo_vincite(vincite)
        self.a.controllo_numero(15)
        self.assertEqual(self.a.controllo_vincite(vincite),4)
        self.a.controllo_numero(40)
        self.assertEqual(self.a.controllo_vincite(vincite),5)
        
    
    

if __name__ == '__main__':
    unittest.main()

        
        
    


        
        
