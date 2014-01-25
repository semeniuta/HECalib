# -*- coding: utf-8 -*-


import params
import olrem
from hecalibrators.park_martin_calibration2 import ParkMartinCalibrator as PMC1
from hecalibrators.park_martin_calibration2 import ParkMartinCalibrator as PMC2

if __name__ == '__main__':
    
    datafile = params.datafiles[1]
    pose_pairs, AB, combinations = olrem.read_pairs_and_calc_AB(datafile)
    
    pmc1 = PMC1(pose_pairs)    
    pmc2 = PMC2(pose_pairs)    
    X1 = pmc1.sensor_in_flange
    X2 = pmc2.sensor_in_flange

    print X1
    print X2

#    matrices, norms = olrem.calc_norms(AB, X, params.norm_func)
#    
#    print X
#    
#    R, V = pose_pairs[0]
#    
#    print R
#    print V
#    print X*V
#    print V*X    
    
    