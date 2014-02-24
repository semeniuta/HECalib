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

    for d in ['d1', 'd2', 'd3']:
        plt.figure()
        plt.plot(top_limits, v1[d], label='old var(%s)' % d)
        plt.plot(top_limits, v2[d], label='new var(%s)' % d)
        
        
        
    ''' Proposition for the aggregated indicator '''
    #diff = v1 - v2
    diff = v2 / v1
    s = diff['d1'] + diff['d2'] + diff['d3']
#    plt.figure()    
#    plt.plot(top_limits, diff['d1'], label='d1')
#    plt.plot(top_limits, diff['d2'], label='d2')
#    plt.plot(top_limits, diff['d3'], label='d3')
#    plt.plot(top_limits, s, label='Sum of variances')
#    plt.legend()
#    plt.title('Decrese in varince after outliers elimination')
#    plt.xlabel('Top limit')
#    plt.ylabel('Decrese in varince')
    
    
    
    
    