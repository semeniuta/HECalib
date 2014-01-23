# -*- coding: utf-8 -*-

'''
Remove outliers from the pairs of the (R, V) pairs
needed for further hand-eye calibration
'''

import numpy as np
from hecalibrators import calibinteract as ci

def read_pairs(pairs_datafile):
    '''
    Read data file with (R, V) pairs in Math3D format
    '''    
    pairs = np.load(pairs_datafile)
    return pairs  
    
def calc_AB(pairs):
    ''' 
    Calculate A and B matrices for each of the (R, V) pairs:
    Ai = inv(Ri-1) * Ri
    '''
    res_AB = []
    res_pairs = []
    
    n = len(pairs)
    for i in range(n-1):
        pair_0 = pairs[i]
        for j in range(i+1, n):
            pair_1 = pairs[j]
            R, V = pair_1
            Rprev, Vprev = pair_0
            A = Rprev.inverse() * R
            B = Vprev.inverse() * V
            res_AB.append((A, B))
            res_pairs.append((i, j))
    
    return res_AB, res_pairs

def read_pairs_and_calc_AB(pairs_datafile):
    ''' 
    Read the (R, V) pairs from the datafiles and calculate
    the corresponding (A, B) pairs using the specified function
    '''
    pairs = read_pairs(pairs_datafile)
    AB, AB_pairs = calc_AB(pairs)
    return pairs, AB, AB_pairs   
    
def calc_norms(AB, X, norm_func):
    ''' 
    Calculate norms for the given pairs of A and B matrices
    and the corresponding result of hand-eye calibration.
    
    The argumets are supplied in Math3D format.
    
    Returns a list of matrices [A*X - X*B] (in NumPy format) 
    and the corresponding norms. 
    '''
    
    norms = []
    matrices = []
    for A, B in AB:        
        Z1 = A * X        
        Z2 = X * B
        Z = ci.extract(Z1) - ci.extract(Z2)
        norm = norm_func(Z)
        
        norms.append(norm)
        matrices.append(Z)        
            
    return matrices, norms
    
def process_pairs(pairs, AB, AB_pairs, CalibratorClass, norm_func):

    calibres = ci.get_calibration_result(pairs, CalibratorClass)
    matrices, norms = calc_norms(AB, calibres, norm_func)
    norm_min = min(norms)
    ratios = [n/norm_min for n in norms]
    ratios_mean = np.mean(ratios)
    ratios_stdev = np.std(ratios)
    
    res_dict = {
        'class': CalibratorClass,
        'X': calibres,
        'matrices': matrices,
        'norms': norms,
        'norm_min': norm_min,
        'ratios': ratios,
        'ratios_mean': ratios_mean,
        'ratios_stdev': ratios_stdev,
        'AB_pairs': AB_pairs
    }
    
    return res_dict

    
            
