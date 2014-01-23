# -*- coding: utf-8 -*-

'''
Set parameters
'''

import numpy as np
from hecalibrators.park_martin_calibration import ParkMartinCalibrator
from hecalibrators.tsai_lenz_calibration import TsaiLenzCalibrator
from glob import glob

datadir = r'../data'
datafiles = [f for f in glob('%s/*.npy' % datadir)]  
calibrator_classes = [ParkMartinCalibrator, TsaiLenzCalibrator]

norm_func_det = lambda M: np.linalg.det(M)    
norm_func_norm = lambda M: np.linalg.norm(M)    
norm_func_maxabs = lambda M: np.max(np.abs(M))

norm_func = norm_func_maxabs

