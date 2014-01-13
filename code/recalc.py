# -*- coding: utf-8 -*-

''' 
Recalculate the calibration results using ParkMartinCalibrator
after removing outliners
'''

import numpy as np

def recalculate_X(pmc, good_indices):
    pmc._invalidate()
    update_move_pairs(pmc, good_indices)
    new_X = pmc.sensor_in_flange
    return new_X
    
def update_move_pairs(pmc, good_indices):
    move_pairs = list(pmc._move_pairs)
    good_move_pairs = []
    for ind in good_indices:
        good_move_pairs.append(move_pairs[ind])
    pmc._move_pairs = np.array(good_move_pairs)
    

        
        
        
        
    