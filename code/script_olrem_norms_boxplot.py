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
    
    top_limits = [0.01*i for i in range(45, math.trunc(100*max(noe.old_norms)), 10)]
    
    component = 'd1'
    
    samples = []    
    for tl in top_limits:
        noe.remove_outliers(tl)
        samples.append(precision.get_oib_data_pandas(noe.new_object_in_base)[component])
    
     
    