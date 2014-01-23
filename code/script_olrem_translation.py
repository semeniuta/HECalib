# -*- coding: utf-8 -*-

import params
import olrem
from hecalibrators.park_martin_calibration import ParkMartinCalibrator

if __name__ == '__main__':
    
    datafile = params.datafiles[0]
    pose_pairs, AB, combinations = olrem.read_pairs_and_calc_AB(datafile)  
    
    calib = ParkMartinCalibrator(pose_pairs)     
    X = calib.sensor_in_flange
    
    