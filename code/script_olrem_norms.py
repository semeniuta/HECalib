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
    
    target_values = []    
    for tlim in top_limits:    
        noe.remove_outliers(tlim)
    
        df1 = precision.get_oib_data_pandas(noe.old_object_in_base)
        df2 = precision.get_oib_data_pandas(noe.new_object_in_base)
        
        components = ['d1', 'd2', 'd3']
        var_diffs = [df1[c].var() - df2[c].var() for c in components]        
        target = sum(var_diffs)
        target_values.append(target)
        print tlim, target
        
    plt.figure()
    plt.plot(top_limits, target_values)
    
    
    
    
    