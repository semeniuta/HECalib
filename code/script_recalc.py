# -*- coding: utf-8 -*-

import recalc
import params
import olrem
from tcpcalibrators.park_martin_calibration import ParkMartinCalibrator

if __name__ == '__main__':
    
    datafile = params.datafiles[2]
    pairs, AB, AB_pairs = olrem.read_pairs_and_calc_AB(datafile)
    res = olrem.process_pairs(pairs, AB, AB_pairs, ParkMartinCalibrator, params.norm_func)
        
    ''' Try Park-Martin calibration with new pairs '''
    top_limit = 0.7
    filtered_indices = filtered_indices = olrem.filter_pairs(res['norms'], lambda x: x < top_limit)
    
    pmc = ParkMartinCalibrator(pairs)
    new_X = recalc.recalculate_X(pmc, filtered_indices)
    
    new_matrices, new_norms = olrem.calc_norms(AB, new_X, params.norm_func)
    old_norms = res['norms']
    
    print '\tavg\tmin\tmax'
    print 'Old:\t%.2f\t%.2f\t%.2f' % recalc.calc_avg_min_max_norms(old_norms)   
    print 'New:\t%.2f\t%.2f\t%.2f' % recalc.calc_avg_min_max_norms(new_norms)
    
    print '\nMatrix X (old):'
    print res['X']
    
    print '\nMatrix X (new):'
    print new_X