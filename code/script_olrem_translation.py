# -*- coding: utf-8 -*-

'''
Idea from Schmidt et al (2003):
"Remove the positions where the changes in direction of translation of 
the robot arm are very high" (p. 6)
'''

import params
from outliers import precision
from outliers.translations import TranslationsOutliersEliminator
    
if __name__ == '__main__':
    
    datafile = params.datafiles[0]
    top_limit = 700
    
    toe = TranslationsOutliersEliminator(datafile)
    toe.remove_outliers(top_limit)
    
    df1 = precision.get_oib_data_pandas(toe.old_object_in_base)
    df2 = precision.get_oib_data_pandas(toe.new_object_in_base)    
    
    components = ['d1', 'd2', 'd3']
    for c in components:
        var1 = df1[c].var()
        var2 = df2[c].var()
        print c
        print var1, var2, var1 - var2
    
    
    
    
    
    
    
    
         
    
    
    
    