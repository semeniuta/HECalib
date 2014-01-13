# -*- coding: utf-8 -*-

'''
Process several data files 
(calculate calibration results, norms and other parameters)
'''

import params
import olrem
import os
import resprocess

def read_and_process_pairs_for_different_calibrators(datafile):
    pairs, AB, AB_pairs = olrem.read_pairs_and_calc_AB(datafile)
    
    res = []
    for CalibratorClass in params.calibrator_classes:
        res_dict = olrem.process_pairs(pairs, AB, AB_pairs, CalibratorClass, params.norm_func)
        res.append(res_dict)    
    
    return pairs, AB, res

