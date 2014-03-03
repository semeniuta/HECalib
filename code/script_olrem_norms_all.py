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
    
    datafile = params.datafiles[1]

    noe = NormsOutliersEliminator(datafile)    
    print noe.old_norms    
    
    top_limits = [0.01*i for i in range(50, math.trunc(100*max(noe.old_norms)))]
    
    ''' Variances '''    
    v1, v2 = precision.precision_test(noe, top_limits)

    ''' Cumulative varinces '''
    first_name = precision.COLNAMES[0]
    s1 = v1[first_name]
    s2 = v2[first_name]
    for component_name in precision.COLNAMES[1:]:
        s1 += v1[component_name]    
        s2 += v2[component_name]    
    
    
    index_min = s2.index[s2.argmin()]
        
    plt.figure()
    plt.plot(top_limits, s1, label='Sum of variances before removing outliers')
    plt.plot(top_limits, s2, label='Sum of variances after removing outliers')
    plt.legend()
    plt.xlabel('Value of threshold')
    plt.ylabel('Sum of varinces')
    plt.vlines(index_min, plt.ylim()[0], plt.ylim()[1], color='r')
              
    
    
    
    
    