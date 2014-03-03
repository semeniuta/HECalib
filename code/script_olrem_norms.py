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
    print noe.old_norms    
    
    top_limits = [0.01*i for i in range(45, math.trunc(100*max(noe.old_norms)))]
    
    ''' Variances '''    
    v1, v2 = precision.precision_test(noe, top_limits, components=['d1', 'd2', 'd3'])

    ''' Cumulative varinces '''
    s1 = v1['d1'] + v1['d2'] + v1['d3']
    s2 = v2['d1'] + v2['d2'] + v2['d3']

    index_min = s2.index[s2.argmin()]
            
    colors = ['blue', 'green', 'orange']
    components = ['d1', 'd2', 'd3']
    plt.figure()
    for i in range(len(components)):
        d = components[i]
        c = colors[i]
        plt.plot(top_limits, v1[d], label='old var(%s)' % d, color=c, linestyle='--')
        plt.plot(top_limits, v2[d], label='new var(%s)' % d, color=c)
    plt.legend()
    plt.xlabel('Value of threshold')
    plt.ylabel('Varince')
    plt.vlines(index_min, plt.ylim()[0], plt.ylim()[1], color='r', linestyle='--')
    dfile = datafile.split('/')[-1].split('.')[0]    
    plt.savefig('../../%s_each.png' % dfile)
        
    plt.figure()
    plt.plot(top_limits, s1, label='Sum of variances before removing outliers', linestyle='--')
    plt.plot(top_limits, s2, label='Sum of variances after removing outliers')
    plt.legend()
    plt.xlabel('Value of threshold')
    plt.ylabel('Sum of varinces')
    plt.vlines(index_min, plt.ylim()[0], plt.ylim()[1], color='r', linestyle='--')
    plt.savefig('../../%s_sum.png' % dfile)
    
    print s2.min(), index_min
              
    
    
    
    
    