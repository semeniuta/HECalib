# -*- coding: utf-8 -*-

import numpy as np
from park_martin_calibration import ParkMartinCalibrator
from tsai_lenz_calibration import TsaiLenzCalibrator
from os.path import join as opj
from cvfunctions.output import create_histogram
import olrem

datadir = r'../data'
calibrator_classes = [ParkMartinCalibrator, TsaiLenzCalibrator]
    
def make_histograms(big_res):
    for r in big_res:
        norms = r['norms']
        create_histogram(norms, 20)

if __name__ == '__main__':
    pairs_datafile = opj(datadir, '20131114121046.npy')
    #norm_func = lambda M: np.linalg.det(M)    
    norm_func = lambda M: np.linalg.norm(M, -1)    
    filtering_top_limit = 0.001
    criterion = olrem.create_filtering_criterion(filtering_top_limit)
    
    pairs = olrem.read_pairs(pairs_datafile)
    AB = olrem.calc_AB(pairs)
    
    big_res = []
    for CalibratorClass in calibrator_classes:
        res_dict = olrem.process_pairs(pairs, AB, CalibratorClass, norm_func)
        big_res.append(res_dict)

#    ''' Print what norms are calculated for each calibration process '''
#    cal1, cal2 = big_res
#    for i in range(len(cal1['norms'])):
#        print i, cal1['norms'][i], cal2['norms'][i]
#
#    fi = olrem.filter_pairs(pairs, big_res[0]['norms'], criterion)
#    print fi


#    ''' Show histograms '''
#    make_histograms(big_res)    
    
    
#    ''' Analyze sample A and B '''
#    A, B = AB[0]
#    R, V = pairs[0]
#    Rnext, Vnext = pairs[1]    
#    print R
#    print Rnext
#    print V
#    print Vnext
#    print A
#    print B
    
    
        


    
    
    
