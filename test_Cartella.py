#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 19:38:01 2022

@author: giuliano
"""
import unittest
import numpy as np
from GiocodellaTombola.Cartella import Cartella

class TestCartella(unittest.TestCase):
    
    
    def setUp(self):
        self.a = Cartella()
        self.a.inserisci_numero(0,0,1)
    
    def tearDown(self):
        pass
    
   
    def test_inserisci_num_e_controlla_righe_colonne(self):
        self.assertEqual(self.a.conta_colonne[0], 1)
        self.assertEqual(self.a.conta_righe[0], 1)
    
    def test_inserisci_num_e_check_posizione_occupata(self):
        self.assertTrue(self.a.posizione_occupata(0,0))
      
    
    def test_inserisci_num_e_check_posizione_libera(self):
        self.a.inserisci_numero(0,0,1)
        self.assertFalse(self.a.posizione_libera(0,0))
    
    def test_vincolo_righe_e_posizioni(self):
        self.assertTrue(self.a.verifica_vincolo_righe(0))
        self.assertEqual(self.a.elemento_cartella(0,0),1)
        self.assertTrue(self.a.posizione_occupata(0, 0))
        self.assertFalse(self.a.posizione_libera(0, 0))
        self.a.elimina_numero(0, 0)
        self.assertTrue(self.a.verifica_vincolo_righe(0))
        self.assertEqual(self.a.elemento_cartella(0,0),0)
        self.assertFalse(self.a.posizione_occupata(0, 0))
        self.assertTrue(self.a.posizione_libera(0, 0))
        
    def test_estrazione(self):
        np.array_equal(self.a.estrai_colonna(0), self.a.cartella[:,0])
        np.array_equal(self.a.estrai_riga(0), self.a.cartella[0,:])
        
    def test_inserisci_num_e_check_num_estratto(self):
        self.a.inserisci_numero(0,0,-1)
        self.assertTrue(self.a.numero_gia_estratto(0,0))
    

if __name__ == '__main__':
    unittest.main()
