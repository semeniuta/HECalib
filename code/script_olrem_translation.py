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
    
    precision.print_var(toe.old_object_in_base, toe.new_object_in_base)
    precision.print_mean(toe.old_object_in_base, toe.new_object_in_base)
    
    
    
    
    
    
    
    
         
    
    
    
    