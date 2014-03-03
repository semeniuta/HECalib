# -*- coding: utf-8 -*-

'''
Absolute value test
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
    
    m1, m2 = precision.abs_value_test(noe, top_limits)

    
              
    
    
    
    
    