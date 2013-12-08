# -*- coding: utf-8 -*-

import numpy as np
from park_martin_calibration import ParkMartinCalibrator
from tsai_lenz_calibration import TsaiLenzCalibrator
from os.path import join as opj
from glob import glob

datadir = r'../data'
datafiles = [f for f in glob('%s/*.npy' % datadir)]  
calibrator_classes = [ParkMartinCalibrator, TsaiLenzCalibrator]

#norm_func = lambda M: np.linalg.det(M)    
#norm_func = lambda M: np.linalg.norm(M)    
#norm_func = lambda M: np.max(M)
norm_func = lambda M: np.max(np.abs(M))
filtering_top_limit = 1.0
