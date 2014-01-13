# -*- coding: utf-8 -*-

''' 
Recalculate the calibration results using ParkMartinCalibrator
after removing outliners
'''

from helpers import stats
import params
import olrem
from tcpcalibrators.park_martin_calibration import ParkMartinCalibrator
import numpy as np

def recalculate_X(pmc):
    pmc._invalidate()
    update_move_pairs(pmc, filtered_indices)
    new_X = pmc.sensor_in_flange
    return new_X
    
def update_move_pairs(pmc, good_indices):
    move_pairs = list(pmc._move_pairs)
    good_move_pairs = []
    for ind in good_indices:
        good_move_pairs.append(move_pairs[ind])
    pmc._move_pairs = np.array(good_move_pairs)
    
def calc_avg_min_max_norms(norms):
    s = stats.calc_statistics(norms)
    return s['mean'], s['min'], s['max']
    
if __name__ == '__main__':
    
    datafile = params.datafiles[2]
    pairs, AB, AB_pairs = olrem.read_pairs_and_calc_AB(datafile)
    res = olrem.process_pairs(pairs, AB, AB_pairs, ParkMartinCalibrator, params.norm_func)
        
    ''' Try Park-Martin calibration with new pairs '''
    top_limit = 0.7
    filtered_indices = filtered_indices = olrem.filter_pairs(res['norms'], lambda x: x < top_limit)
    
    pmc = ParkMartinCalibrator(pairs)
    new_X = recalculate_X(pmc)
    
    new_matrices, new_norms = olrem.calc_norms(AB, new_X, params.norm_func)
    old_norms = res['norms']
    
    print '\tavg\tmin\tmax'
    print 'Old:\t%.2f\t%.2f\t%.2f' % calc_avg_min_max_norms(old_norms)   
    print 'New:\t%.2f\t%.2f\t%.2f' % calc_avg_min_max_norms(new_norms)
    
    print '\nMatrix X (old):'
    print res['X']
    
    print '\nMatrix X (new):'
    print new_X
        
        
        
        
    