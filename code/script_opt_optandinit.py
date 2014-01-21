# -*- coding: utf-8 -*-

'''
For the given data file, optimized distribution of X is unpicked
and compared with the original one
'''

from optimization import optandinit
import params
from helpers import stats

if __name__ == '__main__':

    target = 'mean'
    datafile = params.datafiles[0]
        
    norms_initial, norms_optimal, opt = optandinit.compare(datafile, target)
    
    print opt.XInitial
    print opt.XOptimal    
    
    s_initial = stats.calc_statistics(norms_initial)
    s_optimal = stats.calc_statistics(norms_optimal)
    
    stats.print_statistics_header()
    stats.print_statistics(s_initial)    
    stats.print_statistics(s_optimal)
    
    optandinit.create_comparison_histogram(norms_initial, norms_optimal, opt, datafile)
