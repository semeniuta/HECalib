# -*- coding: utf-8 -*-

'''
Process several data files 
(calculate calibration results, norms and other parameters)
'''

import diffcalib
import params
import os
import resprocess
import olrem

def read_and_process_pairs_for_different_calibrators(datafile):
    pairs, AB, AB_pairs = olrem.read_pairs_and_calc_AB(datafile)
    
    res = []
    for CalibratorClass in params.calibrator_classes:
        res_dict = olrem.process_pairs(pairs, AB, AB_pairs, CalibratorClass, params.norm_func)
        res.append(res_dict)    
    
    return pairs, AB, res


if __name__ == '__main__':
    results = {}   
    for f in params.datafiles:
        pairs, AB, res = diffcalib.read_and_process_pairs_for_different_calibrators(f)   
        fname = os.path.basename(f)        
        results[fname] = res 
               
        print 'Results of processing data from %s' % fname
        print res[0]['X']
        print res[1]['X']
        
#        resprocess.print_res(res)
#        r_pm, r_tl = resprocess.sort_by_ratios(res)
#        print r_pm
#        print r_tl