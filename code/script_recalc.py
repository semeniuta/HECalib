# -*- coding: utf-8 -*-

'''
Remove outliners and see how it affects the result
'''

import recalc
import params
import olrem
from helpers import stats
from matplotlib import pyplot as plt
from tcpcalibrators.park_martin_calibration import ParkMartinCalibrator

def calc_avg_min_max_norms(norms):
    s = stats.calc_statistics(norms)
    return s['mean'], s['min'], s['max']

if __name__ == '__main__':
    
    datafile = params.datafiles[2]
    pairs, AB, AB_pairs = olrem.read_pairs_and_calc_AB(datafile)
    res = olrem.process_pairs(pairs, AB, AB_pairs, ParkMartinCalibrator, params.norm_func)
        
    ''' Try Park-Martin calibration with new pairs '''
    top_limit = 0.5
    filtered_indices = recalc.filter_pairs(res['norms'], lambda x: x < top_limit)
    
    pmc = ParkMartinCalibrator(pairs)
    new_X = recalc.recalculate_X(pmc, filtered_indices)
    
    new_matrices, new_norms = olrem.calc_norms(AB, new_X, params.norm_func)
    old_norms = res['norms']
    
    print '\tavg\tmin\tmax'
    print 'Old:\t%.2f\t%.2f\t%.2f' % calc_avg_min_max_norms(old_norms)   
    print 'New:\t%.2f\t%.2f\t%.2f' % calc_avg_min_max_norms(new_norms)
    
    print '\nMatrix X (old):'
    print res['X']
    
    print '\nMatrix X (new):'
    print new_X
    
    plt.figure()
    plt.hist(old_norms, 100, color='blue')
    plt.hist(new_norms, 100, color='green')