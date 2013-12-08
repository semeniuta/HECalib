# -*- coding: utf-8 -*-

import numpy as np
import math3d as m3d
from park_martin_calibration import ParkMartinCalibrator
from tsai_lenz_calibration import TsaiLenzCalibrator
from os.path import join as opj
from cvfunctions.output import create_histogram

datadir = r'../data'
calibrator_classes = [ParkMartinCalibrator, TsaiLenzCalibrator]

def extract(orig):
    '''
    Extracts a transformation matrix (A or B)
    originally stored in the weird format (math3d?)
    '''
    rot_matrix = orig.matrix
    return np.array(rot_matrix)    

def calc_AB(pairs_plain):
    res_AB = []

    for i in range(len(pairs_plain) - 1):
        R, V = pairs_plain[i]
        Rnext, Vnext = pairs_plain[i+1]
        
        ''' or maybe vice versa '''        
        A = np.linalg.inv(R) * Rnext
        B = np.linalg.inv(V) * Vnext

        res_AB.append((A, B))

    return res_AB
    

def calc_norms(AB, res_plain, verbose=False):
    ''' ||AX - XB|| '''
    
    norms = []
    matrices = []
    for A, B in AB:
        X = res_plain    
        M = A*X - X*B
        norm = np.linalg.norm(M, ord=-1)
        
        norms.append(norm)
        matrices.append(M)        
        
        if verbose:
            print M            
            print norm
            
    return matrices, norms
    
def make_histograms(big_res):
    for r in big_res:
        norms = r['norms']
        create_histogram(norms, 20)

if __name__ == '__main__':
    pairs = np.load(opj(datadir, '20131114121046.npy'))
    pairs_plain = [[extract(m1), extract(m2)] for m1, m2 in pairs]
    AB = calc_AB(pairs_plain)
    
    big_res = []
    for CalibratorClass in calibrator_classes:
        calibrator = CalibratorClass(pairs)
        res = calibrator.sensor_in_flange
        res_plain = extract(res)    
        matrices, norms = calc_norms(AB, res_plain, verbose=False)

        for_current_method = {
            'res': res,
            'res_plain': res_plain,
            'matrices': matrices,
            'norms': norms        
        }
        
        big_res.append(for_current_method)
    
    ''' Show histograms '''
    #make_histograms(big_res)    
    
    ''' Analyze sample A and B '''
    A, B = AB[0]
    R, V = pairs_plain[0]
    Rnext, Vnext = pairs_plain[1]
    
    print R
    print Rnext
    print A
        


    
    
    
