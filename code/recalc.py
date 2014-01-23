# -*- coding: utf-8 -*-

''' 
Recalculate the calibration results using ParkMartinCalibrator
after removing outliers
'''
    
def filter_pairs(norms, criterion):
    accepted_indices = []    
    for i in range(len(norms)):
        norm = norms[i]
        if criterion(norm):
            accepted_indices.append(i)
    return accepted_indices

def create_filtering_criterion(top_limit):
    return lambda norm: norm < top_limit
        
        
        
        
    