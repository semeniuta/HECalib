# -*- coding: utf-8 -*-

import params
import olrem
from park_martin_calibration import ParkMartinCalibrator
import math3d as m3d
from scipy.optimize import minimize
import numpy as np

class HandEyeOptimizer:
    
    def __init__(self, pairs, AB):
        self.pairs = pairs
        self.AB = AB
        
    def perform_optimization():

def reconstruct_matrix(x):
    '''
    Reconstruct X matrix from an x array
    ([x1, x2 ... x12])    
    '''
    last_row = np.array([0, 0, 0, 1])    
    matrix = np.vstack([x.reshape((3, 4)), last_row])
    return matrix

def calc_max_norm(x):
    ''' 
    Calculate the maximal norm (having the set of (A, B) pairs)
    based on the provided array x  
    (flattened X matrix without the last row). 
    
    Used for optimization purposes as an objective function    
    '''
    matrix = reconstruct_matrix(x)
    
    X = m3d.Transform(matrix)
    matrices, norms = olrem.calc_norms(AB, X, params.norm_func)   
    avg_norm, min_norm, max_norm, norms_var = olrem.calc_norms_distribution_parameters(norms)
    print matrix
    print avg_norm, min_norm, max_norm, norms_var
    return max_norm

if __name__ == '__main__':
    
    ''' Open data file and calculate X matrix using ParkMartinCalibrator '''
    datafile = params.datafiles[0]
    pairs, AB, AB_pairs = olrem.read_pairs_and_calc_AB(datafile)
    pmc = ParkMartinCalibrator(pairs)
    X0 = pmc.sensor_in_flange
    
    ''' Flatten the X matrix and take the first 12 elements 
     (excluding the first row [0, 0, 0, 1]) for their usage as
     the initial values of optimization factors '''    
    x0 = olrem.extract(X0).flatten()[:12]
    
    ''' 
    Conduct optimization:
        * objective function: minimize maximal norm (calc_max_norm)
        * optimization factors: x1, x2 ... x12
    '''
    res = minimize(calc_max_norm, x0, method='nelder-mead', options={'disp': True})
    
    ''' Reconstruct the X matrix from the optimized x values '''
    X = reconstruct_matrix(res.x)
    
