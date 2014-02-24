# -*- coding: utf-8 -*-

'''
Idea from Schmidt et al (2003):
"Remove the positions where the changes in direction of translation of 
the robot arm are very high" (p. 6)
'''

import math
import recalc
import params
import olrem
from hecalibrators.park_martin_calibration import ParkMartinCalibrator
from outliers import precision
from outliers.basic import BasicOutliersEliminator

def get_translation_vector(M):
    ''' Last column without the leading "1" '''
    return M.matrix[:-1, -1]
    
def calc_vector_len(vec):
    return math.sqrt(sum([el**2 for el in vec]))

class TranslationsOutliersEliminator(BasicOutliersEliminator):
        
    def remove_outliers(self, top_limit):
            
        ''' 
        Filter out some of the transformations based on specified criterion
        '''
        lengths = [calc_vector_len(get_translation_vector(A)) for A, B in self.AB]  
        filtered_indices = recalc.filter_pairs(lengths, lambda x: x < top_limit)
        
        '''
        Perform calibration without filtered transformations and calculate norms 
        of |AX-XB| matrix
        '''
        new_pmc = ParkMartinCalibrator(self.pose_pairs)
        new_pmc.update_move_pairs(filtered_indices)
        self.new_sif = new_pmc.sensor_in_flange    
        new_matrices, self.new_norms = olrem.calc_norms(self.AB, self.new_sif, params.norm_func)
        
        '''Calculate object to base transform: R*X*inv(V) '''
        self.old_object_in_base = precision.get_oib_data(self.pose_pairs, self.old_sif)
        self.new_object_in_base = precision.get_oib_data(self.pose_pairs, self.new_sif)