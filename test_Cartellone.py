#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 22:20:51 2022

@author: giuliano
"""

import unittest
from GiocodellaTombola.Cartellone import Cartellone

class TestCartellone(unittest.TestCase):
    
    def setUp(self):
        self.a = Cartellone()
        self.a.genera_cartellone()
        
        
    def test_generazione(self):
        self.assertEqual(len(self.a.cartellone),6)
    
    def test_segna_numero(self):
        self.assertEqual(self.a.check_estrazione_cartellone(60),3)

if __name__ == '__main__':
    unittest.main()







                         