# -*- coding: utf-8 -*-

import olrem
from hecalibrators.park_martin_calibration import ParkMartinCalibrator

class BasicOutliersEliminator:
    def __init__(self, datafile):
        
        ''' 
        Open data file with pose pairs (R, V) and calculate all 
        transformations (A, B)
        '''    
        self.pose_pairs, self.AB, combinations = olrem.read_pairs_and_calc_AB(datafile)
        
        '''
        Perform calibration with ALL transformations
        '''
        old_pmc = ParkMartinCalibrator(self.pose_pairs)    
        self.old_sif = old_pmc.sensor_in_flange
        
                