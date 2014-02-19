# -*- coding: utf-8 -*-

'''
Remove outliers and see how it affects the result
'''

import math
import params
from outliers import precision
from outliers.norms import NormsOutliersEliminator
from matplotlib import pyplot as plt

if __name__ == '__main__':
    
    datafile = params.datafiles[0]

    noe = NormsOutliersEliminator(datafile)    
    
    top_limits = [0.01*i for i in range(34, math.trunc(100*max(noe.old_norms)))]
    
    v1, v2 = precision.precision_test(noe, top_limits)
    diff = v1 - v2
    s = diff['d1'] + diff['d2'] + diff['d3']
    
    plt.figure()    
    plt.plot(top_limits, diff['d1'])
    plt.plot(top_limits, diff['d2'])
    plt.plot(top_limits, diff['d3'])
    plt.plot(top_limits, s)
    
    
    
    
    