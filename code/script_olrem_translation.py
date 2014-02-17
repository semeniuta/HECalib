# -*- coding: utf-8 -*-

'''
Idea from Schmidt et al (2003):
"Remove the positions where the changes in direction of translation of 
the robot arm are very high" (p. 6)
'''

import math
import numpy as np
import params
import olrem
import recalc
from matplotlib import pyplot as plt
from hecalibrators.park_martin_calibration import ParkMartinCalibrator as PMC
from helpers import m3dinteract as m3di
import scipy
from outliers import precision

def get_translation_vector(M):
    ''' Last column without the leading "1" '''
    return M.matrix[:-1, -1]

def calc_vector_len(vec):
    return math.sqrt(sum([el**2 for el in vec]))
    
if __name__ == '__main__':
    
    datafile = params.datafiles[0]
    pose_pairs = olrem.read_pairs(datafile)
    AB, combinations = olrem.calc_AB(pose_pairs)
    
    calib = PMC(pose_pairs)     
    X = calib.sensor_in_flange

    lengths = [calc_vector_len(get_translation_vector(A)) for A, B in AB]    
    #plt.plot(sorted(lengths))
    
    matrices, norms = olrem.calc_norms(AB, X, params.norm_func)

    top_limit = 700
    filtered_indices = recalc.filter_pairs(lengths, lambda x: x < top_limit)
    
    new_pmc = PMC(pose_pairs)
    new_pmc.update_move_pairs(filtered_indices)
    new_X = new_pmc.sensor_in_flange    
    new_matrices, new_norms = olrem.calc_norms(AB, new_X, params.norm_func)
    
    print '\nMatrix X (old):'
    print X
    print '\nMatrix X (new):'
    print new_X    
    
    '''Calculate object to base transform: R*X*inv(V) '''
    object_to_base = precision.get_oib_data(pose_pairs, X)
    object_to_base_new = precision.get_oib_data(pose_pairs, new_X)
    
    precision.print_var(object_to_base, object_to_base_new)
    precision.print_mean(object_to_base, object_to_base_new)
    
    
    
    
    
    
    
    
         
    
    
    
    