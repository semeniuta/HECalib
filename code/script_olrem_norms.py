# -*- coding: utf-8 -*-

'''
Remove outliers and see how it affects the result
'''

import recalc
import params
import olrem
from helpers import stats
from matplotlib import pyplot as plt
from hecalibrators.park_martin_calibration import ParkMartinCalibrator
from outliers import precision

def calc_avg_min_max_norms(norms):
    s = stats.calc_statistics(norms)
    return s['mean'], s['min'], s['max']

if __name__ == '__main__':
    
    ''' 
    Open data file with pose pairs (R, V) and calculate all 
    transformations (A, B)
    '''    
    datafile = params.datafiles[0]
    pose_pairs, AB, combinations = olrem.read_pairs_and_calc_AB(datafile)
    
    '''
    Perform calibration with ALL transformations and calculate norms 
    of |AX-XB| matrix
    '''
    old_pmc = ParkMartinCalibrator(pose_pairs)    
    old_X = old_pmc.sensor_in_flange
    old_matrices, old_norms = olrem.calc_norms(AB, old_X, params.norm_func)
        
    ''' 
    Filter out some of the transformations based on specified criterion
    '''
    top_limit = 0.7
    filtered_indices = recalc.filter_pairs(old_norms, lambda x: x < top_limit)
    
    '''
    Perform calibration without filtered transformations and calculate norms 
    of |AX-XB| matrix
    '''
    new_pmc = ParkMartinCalibrator(pose_pairs)
    new_pmc.update_move_pairs(filtered_indices)
    new_X = new_pmc.sensor_in_flange    
    new_matrices, new_norms = olrem.calc_norms(AB, new_X, params.norm_func)
    

    ''' Compare the difference '''
    '''    
    print '\tavg\tmin\tmax'
    print 'Old:\t%.2f\t%.2f\t%.2f' % calc_avg_min_max_norms(old_norms)   
    print 'New:\t%.2f\t%.2f\t%.2f' % calc_avg_min_max_norms(new_norms)
    
    print '\nMatrix X (old):'
    print old_X
    
    print '\nMatrix X (new):'
    print new_X
    
    plt.figure()
    plt.hist(old_norms, 100, color='blue')
    plt.hist(new_norms, 100, color='green')
    '''
    
    '''Calculate object to base transform: R*X*inv(V) '''
    object_to_base = precision.get_oib_data(pose_pairs, old_X)
    object_to_base_new = precision.get_oib_data(pose_pairs, new_X)
    
    precision.print_var(object_to_base, object_to_base_new)
    precision.print_mean(object_to_base, object_to_base_new)