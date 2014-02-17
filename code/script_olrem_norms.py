# -*- coding: utf-8 -*-

'''
Remove outliers and see how it affects the result
'''

import params
from outliers import precision
from outliers.norms import NormsOutliersEliminator

if __name__ == '__main__':
    
    datafile = params.datafiles[0]
    top_limit = 0.7
    
    noe = NormsOutliersEliminator(datafile)
    noe.remove_outliers(top_limit)

    df1 = precision.get_oib_data_pandas(noe.old_object_in_base)
    df2 = precision.get_oib_data_pandas(noe.new_object_in_base)
    
    components = ['d1', 'd2', 'd3']
    for c in components:
        var1 = df1[c].var()
        var2 = df2[c].var()
        print c
        print var1, var2, var1 - var2    
    
    
    
    
    