# -*- coding: utf-8 -*-

import olrem
from classes.transformation import Transformation

class TCPCalibDataSet:
    
    def __init__(self, positions=[], transformations={}):    
        self.positions = positions
        self.transformations = transformations
    
    def read_file(self, datafile):
        self.datafile = datafile
        RV, AB, combinations = olrem.read_pairs_and_calc_AB(self.datafile)

        self.positions = RV
        
        n_transfomations = len(AB)
        for i in range(n_transfomations):
            A, B = AB[i]
            index_tuple = combinations[i]
            t = Transformation(A, B)
            self.transformations[index_tuple] = t
    
    @property        
    def transformation_indices(self):
        return set(self.transformation.keys())
    
    def select_transformations(self, indices):
        res = {}        
        for tpl in indices:
            res[tpl] = self.transformations[tpl]
        return res

        
                
        
        