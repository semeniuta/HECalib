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
    
    precision.print_var(noe.old_object_in_base, noe.new_object_in_base)
    precision.print_mean(noe.old_object_in_base, noe.new_object_in_base)
    
    df = precision.get_oib_data_pandas(noe.new_object_in_base)
    