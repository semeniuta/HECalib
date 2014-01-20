# -*- coding: utf-8 -*-

import olrem
from classes.position import Position
from classes.transformation import Transformation

class TCPCalibDataSet:
    
    def __init__(self):    
        self.positions = []
        self.transformations = []
    
    def read_file(self, datafile):
        self.datafile = datafile
        RV, AB, combinations = olrem.read_pairs_and_calc_AB(self.datafile)
        
        for R, V in RV:
            p = Position(R, V)
            self.positions.append(p)
        
        n_transfomations = len(AB)
        for i in range(n_transfomations):
            A, B = AB[i]
            R, V = combinations[i]
            t = Transformation(A, B, R, V)
            self.transformations.append(t)
        
                
        
        