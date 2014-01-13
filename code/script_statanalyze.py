# -*- coding: utf-8 -*-

from optimization import optandinit as oi
import params
from scipy import stats

if __name__ == '__main__':

    target = 'mean'    
    datafile = params.datafiles[2]
    
    norms_initial, norms_optimal, opt = oi.compare(datafile, target)
    
    n1 = norms_initial[1]
    n2 = norms_optimal[1]
    
    stats.describe(n1)
    
    