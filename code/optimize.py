# -*- coding: utf-8 -*-

import params
import olrem
import stats
import calibinteract
from park_martin_calibration import ParkMartinCalibrator
import math3d as m3d
from scipy.optimize import minimize
import numpy as np

class HandEyeOptimizer:
    
    minimization_target = 'mean' 
    opt_method = 'nelder-mead'
    
    def __init__(self, pairs, AB):
        self.pairs = pairs
        self.AB = AB
        
        pmc = ParkMartinCalibrator(pairs)
        X0 = pmc.sensor_in_flange
        
        self.XInitial = X0
        
        ''' Flatten the X matrix and take the first 12 elements 
        (excluding the first row [0, 0, 0, 1]) for their usage as
        the initial values of optimization factors '''    
        self.x0 = calibinteract.extract(X0).flatten()[:12]
        
    def perform_optimization(self, verbose=False):
        ''' 
        Conduct optimization:
            * objective function: minimize maximal norm (objective_func)
            * optimization factors: x1, x2 ... x12
        '''
        self.verbose = verbose
        res = minimize(self.objective_func, self.x0, method=self.opt_method, options={'disp': True})
        self.optimization_result = res
        self.XOptimal = m3d.Transform(self.reconstruct_matrix(res.x))

    def reconstruct_matrix(self, x):
        '''
        Reconstruct X matrix from an x array
        ([x1, x2 ... x12])    
        '''
        last_row = np.array([0, 0, 0, 1])    
        matrix = np.vstack([x.reshape((3, 4)), last_row])
        return matrix
   
    def objective_func(self, x):
        ''' 
        Calculate the maximal norm (having the set of (A, B) pairs)
        based on the provided array x  
        (flattened X matrix without the last row). 
        
        Used for optimization purposes as an objective function    
        '''
        matrix = self.reconstruct_matrix(x)
        
        X = m3d.Transform(matrix)
        matrices, norms = olrem.calc_norms(self.AB, X, params.norm_func)   

        s = stats.calc_statistics(norms)
        max_norm = s[self.minimization_target]
        
        if self.verbose:        
            min_norm = s['min']
            avg_norm = s['mean']
            norms_var = s['var']            
            print matrix
            print avg_norm, min_norm, max_norm, norms_var
        
        return max_norm

if __name__ == '__main__':
    
    ''' Open data file and calculate X matrix using ParkMartinCalibrator '''
    datafile = params.datafiles[0]
    pairs, AB, AB_pairs = olrem.read_pairs_and_calc_AB(datafile, calc_AB_func=olrem.calc_AB_ML)
    opt = HandEyeOptimizer(pairs, AB)
    opt.perform_optimization(verbose=False)
    
