# -*- coding: utf-8 -*-

'''
Subtraction is not a defined operation in SE(3). You should use another way of 
assessing the error between AX and XB. E.g. find the (weighed average between) 
distance and angle among the two transforms AX and XB. If you use python(3)-
math3d and have defined XB=X*B and  AX=A*X get the angular and linear distances 
by

	XB.orient.ang_dist(AX.orient)

and 

	XB.pos.dist(AX.pos)

That way you may eliminate some surprises. Especially for the orientation 
part, you may find that in some pathological cases, M = AX - XB, may become 
huge whereas AX and XB are quite close in SE(3).
'''

import recalc
import params
import olrem
from hecalibrators.park_martin_calibration import ParkMartinCalibrator
from outliers import precision
from outliers.basic import BasicOutliersEliminator

class DistAngOutliersEliminator(BasicOutliersEliminator):
    
    def __init__(self, datafile):
        BasicOutliersEliminator.__init__(self, datafile)
        self.old_distances, self.old_angles = olrem.calc_distang(self.AB, self.old_sif)
        
        '''Calculate object to base transform: R*X*inv(V) '''
        self.old_object_in_base = precision.get_oib_data(self.pose_pairs, self.old_sif)
        
    def remove_outliers(self, top_limit):
        
        ''' 
        Filter out some of the transformations based on specified criterion
        '''
        filtered_indices = recalc.filter_pairs(self.old_distances, lambda x: x < top_limit)
        print filtered_indices
        
        '''
        Perform calibration without filtered transformation
        '''
        new_pmc = ParkMartinCalibrator(self.pose_pairs)
        new_pmc.update_move_pairs(filtered_indices)
        self.new_sif = new_pmc.sensor_in_flange    

        self.new_distances, self.new_angles = olrem.calc_distang(self.AB, self.new_sif)
        
        '''Calculate object to base transform: R*X*inv(V) '''
        self.new_object_in_base = precision.get_oib_data(self.pose_pairs, self.new_sif)
        