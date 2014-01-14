# -*- coding: utf-8 -*-

'Call scipy.stats.describe on the intial and optimized norms'

from optimization import optandinit as oi
import params
from scipy import stats

if __name__ == '__main__':

    target = 'mean'    
    datafile = params.datafiles[2]
    
    norms_initial, norms_optimal, opt = oi.compare(datafile, target)
    
    print stats.describe(norms_initial)
    print stats.describe(norms_optimal)
    
    