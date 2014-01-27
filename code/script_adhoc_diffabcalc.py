# -*- coding: utf-8 -*-


'''
In the calibrators by Morten Lind and Lars Tingelstad, A and B 
transformations are calculated in this way:
A = inv(R1)*R2
B = inv(V1)*V2

However, in the literature transformations are calculated differently:
A = inv(R2)*R1
B = V2*inv(V1)

This is derived from the following:
[BASE]-(Ri)->[GRIPPER]-(X)->[CAMERA]-(Vi)->[OBJECT]
R1*X*V1 = R2*X*V2
inv(R2)*R1*X = X*V2*inv(V1)
AX = XB, where A = inv(R2)*R1, B = V2*inv(V1) 
'''

import params
import olrem
from hecalibrators.park_martin_calibration import ParkMartinCalibrator as PMC1
from hecalibrators.park_martin_calibration2 import ParkMartinCalibrator as PMC2

if __name__ == '__main__':
    
    datafile = params.datafiles[1]
    pose_pairs, AB, combinations = olrem.read_pairs_and_calc_AB(datafile)
    
    pmc1 = PMC1(pose_pairs)    
    pmc2 = PMC2(pose_pairs)    
    X1 = pmc1.sensor_in_flange
    X2 = pmc2.sensor_in_flange
    
    print X1, X2    
    
    R0, V0 = pose_pairs[0]
    R1, V1 = pose_pairs[1]
    '''
    # Shat et al / Shiu and Ahmad
    print R0*X2*V0
    print R1*X2*V1
    
    # Morten Lind            
    print R0.inverse()*R1*X1
    print X1*V0.inverse()*V1
    '''