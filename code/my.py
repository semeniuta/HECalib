# -*- coding: utf-8 -*-

import numpy as np
import math3d as m3d
from park_martin_calibration import ParkMartinCalibrator
from tsai_lenz_calibration import TsaiLenzCalibrator
from os.path import join as opj
import outlinersremove as olrem

datadir = r'../data'

calib = np.load(opj(datadir, '20131114121046.npy'))

parkmartin = ParkMartinCalibrator(calib)
tsailenz = TsaiLenzCalibrator(calib)

res_pm = parkmartin.sensor_in_flange
res_tl = tsailenz.sensor_in_flange

pose_pairs = parkmartin._pose_pairs
move_pairs = parkmartin._move_pairs

R, V = pose_pairs[0]
Rnext, Vnext = pose_pairs[1]
A, B = move_pairs[0]

print R
print Rnext
print V
print Vnext
print A.move
print B.move


